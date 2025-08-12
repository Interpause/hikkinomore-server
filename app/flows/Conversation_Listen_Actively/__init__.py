"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Listen Actively",
        content="User expresses a personal value that may be different from others.",
        model_content="User expresses a personal value that may be different from others.",
    ),
    StageInfo(
        id="question_1",
        content="Think about a time you felt really heard.",
    ),
    StageInfo(
        id="question_1.5",
        content="What did that person do?",
        model_content="Quiz page says: Think about a time you felt really heard. What did that person do?",
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
        content="When you're in a convo, how do you show someone you're paying attention?",
        model_content="Quiz page says: When you're in a convo, how do you show someone you're paying attention?",
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
