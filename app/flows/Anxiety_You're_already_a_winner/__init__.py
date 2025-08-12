"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="We All Need Help",
        content="User explicitly asks the bot for help or comfort.",
        model_content="User explicitly asks the bot for help or comfort.",
    ),
    StageInfo(
        id="question_1",
        content="Think about a time when you felt overwhelmed.",
    ),
    StageInfo(
        id="question_1.5",
        content="What stopped you from asking for help right away?",
        model_content="Quiz page says: Think about a time when you felt overwhelmed. What stopped you from asking for help right away?",
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
        content="How did it feel once you did reach out (or imagine if you had)?",
        model_content="Quiz page says: How did it feel once you did reach out (or imagine if you had)?",
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
        content="What's something that makes your journey different, but still valuable?",
        model_content="Quiz page says: What's something that makes your journey different, but still valuable?",
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
