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


def get_initial_message(agent: str) -> str:
    """I am lazy."""
    if agent == "general":
        return "I am Buddy, how are you doing?"
    elif agent == "nervy":
        return "Hey… thanks for choosing me. I totally get what it’s like to overthink every word. Wanna practice chatting with someone who won’t judge you at all? 😊 What kind of social situations make you feel nervous?"
    elif agent == "avoi":
        return "Hi there. I know small talk can feel… weird. You can talk to me like a colleague, or like a friend—no pressure. Want to start by telling me how your day’s been, casually?"
    elif agent == "enthu":
        return "Hi! I’m all ears if you’ve got something cool to share—I love when people are passionate. Want to tell me about something you’re really into lately? Then I’ll help you figure out how to keep others interested too!"
    elif agent == "iso":
        return "Hey. You don’t have to be super social to want connection—I’m here for small steps. Maybe we could just talk about something simple. What’s something you enjoy doing alone?"
    else:
        return "How can I help you today?"
