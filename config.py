import os
from dotenv import load_dotenv

# environment variables are loaded
load_dotenv()

API_KEY = os.getenv('OPENROUTER_API_KEY')
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-2.0-flash-exp:free"