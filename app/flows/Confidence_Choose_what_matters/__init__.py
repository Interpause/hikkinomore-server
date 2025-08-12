"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Choose What Matters",
        content="User makes a decision that aligns with their values, even if it’s hard.",
        model_content="User makes a decision that aligns with their values, even if it’s hard.",
    ),
    StageInfo(
        id="question_1",
        content="Think about a time you chose not to people-please",
    ),
    StageInfo(
        id="question_1.5",
        content="In that scenario, what helped you stick with your decision?",
        model_content="Quiz page says: Think about when you chose not to people-please. In that scenario, what helped you stick with your decision?",
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
        content="Was there any guilt or doubt afterwards? Why?",
        model_content="Quiz page says: Was there any guilt or doubt afterwards? Why?",
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
