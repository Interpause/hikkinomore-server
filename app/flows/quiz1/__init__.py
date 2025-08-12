"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        content="Welcome to the quiz!",
    ),
    StageInfo(
        id="question_1",
        content="How do you feel?",
        model_content="Quiz page says: How do you feel?",
        has_user_input=True,
    ),
    StageInfo(
        id="reply_1",
        content="The AI says:",
        prompt_name="reply_1",
        has_model_reply=True,
    ),
    StageInfo(
        id="question_2",
        content="Why do you feel that way?",
        model_content="Quiz page says: Why do you feel that way?",
        has_user_input=True,
    ),
    StageInfo(
        id="reply_2",
        content="The AI says:",
        prompt_name="reply_2",
        has_model_reply=True,
    ),
    StageInfo(
        id="summary",
        content="Thank you for your responses! Here is a summary of your answers.",
        prompt_name="summary",
        has_model_reply=True,
    ),
    StageInfo(
        id="end",
        content="Thank you for taking the quiz!",
    ),
]
