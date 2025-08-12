"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Setting boundaries",
        content="User recognises something that causes anxiety and sets boundaries to stop it.",
        model_content="User recognises something that causes anxiety and sets boundaries to stop it.",
    ),
    StageInfo(
        id="question_1",
        content="Think about a time someone caused you to be anxious. ",
    ),
    StageInfo(
        id="question_1.5",
        content="In that scenario, did you voice out your discomfort to them?",
        model_content="Quiz page says: Think about a time when you felt anxious. In that scenario, did you voice out your discomfort to them?",
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
        content="How might you take action to stop this in the future?",
        model_content="Quiz page says: How might you take action to stop this in the future?",
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
