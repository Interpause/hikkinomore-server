from google.genai import Client

from app.config import CONFIG

client = Client(api_key=CONFIG.gemini_api_key)
