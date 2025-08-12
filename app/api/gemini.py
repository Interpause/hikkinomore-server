import json
from dataclasses import dataclass
from pathlib import Path

from google.genai import Client
from google.genai.chats import AsyncChat
from google.genai.types import Content

from app.config import CONFIG

SAVE_LOCATION = "./data/"

# TODO: this should probably be a fastapi dep
client = Client(api_key=CONFIG.gemini_api_key)


@dataclass
class ChatSession:
    """Dataclass to hold chat session information."""

    user_id: str
    chat_id: str
    agent: str
    chat: AsyncChat


def save_chat(chat_id: str, chat: ChatSession):
    """Save chat history locally."""
    Path(SAVE_LOCATION).mkdir(parents=True, exist_ok=True)
    # TODO: Make this safe
    save_path = Path(SAVE_LOCATION) / f"{chat_id}.json"
    hist = chat.chat.get_history(curated=True)
    hist = [msg.to_json_dict() for msg in hist]
    obj = dict(
        user_id=chat.user_id,
        chat_id=chat.chat_id,
        agent=chat.agent,
        history=hist,
    )
    with save_path.open("w", encoding="utf-8") as f:
        json.dump(obj, f)


def load_chat(chat_id: str):
    """Load chat history from local storage."""
    save_path = Path(SAVE_LOCATION) / f"{chat_id}.json"
    if not save_path.exists():
        raise FileNotFoundError(f"Chat with ID {chat_id} not found.")

    with save_path.open("r", encoding="utf-8") as f:
        obj = json.load(f)
    hist = obj["history"]
    user_id = obj["user_id"]
    agent = obj["agent"]
    hist = [Content.model_validate(msg) for msg in hist]

    chat = client.aio.chats.create(model=CONFIG.gemini_model, history=hist)
    return ChatSession(
        user_id=user_id,
        chat_id=chat_id,
        agent=agent,
        chat=chat,
    )


def new_chat(chat_id: str, user_id: str, agent: str):
    """Create a new chat session."""
    chat = client.aio.chats.create(model=CONFIG.gemini_model)
    obj = ChatSession(
        user_id=user_id,
        chat_id=chat_id,
        agent=agent,
        chat=chat,
    )
    save_chat(chat_id, obj)
    return obj
