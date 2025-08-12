import asyncio
import uuid
from contextlib import asynccontextmanager
from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

import app.chat.prompts
from app.api.gemini import ChatSession, Content, load_chat, new_chat
from app.chat.prompts import get_prompt
from app.dependencies import User, get_user
from app.logging_config import get_logger
from app.utils import watch_prompts_folder

log = get_logger(__name__)


class ChatRequest(BaseModel):
    """Model for chat request."""

    message: str


class NewChatResponse(BaseModel):
    """Response model for new chat request."""

    chat_id: str


class ChatDataResponse(BaseModel):
    """Response model for chat data."""

    user_id: str
    chat_id: str
    agent: str
    history: List[Content]


@asynccontextmanager
async def lifespan(router: APIRouter):
    """Lifespan context manager specifically for the chat router."""
    # Load prompts dict.
    prompts_dict, task = watch_prompts_folder(app.chat.prompts)
    chat_cache = {}

    try:
        yield dict(
            prompts=prompts_dict,
            chats=chat_cache,
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


async def get_chats(req: Request) -> Dict[str, ChatSession]:
    """Get the chat sessions dictionary."""
    return req.state.chats


router = APIRouter(lifespan=lifespan)


@router.get("/new")
async def route_new_chat(
    agent: str,
    prompts: Annotated[Dict[str, str], Depends(get_prompts)],
    chats: Annotated[Dict[str, ChatSession], Depends(get_chats)],
    user: Annotated[User, Depends(get_user)],
) -> NewChatResponse:
    """Handle chat requests."""
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not authenticated.",
        )
    prompt = get_prompt(agent, prompts)
    if prompt is None:
        raise HTTPException(
            status_code=400,
            detail=f"Prompt for agent '{agent}' not found.",
        )

    chat_id = f"{user.id}.{agent}.{uuid.uuid4().hex}"
    chats[chat_id] = new_chat(chat_id, user.id, agent)
    await chats[chat_id].chat.send_message(prompt)

    return NewChatResponse(chat_id=chat_id)


@router.get("/{chat_id}")
async def route_get_chat(
    chat_id: str,
    chats: Annotated[Dict[str, ChatSession], Depends(get_chats)],
) -> ChatDataResponse:
    """Get chat history by chat ID."""
    log.info(f"Retrieving chat history for chat ID: {chat_id}")
    try:
        session = chats.setdefault(chat_id, load_chat(chat_id))
        obj = ChatDataResponse(
            user_id=session.user_id,
            chat_id=session.chat_id,
            agent=session.agent,
            history=session.chat.get_history(curated=True),
        )
        return obj
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail=f"Chat with ID {chat_id} not found.",
        )


@router.post("/{chat_id}/message")
async def route_send_message(
    chat_id: str,
    req: ChatRequest,
    chats: Annotated[Dict[str, ChatSession], Depends(get_chats)],
) -> str:
    """Send a message to the chat."""
    log.info(f"Sending message to chat ID {chat_id}: {req.message}")

    try:
        session = chats.setdefault(chat_id, load_chat(chat_id))
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail=f"Chat with ID {chat_id} not found.",
        )

    response = await session.chat.send_message(req.message)
    text = response.text
    if not text:
        raise HTTPException(
            status_code=500,
            detail="Received empty response from chat service.",
        )

    return text


# Test route that lets me get prompt file by name.
@router.get("/prompts/{prompt_name}")
async def route_prompt(
    prompt_name: str, prompts: Annotated[Dict[str, str], Depends(get_prompts)]
) -> str:
    """Get a prompt by its name."""
    log.info(
        f"Retrieved prompt: {prompt_name}, available prompts: {list(prompts.keys())}"
    )
    if prompt_name not in prompts:
        return "Prompt not found."
    return prompts[prompt_name]
