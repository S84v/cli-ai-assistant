import os
from dotenv import load_dotenv
from openai import OpenAI
import config
import json
from chat import get_response
from handle_commands import handle_commands
from utils import add_user_message, add_assistant_message
from summarize import summarize_conversation

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if api_key is None:
    exit("DeepSeek API key not found.")

client = OpenAI(api_key=api_key, base_url=config.BASE_URL)


print(r"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\
┃                                                                                               ┃\
┃                 /##       /##       /##      /##        /######  /##       /######            ┃\
┃               | ##      | ##      | ###    /###       /##__  ##| ##      |_  ##_/             ┃\
┃               | ##      | ##      | ####  /####      | ##  \__/| ##        | ##               ┃\
┃               | ##      | ##      | ## ##/## ##      | ##      | ##        | ##               ┃\
┃               | ##      | ##      | ##  ###| ##      | ##      | ##        | ##               ┃\
┃               | ##      | ##      | ##\  # | ##      | ##    ##| ##        | ##               ┃\
┃               | ########| ########| ## \/  | ##      |  ######/| ######## /######             ┃\
┃               |________/|________/|__/     |__/       \______/ |________/|______/             ┃\
┃                                                                                               ┃\
┃                                                                                               ┃\
┃                                                                                               ┃\
┃                                CLI PROGRAMMING ASSISTANT                                      ┃\
┃                                                                                               ┃\
┃      • Powered by OpenAI API                                                                  ┃\
┃      • Streaming Responses Enabled                                                            ┃\
┃      • Token Usage Tracking                                                                   ┃\
┃      • Conversation Memory                                                                    ┃\
┃      • Automatic Context Compression                                                          ┃\
┃                                                                                               ┃\
┃      Type /help for available commands                                                        ┃\
┃                                                                                               ┃\
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"
)

print(
    "\nWelcome to LLM CLI, a CLI programming assistant. Get started by writing your query below:"
)


def chat():
    last_usage = None
    messages = [
        {"role": "system", "content": config.SYSTEM_PROMPT},
    ]
    while True:
        assistant_response = ""
        user_input = input("\n> ")
        print("")

        if user_input.startswith("/"):
            messages = handle_commands(user_input, messages, last_usage)
            continue

        add_user_message(messages, user_input)

        usage, assistant_response = get_response(client, messages, assistant_response)
        last_usage = usage

        add_assistant_message(messages, assistant_response)

        if usage.prompt_tokens > config.SUMMARY_THRESHOLD_TOKENS:
            print("\nSUMMARY THRESHOLD REACHED. SUMMARIZING THE CONVERSATION...")
            summary, recent_messages = summarize_conversation(client, messages)
            messages = [
                {"role": "system", "content": config.SYSTEM_PROMPT},
                {"role": "system", "content": f"Conversation summary:\n{summary}"},
            ]
            messages.extend(recent_messages)


if __name__ == "__main__":
    chat()
