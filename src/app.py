import os
from dotenv import load_dotenv
from openai import OpenAI
import config

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if api_key is None:
    exit("DeepSeek API key not found.")

client = OpenAI(api_key=api_key, base_url=config.BASE_URL)

messages = [
    {"role": "system", "content": config.SYSTEM_PROMPT},
]

print("Hello. Welcome to CLI Programming Assistant. Write your query below:")

while True:
    assistant_response = ""
    user_input = input("\n> ")

    if user_input == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=config.MODEL_FLASH,
        messages=messages,
        max_tokens=config.MAX_TOKENS,
        temperature=config.TEMPERATURE,
        stream=True,
        extra_body={"thinking": {"type": "disabled"}},
    )

    for chunk in response:
        delta = chunk.choices[0].delta.content or ""
        assistant_response += delta
        print(delta, end="", flush=True)

    messages.append({"role": "assistant", "content": assistant_response})

    print(messages)
