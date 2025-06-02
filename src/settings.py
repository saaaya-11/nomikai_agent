import os 
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

# Gemini
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
GOOGLE_ENDPOINT_OPENAI = "https://generativelanguage.googleapis.com/v1beta/openai/"

# OpenAI
OpenAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Hotpepper (Ref: https://webservice.recruit.co.jp/doc/hotpepper/reference.html)
RECRUIT_API_KEY = os.environ.get("RECRUIT_API_KEY")