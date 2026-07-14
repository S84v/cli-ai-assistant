import json


def handle_commands(user_input: str, messages: list, last_usage):

    role_labels = {"system": "System", "user": "User", "assistant": "Assistant"}
    seperator_roles = ["system", "assistant"]

    if user_input == "/logs":
        print("===============CONVERSATION HISTORY===============\n")
        for message in messages:
            role = message["role"]
            content = message["content"]
            print(role_labels[role], ": ", end="")
            print(content)
            if role in seperator_roles:
                print("\n" + "-" * 30 + "\n")

    if user_input == "/usage":
        if last_usage == None:
            print("No usage. Please start a conversation to track usage.")
        else:
            print("------------------------------")
            print("Prompt tokens: ", last_usage.prompt_tokens)
            print("Completion tokens: ", last_usage.completion_tokens)
            print("Total tokens: ", last_usage.total_tokens)
            print("------------------------------")
