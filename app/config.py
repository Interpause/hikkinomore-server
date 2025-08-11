from pydantic_settings import BaseSettings


# See: https://docs.pydantic.dev/latest/concepts/pydantic_settings
class Config(BaseSettings, env_file=".env"):
    """App configuration.

    Attributes:
        gemini_api_key (str): API key for Gemini.
    """

    gemini_api_key: str
