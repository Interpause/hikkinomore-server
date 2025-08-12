"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Keep It Going",
        content="User mentions something distinctive about themselves.",
        model_content="User mentions something distinctive about themselves.",
    ),
    StageInfo(
        id="question_1",
        content="Have you ever wondered what makes a follow-up question feel natural versus forced?",
    ),
    StageInfo(
        id="question_1.5",
        content="What is this value? How do you usually act on it?",
        model_content="Quiz page says: Think about what makes a follow-up question feel natural versus forced How do you normally follow up conversations?",
        has_user_input=True,
    ),
    StageInfo(
        id="reply_1",
        # content="The AI says:",
        prompt_name="reply_1",
        has_model_reply=True,
    ),
    StageInfo(
        id="question_2",
        content="If you were to ask Nervy a follow-up now, what would it be?",
        model_content="Quiz page says: If you were to ask Nervy a follow-up now, what would it be?",
        has_user_input=True,
    ),
    StageInfo(
        id="reply_2",
        # content="The AI says:",
        prompt_name="reply_2",
        has_model_reply=True,
    ),
    StageInfo(
        id="summary",
        # content="Thank you for your responses! Here is a summary of your answers.",
        prompt_name="summary",
        has_model_reply=True,
    ),
    StageInfo(
        id="lesson",
        # content="Thank you for taking the quiz!",
        prompt_name="lesson",
        has_model_reply=True,
    ),
]
