"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Recognise Progress",
        content="User reflects on or acknowledges their growth.",
        model_content="User reflects on or acknowledges their growth.",
    ),
    StageInfo(
        id="question_1",
        content="Think back to 2 months ago. Have you made any improvements since then?",
    ),
    StageInfo(
        id="question_1.5",
        content="Do you give yourself credit for small wins? Why or why not?",
        model_content="Quiz page says: Think about when you reflect on your progress. Do you give yourself credit for small wins? Why or why not?",
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
        content="What’s one moment of growth you want to celebrate right now?",
        model_content="Quiz page says: What’s one moment of growth you want to celebrate right now?",
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
