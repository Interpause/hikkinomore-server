from contextlib import asynccontextmanager
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, Request


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Put only heavy loading or cleanup tasks here."""
    # TODO: Initialize user study logging

    # TODO: Below is placeholder for deps system
    yield dict(
        db={},
    )

    ### Clean up tasks go below here:


async def get_db(request: Request) -> dict:
    """Get database handle."""
    return request.state.db


async def get_user(
    db: Annotated[dict, Depends(get_db)],
    user_id: Optional[str] = None,
) -> Optional[dict]:
    """Get user information if `user_id` is given."""
    if user_id is None:
        return None

    # TODO: Below is all placeholder.
    user = db.get("users", {}).get(user_id)
    if user is None:
        return {"name": "placeholder", "id": user_id}
