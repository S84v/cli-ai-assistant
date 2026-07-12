import os
from dotenv import load_dotenv
from openai import OpenAI
import config

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

app = OpenAI(
    api_key=api_key,
    base_url = config.BASE_URL  
)