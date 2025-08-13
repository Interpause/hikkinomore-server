"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Own your story!",
        content="User talks about a real, personal experience without filtering.",
        model_content="User talks about a real, personal experience without filtering.",
    ),
    StageInfo(
        id="question_1",
        content="Can you think of a time when you really wanted to tell a story, but did not have the chance?",
    ),
    StageInfo(
        id="question_1.5",
        content="How did that make you feel?",
        model_content="Quiz page says: Think of a time when you really wanted to tell a story, but did not have the chance. How did that make you feel?",
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
        content="Tell the story you wanted to tell at that time",
        model_content="Quiz page says: What was the story you wanted to tell at that time?",
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
        content="Talk about what stopped you from telling that story ",
        model_content="Quiz page says: What stopped you from telling that story?",
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
