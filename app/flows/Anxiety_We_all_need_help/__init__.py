"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="You’re Already a Winner",
        content="User notices or resists comparison to others.",
        model_content="User notices or resists comparison to others.",
    ),
    StageInfo(
        id="question_1",
        content="Do you often find yourself comparing yourself to others?",
    ),
    StageInfo(
        id="question_1.5",
        content="What did those comparisons make you feel or believe about yourself?",
        model_content="Quiz page says: Think about when you found yourself comparing to others. What did those comparisons make you feel or believe about yourself?",
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
        content="What can you do to remind yourself that you’re not falling behind?",
        model_content="Quiz page says: What can you do to remind yourself that you’re not falling behind?",
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
    StageInfo(
        id="end",
        content="This is the end of the quest. Now go and practice what you've learnt with your friends!",
    ),
]
