from fastapi import FastAPI

from app.config import Config

__all__ = ["app"]

config = Config()  # type: ignore
app = FastAPI()


@app.get("/")
async def root() -> str:
    """Route that returns hello world."""
    return "Hello world!"
