"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Start the talk",
        content="User mentions something distinctive about themselves.",
        model_content="User mentions something distinctive about themselves.",
    ),
    StageInfo(
        id="question_1",
        content="When was the last time you initiated a conversation with someone new?",
    ),
    StageInfo(
        id="question_1.5",
        content="Tell me more about it!",
        model_content="Quiz page says: When was the last time you initiated a conversation with someone new? Tell me more about it!",
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
        content="What was the hardest part about starting that conversation?",
        model_content="Quiz page says: What was the hardest part about starting that conversation?",
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
