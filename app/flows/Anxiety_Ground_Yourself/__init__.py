"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Ground Yourself",
        content="User uses a sensory or physical check-in to calm down.",
        model_content="User uses a sensory or physical check-in to calm down.",
    ),
    StageInfo(
        id="question_1",
        content="Do you ever feel anxious when socialising?",
    ),
    StageInfo(
        id="question_1.5",
        content="When feeling anxious, how did you react?",
        model_content="Quiz page says: Think about when you felt anxious. How did you react?",
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
        content="What did you do today to ground yourself or calm down?",
        model_content="Quiz page says: What did you do today to ground yourself or calm down?",
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
