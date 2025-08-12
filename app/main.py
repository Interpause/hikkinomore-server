from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.chat.router import router as chat_router
from app.dependencies import get_user, lifespan
from app.logging_config import get_logger

__all__ = ["app"]


log = get_logger(__name__)

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["chat"],
)


@app.get("/")
async def root(user: Annotated[Optional[dict], Depends(get_user)]) -> str:
    """Route that returns hello world."""
    if user is None:
        return "Hello world!"
    else:
        return f"Hello {user['name']}!"
