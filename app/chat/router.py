import asyncio
from contextlib import asynccontextmanager
from typing import Annotated, Dict, Literal

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

import app.chat.prompts
from app.logging_config import get_logger
from app.utils import watch_prompts_folder

log = get_logger(__name__)


class ChatRequest(BaseModel):
    """Model for chat request."""

    message: str
    agent: Literal["nervy"]


@asynccontextmanager
async def lifespan(router: APIRouter):
    """Lifespan context manager specifically for the chat router."""
    # Load prompts dict.
    prompts_dict, task = watch_prompts_folder(app.chat.prompts)

    try:
        yield dict(
            prompts=prompts_dict,
        )
    finally:
        # Cancel the task if it is still running.
        if not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass


async def get_prompts(req: Request) -> Dict[str, str]:
    """Get the prompts dictionary."""
    return req.state.prompts


router = APIRouter(lifespan=lifespan)


# Test route that lets me get prompt file by name.
@router.get("/prompts/{prompt_name}")
async def get_prompt(
    prompt_name: str, prompts: Annotated[Dict[str, str], Depends(get_prompts)]
) -> str:
    """Get a prompt by its name."""
    log.info(
        f"Retrieved prompt: {prompt_name}, available prompts: {list(prompts.keys())}"
    )
    if prompt_name not in prompts:
        return f"Prompt '{prompt_name}' not found."
    return prompts[prompt_name]
