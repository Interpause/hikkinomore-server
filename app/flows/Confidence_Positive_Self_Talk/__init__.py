"""Hardcode the selected prompts here."""

from app.flows.structs import StageInfo

STAGES = [
    StageInfo(
        id="intro",
        title="Positive Self-Talk",
        content="User rephrases a self-critical thought as something to work on.",
        model_content="User rephrases a self-critical thought as something to work on.",
    ),
    StageInfo(
        id="question_1",
        content="Do you feel like when it comes to social blunders, you are especially hard on yourself?",
    ),
    StageInfo(
        id="question_1.5",
        content="What's something you're hard on yourself about?",
        model_content="Quiz page says: When it comes to social blunders, think about whether you are especially hard on yourself. What's something you're hard on yourself about?",
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
        content="How would a kind friend reframe that thought for you?",
        model_content="Quiz page says: How would a kind friend reframe that thought for you?",
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
        content="Now rephrase that critical self-thought into a kind one yourself!",
        model_content="Quiz page says: Now rephrase that critical self-thought into a kind one yourself!",
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
