import asyncio
import re
import types
from pathlib import Path
from typing import Dict, Tuple, Union

from watchfiles import Change, awatch

from app.logging_config import get_logger

log = get_logger(__name__)


def _load_prompt_file(file_path: Path) -> str:
    """Load and process a single prompt file."""
    with file_path.open(encoding="utf-8") as f:
        content = f.read()
        # Remove all <!-- ... --> comments (including multiline), including surrounding whitespace/newlines.
        content = re.sub(
            r"^[ \t]*<!--.*?-->[ \t]*(\r?\n)?",
            "",
            content,
            flags=re.DOTALL | re.MULTILINE,
        )
        return content.strip()


def watch_prompts_folder(
    module_or_path: Union[types.ModuleType, str],
) -> Tuple[Dict[str, str], asyncio.Task]:
    """Watch a folder for markdown file changes and update prompts dictionary.

    Args:
        module_or_path: Either a module object (e.g., app.chat.prompts) or a string path
            to the directory containing markdown files

    Returns:
       Tuple of dictionary to update with prompt changes (modified in-place) and
       an asyncio Task that runs the watcher
    """
    prompts_dict = {}

    # Determine the directory path
    if isinstance(module_or_path, types.ModuleType):
        if module_or_path.__file__ is None:
            raise ValueError(
                f"Module {module_or_path} does not have a __file__ attribute"
            )
        dir_path = Path(module_or_path.__file__).parent
    else:
        dir_path = Path(module_or_path)

    if not dir_path.is_dir():
        raise ValueError(f"Provided path '{dir_path}' is not a directory.")

    for md_file in dir_path.glob("*.md"):
        try:
            prompts_dict[md_file.stem] = _load_prompt_file(md_file)
            log.info(f"Loaded existing prompt file: {md_file.stem}")
        except Exception as e:
            log.error(f"Error loading existing prompt file {md_file}: {e}")

    # Custom filter to only watch .md files
    def md_filter(change: Change, path: str) -> bool:
        return Path(path).suffix == ".md"

    async def watch_task():
        async for changes in awatch(dir_path, watch_filter=md_filter):
            for change, path in changes:
                file_path = Path(path)
                file_stem = file_path.stem

                if change == Change.deleted:
                    # Remove from prompts dict if file was deleted
                    prompts_dict.pop(file_stem, None)
                elif change in (Change.added, Change.modified):
                    # Load/reload the file content
                    try:
                        prompts_dict[file_stem] = _load_prompt_file(file_path)
                        log.info(f"Loaded prompt file: {file_stem}")
                    except Exception as e:
                        # Handle file read errors gracefully
                        log.error(f"Error loading prompt file {file_path}: {e}")
                        prompts_dict.pop(file_stem, None)

    task = asyncio.create_task(watch_task())
    return prompts_dict, task
