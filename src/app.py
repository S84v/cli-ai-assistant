import os
from dotenv import load_dotenv
from openai import OpenAI
import config

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key=api_key, base_url=config.BASE_URL)

response = client.chat.completions.create(
    model=config.MODEL_FLASH,
    messages=[
        {"role": "system", "content": config.SYSTEM_PROMPT},
        {"role": "user", "content": "hello"},
    ],
    max_tokens=config.MAX_TOKENS,
    temperature=config.TEMPERATURE,
    stream=True,
    extra_body={"thinking": {"type": "disabled"}},
)

for chunk in response:
    delta = chunk.choices[0].delta.content or ""
    print(delta, end = "", flush = True)
