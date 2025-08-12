"""Dependencies for the whole FastAPI app, and the lifespan context for them.

Note that router specific lifespan and dependencies should be defined in the router's
module instead.
"""

from contextlib import asynccontextmanager
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, Request
from pydantic import BaseModel

from app.logging_config import get_logger, setup_logging

log = get_logger(__name__)


class User(BaseModel):
    """Placeholder for user model. Replace with actual user model as needed."""

    name: str
    id: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Put only heavy loading or cleanup tasks for the whole app."""
    # TODO: Initialize user study logging
    setup_logging(force_setup=True)

    # TODO: Below is placeholder for deps system
    try:
        yield dict(
            db={},
        )
    ### Clean up tasks go below here:
    finally:
        pass


async def get_db(req: Request) -> dict:
    """Get database handle."""
    return req.state.db


async def get_user(
    db: Annotated[dict, Depends(get_db)],
    user_id: Optional[str] = None,
) -> Optional[User]:
    """Get user information if `user_id` is given."""
    if user_id is None:
        return None

    # TODO: Below is all placeholder.
    user = db.get("users", {}).get(user_id)
    if user is None:
        return User(
            name="placeholder",
            id=user_id,
        )
