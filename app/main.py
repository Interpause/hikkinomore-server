from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.flows.quiz1
from app.chat.router import router as chat_router
from app.dependencies import get_user, lifespan
from app.flows.router import create_quiz_router
from app.logging_config import get_logger

__all__ = ["api"]


log = get_logger(__name__)

api = FastAPI(lifespan=lifespan)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(
    chat_router,
    prefix="/chat",
    tags=["chat"],
)

api.include_router(
    create_quiz_router(app.flows.quiz1),
    prefix="/quiz1",
    tags=["quiz1"],
)


@api.get("/")
async def root(user: Annotated[Optional[dict], Depends(get_user)]) -> str:
    """Route that returns hello world."""
    if user is None:
        return "Hello world!"
    else:
        return f"Hello {user['name']}!"
