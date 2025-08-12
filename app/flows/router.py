import asyncio
import json
from contextlib import asynccontextmanager
from types import ModuleType
from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends, HTTPException, Request
from google.genai.types import Content, GenerateContentConfig, Part

from app.api.gemini import client
from app.config import CONFIG
from app.flows.structs import QuizRequest, QuizResponse, StageInfo
from app.logging_config import get_logger
from app.utils import watch_prompts_folder


def create_quiz_router(module: ModuleType) -> APIRouter:
    """Create a quiz router with the specified module."""
    assert isinstance(getattr(module, "STAGES", None), list), (
        "Module must have a 'STAGES' list defined."
    )
    stage_map: Dict[str, StageInfo] = {s.id: s for s in module.STAGES}
    stage_order: List[str] = [s.id for s in module.STAGES]

    log = get_logger(f"{__name__}.{module.__name__}")

    @asynccontextmanager
    async def lifespan(router: APIRouter):
        nonlocal module
        prompts_dict, task = watch_prompts_folder(module)

        try:
            yield {
                f"prompts_{module.__name__}": prompts_dict,
            }
        finally:
            if not task.done():
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

    async def get_prompts(req: Request) -> Dict[str, str]:
        """Get the prompts dictionary."""
        return getattr(req.state, f"prompts_{module.__name__}", {})

    router = APIRouter(lifespan=lifespan)

    @router.post("/send")
    async def send_message(
        req: QuizRequest, prompts: Annotated[Dict[str, str], Depends(get_prompts)]
    ) -> QuizResponse:
        nonlocal stage_map, stage_order

        log.info(f"Request:\n{json.dumps(req.model_dump(), indent=2)}")

        # Send initial info for frontend to render.
        if req.stage_id is None:
            return QuizResponse(stages=stage_map, next_stage=stage_order[0])

        if req.stage_id not in stage_map:
            raise HTTPException(status_code=400, detail="Invalid stage")

        stage = stage_map[req.stage_id]
        next_idx = stage_order.index(req.stage_id) + 1
        next_stage = stage_order[next_idx] if next_idx < len(stage_order) else None

        if not stage.has_model_reply:
            return QuizResponse(
                stages=stage_map,
                next_stage=next_stage,
                user_inputs=req.user_inputs,
                model_replies=req.model_replies,
            )

        assert stage.prompt_name in prompts, (
            f"Prompt '{stage.prompt_name}' not found in prompts: {prompts.keys()}."
        )
        stage_prompt = prompts[stage.prompt_name]

        contents: List[Content] = [
            Content(role="user", parts=[Part.from_text(text="")])
        ]

        # Append in order: hardcoded model_content, user input, model replies, then empty user input.
        for id in stage_order:
            sta = stage_map[id]
            if sta.has_user_input:
                model_content = sta.model_content or stage.content or ""
                if contents[-1].role == "model":
                    contents.append(
                        Content(role="user", parts=[Part.from_text(text="")])
                    )
                contents += [
                    Content(role="model", parts=[Part.from_text(text=model_content)]),
                    Content(
                        role="user",
                        parts=[Part.from_text(text=req.user_inputs.get(id, ""))],
                    ),
                ]
            if sta.has_model_reply:
                model_reply = req.model_replies.get(id, "")
                if contents[-1].role == "model":
                    contents.append(
                        Content(role="user", parts=[Part.from_text(text="")])
                    )
                contents.append(
                    Content(role="model", parts=[Part.from_text(text=model_reply)])
                )

            if id == stage.id:
                break

        log.info(
            f"Contents to send:\n{json.dumps([c.model_dump() for c in contents], indent=2)}"
        )

        resp = await client.aio.models.generate_content(
            model=CONFIG.gemini_model,
            contents=contents,
            config=GenerateContentConfig(
                system_instruction=stage_prompt,
            ),
        )
        req.model_replies[stage.id] = resp.text or ""

        return QuizResponse(
            stages=stage_map,
            next_stage=next_stage,
            user_inputs=req.user_inputs,
            model_replies=req.model_replies,
        )

    return router
