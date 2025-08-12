"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Brave the Awkward",
        content="User shares a genuine feeling or thought, despite discomfort.",
        model_content="UUser shares a genuine feeling or thought, despite discomfort.",
    ),
    StageInfo(
        id="question_1",
        content="Think of a recent moment where you or someone else was really awkward.",
    ),
    StageInfo(
        id="question_1.5",
        content="Why do you think awkward moments happen in chats?",
        model_content="Quiz page says: Think of a recent moment where you or someone else was really awkward. Why do you think awkward moments happen in chats?",
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
        content="How do you usually respond when things get tense or weird?",
        model_content="Quiz page says: How do you usually respond when things get tense or weird?",
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
