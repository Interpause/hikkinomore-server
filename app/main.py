import importlib
import pkgutil

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

import app.flows
from app.chat.router import router as chat_router
from app.dependencies import lifespan
from app.flows.router import create_quiz_router
from app.logging_config import get_logger

__all__ = ["api"]


log = get_logger(__name__)


def discover_quiz_modules():
    """Discover all quiz modules in app.flows that have STAGES defined."""
    quiz_modules = []

    # Get the flows package path
    flows_path = app.flows.__path__

    # Iterate through all modules in the flows package
    for module_info in pkgutil.iter_modules(flows_path, app.flows.__name__ + "."):
        try:
            # Import the module
            module = importlib.import_module(module_info.name)

            # Check if the module has STAGES defined
            if hasattr(module, "STAGES") and isinstance(
                getattr(module, "STAGES"), list
            ):
                # Extract the module name (last part after the dot)
                module_name = module_info.name.split(".")[-1]
                quiz_modules.append((module_name, module))
                log.info(f"Discovered quiz module: {module_name}")

        except Exception as e:
            log.warning(f"Failed to import module {module_info.name}: {e}")

    return quiz_modules


api = FastAPI(lifespan=lifespan)

# Custom exception handler for SPA routing
@api.exception_handler(StarletteHTTPException)
async def spa_handler(request: Request, exc: StarletteHTTPException):
    """
    Handle 404 errors by serving index.html for non-API routes.
    This enables client-side routing for the React SPA.
    """
    if exc.status_code == 404:
        # Check if this is an API request
        if request.url.path.startswith("/api/"):
            # Return the original 404 for API routes
            return exc
        
        # For all other routes, serve index.html to enable SPA routing
        return FileResponse("public/index.html")
    
    return exc

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["chat"],
)

# Automatically discover and register all quiz modules
quiz_modules = discover_quiz_modules()
for module_name, module in quiz_modules:
    api.include_router(
        create_quiz_router(module),
        prefix=f"/api/{module_name}",
        tags=[module_name],
    )
    log.info(f"Registered quiz router for {module_name} at /api/{module_name}")

# Must be mounted last.
api.mount("/", StaticFiles(directory="public", html=True))
