from typing import Dict, Optional

from pydantic import BaseModel


class StageInfo(BaseModel):
    """Model for stage information.

    If has_model_reply is True, specifying prompt_name is required, and specifying
    model_content is good to do.

    Attributes:
        id: Unique identifier for the stage.
        title: Optional card title to show on frontend.
        content: Optional card content to show on frontend.
        model_content: What the model "thinks" it said, if None, will fallback to content.
        prompt_name: Filename (without .md suffix) of the system prompt to use for this stage.
        has_user_input: Whether this stage requires user input.
        has_model_reply: Whether this stage has a model reply.
    """

    id: str
    title: Optional[str] = None
    content: Optional[str] = None
    model_content: Optional[str] = None
    prompt_name: Optional[str] = None
    has_user_input: bool = False
    has_model_reply: bool = False


class QuizRequest(BaseModel):
    """Model for quiz request.

    Attributes:
        stage_id: The id of the current stage shown on frontend.
        user_inputs: A dictionary of stage id to user inputs across all stages.
        model_replies: A dictionary of stage id to model replies across all stages.
    """

    stage_id: Optional[str] = None
    user_inputs: Dict[str, str] = {}
    model_replies: Dict[str, str] = {}


class QuizResponse(BaseModel):
    """Response model for quiz.

    Attributes:
        stages: A dictionary of stage id to StageInfo for all stages.
        next_stage: The id of the next stage to show on frontend, if None, no next stage.
        user_inputs: A dictionary of stage id to user inputs across all stages.
        model_replies: A dictionary of stage id to model replies across all stages.
    """

    stages: Dict[str, StageInfo]
    next_stage: Optional[str] = None
    user_inputs: Dict[str, str] = {}
    model_replies: Dict[str, str] = {}
