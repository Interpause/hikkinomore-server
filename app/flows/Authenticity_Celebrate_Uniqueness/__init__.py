"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Celebrate Uniqueness",
        content="User mentions something distinctive about themselves.",
        model_content="User mentions something distinctive about themselves.",
    ),
    StageInfo(
        id="question_1",
        content="Is there something about you that makes you different from most people you know?",
    ),
    StageInfo(
        id="question_1.5",
        content="What is this trait? How do you feel about it?",
        model_content="Quiz page says: Choose something about you that makes you different from most people you know. What is this trait? How do you feel about it?",
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
        content="Do you hide this trait sometimes, or do you embrace it fully? Why?",
        model_content="Quiz page says: Do you hide this trait sometimes, or do you embrace it fully? Why?",
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
        title="Summary",
        prompt_name="summary",
        has_model_reply=True,
    ),
    StageInfo(
        id="lesson",
        title="Lesson",
        prompt_name="lesson",
        has_model_reply=True,
    ),
    StageInfo(
        id="end",
        content="This is the end of the quest. Now go and practice what you've learnt with your friends!",
    ),
]
