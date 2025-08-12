"""
Logging configuration for the application.

This module provides centralized logging configuration that works well with FastAPI/uvicorn
without causing duplicate log messages.
"""

import logging
import sys
from typing import Optional


def setup_logging(log_level: str = "INFO", force_setup: bool = False) -> None:
    """
    Set up application logging configuration.

    Args:
        log_level: The logging level to use (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        force_setup: If True, will reconfigure logging even if already set up
    """
    # Configure the app logger hierarchy
    app_logger = logging.getLogger("app")
    app_logger.setLevel(getattr(logging, log_level.upper()))

    # Only add handler if it doesn't already exist or if forced
    if not app_logger.handlers or force_setup:
        # Clear existing handlers if forcing setup
        if force_setup:
            app_logger.handlers.clear()

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s|%(levelname)s|%(name)s: %(message)s", "%H:%M"
        )
        handler.setFormatter(formatter)
        app_logger.addHandler(handler)
        app_logger.propagate = False  # Prevent propagation to root logger

        # Also ensure that our handler has the highest priority
        handler.setLevel(getattr(logging, log_level.upper()))

    # Prevent uvicorn from overriding our configuration
    # by setting a custom attribute that we can check later
    setattr(app_logger, "_custom_configured", True)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance for the application.

    Args:
        name: The logger name. If None, uses the caller's module name.

    Returns:
        A logger instance under the 'app' hierarchy.
    """
    # Check if our logging was overridden by uvicorn and re-setup if needed
    app_logger = logging.getLogger("app")
    if not getattr(app_logger, "_custom_configured", False) or not app_logger.handlers:
        setup_logging(force_setup=True)

    if name is None:
        # Get the caller's module name
        import inspect

        frame = inspect.currentframe()
        if frame and frame.f_back:
            name = frame.f_back.f_globals.get("__name__", "app")
        else:
            name = "app"

    # At this point name is guaranteed to be a string
    assert isinstance(name, str)

    # Ensure the logger is under the app hierarchy
    if not name.startswith("app."):
        name = f"app.{name}"

    return logging.getLogger(name)
