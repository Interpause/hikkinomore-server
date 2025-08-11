from fastapi import FastAPI

__all__ = ["app"]

app = FastAPI()


@app.get("/")
async def root() -> str:
    """Route that returns hello world."""
    return "Hello world!"
