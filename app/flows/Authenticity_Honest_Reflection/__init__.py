"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Honest reflection",
        content="User shares a genuine feeling or thought, despite discomfort.",
        model_content="User shares a genuine feeling or thought, despite discomfort.",
    ),
    StageInfo(
        id="question_1",
        content="Think of a recent moment where you felt something strongly, but didn't say it out loud.",
    ),
    StageInfo(
        id="question_1.5",
        content="What did you want to say?",
        model_content="Quiz page says: Think of a recent moment where you felt something strongly, but didn't say it out loud. What did you want to say?",
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
        content="If you had said it out loud, how do you think it would have gone?",
        model_content="Quiz page says: If you had said it out loud, how do you think it would have gone?",
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
