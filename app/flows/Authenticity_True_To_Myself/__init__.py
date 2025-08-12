"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="True to Myself!",
        content="User expresses a personal value that may be different from others.",
        model_content="User expresses a personal value that may be different from others.",
    ),
    StageInfo(
        id="question_1",
        content="Is there one belief or value you hold strongly, even if others might not agree with it?",
    ),
    StageInfo(
        id="question_1.5",
        content="What is this value? How do you usually act on it?",
        model_content="Quiz page says: Think about one belief or value you hold strongly, even if others might not agree with it. What is this value? How do you usually act on it?",
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
        content="Have you ever felt judged for this belief? Tell me more!",
        model_content="Quiz page says: Have you ever felt judged for this belief? Tell me more!",
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
