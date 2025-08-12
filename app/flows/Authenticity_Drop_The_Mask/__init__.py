"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Drop the Mask",
        content="User practices disagreeing with someone.",
        model_content="User practices disagreeing with someone.",
    ),
    StageInfo(
        id="question_1",
        content="Think of a time you disagreed with someone but chose to stay silent.",
    ),
    StageInfo(
        id="question_1.5",
        content="What stopped you from saying what you really thought?",
        model_content="Quiz page says: Think of a time you disagreed with someone but chose to stay silent. What stopped you from saying what you really thought?",
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
        content="If you could redo that moment, what might you say differently?",
        model_content="Quiz page says: If you could redo that moment, what might you say differently?",
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
