"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Take the lead!",
        content="User volunteers suggests a conversation topic with Nervy.",
        model_content="User volunteers suggests a conversation topic with Nervy.",
    ),
    StageInfo(
        id="question_1",
        content="Think about a time you suggested a topic in a group and it went well.",
    ),
    StageInfo(
        id="question_1.5",
        content="How did it go? Were you passionate about it?",
        model_content="Quiz page says: Think of a time when you suggested a topic in a group and it went well. How did it go? Were you passionate about it?",
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
        content="What helped you feel confident bringing it up?",
        model_content="Quiz page says: What helped you feel confident bringing it up?",
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
        content="Try starting a conversation about it now!",
        model_content="Quiz page says: Try starting a conversation about it now!",
        has_user_input=True,
    ),
    StageInfo(
        id="reply_3",
        # content="The AI says:",
        prompt_name="reply_3",
        has_model_reply=True,
    ),
    StageInfo(
        id="summary",
        title="Summary",
        prompt_name="summary",
        has_model_reply=True,
    ),
    StageInfo(
        id="lesson",
        title="Lesson",
        prompt_name="lesson",
        has_model_reply=True,
    ),
    StageInfo(
        id="end",
        content="This is the end of the quest. Now go and practice what you've learnt with your friends!",
    ),
]
