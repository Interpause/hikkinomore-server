"""Hardcode the selected prompts here."""

from typing import Optional

PROMPT_AVOI = "chat_avoi"
PROMPT_ENTHU = "chat_enthu"
PROMPT_ISO = "chat_iso"
PROMPT_NERVY = "chat_nervy"
PROMPT_GENERAL = "chat_general"


def get_prompt(agent: str, prompts: dict) -> Optional[str]:
    """Get the prompt for the specified agent."""
    if agent == "general":
        return prompts.get(PROMPT_GENERAL, None)
    elif agent == "nervy":
        return prompts.get(PROMPT_NERVY, None)
    elif agent == "avoi":
        return prompts.get(PROMPT_AVOI, None)
    elif agent == "enthu":
        return prompts.get(PROMPT_ENTHU, None)
    elif agent == "iso":
        return prompts.get(PROMPT_ISO, None)
    else:
        return None
