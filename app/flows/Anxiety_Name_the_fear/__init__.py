"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Name the Fear",
        content="User mentions a social worry or fear.",
        model_content="User mentions a social worry or fear.",
    ),
    StageInfo(
        id="question_1",
        content="Do you have any social fears?",
    ),
    StageInfo(
        id="question_1.5",
        content="What social situation makes you feel tense, awkward, or anxious?",
        model_content="Quiz page says: Think about a time when you felt anxious. What social situation makes you feel tense, awkward, or anxious?",
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
        content="What’s something small you can try next time to face that fear a little differently?",
        model_content="Quiz page says: What’s something small you can try next time to face that fear a little differently?",
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
