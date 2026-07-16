import os
from dotenv import load_dotenv
from openai import OpenAI
import config
import json
from chat import get_response
from handle_commands import handle_commands
from utils import add_user_message, add_assistant_message

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if api_key is None:
    exit("DeepSeek API key not found.")

client = OpenAI(api_key=api_key, base_url=config.BASE_URL)


print(r"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\
┃                                                                                               ┃\
┃ / ###### / ##       /######        /######   /######   /######  /######  /######  /########   ┃\
┃ /##__  ##| ##      |_  ##_/       /##__  ## /##__  ## /##__  ##|_  ##_/ /##__  ##|__  ##__/   ┃\
┃| ##  \__/| ##        | ##        | ##  \ ##| ##  \__/| ##  \__/  | ##  | ##  \__/   | ##      ┃\
┃| ##      | ##        | ##        | ########|  ###### |  ######   | ##  |  ######    | ##      ┃\
┃| ##      | ##        | ##        | ##__  ## \____  ## \____  ##  | ##   \____  ##   | ##      ┃\
┃| ##    ##| ##        | ##        | ##  | ## /##  \ ## /##  \ ##  | ##   /##  \ ##   | ##      ┃\
┃|  ######/| ######## /######      | ##  | ##|  ######/|  ######/ /######|  ######/   | ##      ┃\
┃ \______/ |________/|______/      |__/  |__/ \______/  \______/ |______/ \______/    |__/      ┃\
┃                                                                                               ┃\
┃                                                                                               ┃\
┃              CLI PROGRAMMING ASSISTANT                                                        ┃\
┃                                                                                               ┃\
┃      • DeepSeek API                                                                           ┃\
┃      • Streaming Enabled                                                                      ┃\
┃      • Token Tracking                                                                         ┃\
┃      • Conversation Memory                                                                    ┃\
┃                                                                                               ┃\
┃      Type /help for available commands                                                        ┃\
┃                                                                                               ┃\
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

print("\nWelcome to the CLI Programming Assistant. Get started by writing your query below:")


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


if __name__ == "__main__":
    chat()
