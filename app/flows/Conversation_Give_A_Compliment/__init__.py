"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Give a Compliment",
        content="User practices disagreeing with someone.",
        model_content="User practices disagreeing with someone.",
    ),
    StageInfo(
        id="question_1",
        content="Do compliments ever feel awkward to give or receive?",
    ),
    StageInfo(
        id="question_1.5",
        content="What's something you admire about a friend, but haven't told them yet?",
        model_content="Quiz page says: Think about whether compliments ever feel awkward to give or receive. What's something you admire about a friend, but haven't told them yet?",
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
        content="What's a compliment you'd like to give Nervy right now?",
        model_content="Quiz page says: What's a compliment you'd like to give Nervy right now?",
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
