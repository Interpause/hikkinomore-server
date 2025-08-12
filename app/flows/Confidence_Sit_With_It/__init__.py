"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Sit with it",
        content="User notices a tough feeling (like jealousy, fear, or shame) and explores it instead of pushing it away.",
        model_content="User notices a tough feeling (like jealousy, fear, or shame) and explores it instead of pushing it away.",
    ),
    StageInfo(
        id="question_1",
        content="Do you normally avoid tough feelings?",
    ),
    StageInfo(
        id="question_1.5",
        content="What's a feeling you usually try to avoid?",
        model_content="Quiz page says: Think about when you normally avoid tough feelings. What's a feeling you usually try to avoid?",
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
        content="What might happen if you sat with that feeling a bit longer next time?",
        model_content="Quiz page says: What might happen if you sat with that feeling a bit longer next time?",
        has_user_input=True,
    ),
    StageInfo(
        id="reply_2",
        # content="The AI says:",
        prompt_name="reply_2",
        has_model_reply=True,
    ),
    StageInfo(
        id="question_3",
        content="What's one way you could listen better this week?",
        model_content="Quiz page says: What's one way you could listen better this week?",
        has_user_input=True,
    ),
    StageInfo(
        id="reply_3",
        # content="The AI says:",
        prompt_name="reply_3",
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
