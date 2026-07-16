import sys
import config
import os


def handle_commands(user_input: str, messages: list, last_usage):

    if user_input == "/exit":
        print("Thank you for using CLI Assistant. Exiting...")
        sys.exit(0)

    elif user_input == "/logs":
        role_labels = {"system": "System", "user": "User", "assistant": "Assistant"}
        seperator_roles = ["system", "assistant"]

        print("===============CONVERSATION HISTORY===============\n")

        for message in messages:
            role = message["role"]
            content = message["content"]
            print(role_labels[role], ": ", end="")
            print(content)
            if role in seperator_roles:
                print("\n" + "-" * 30 + "\n")

    elif user_input == "/usage":
        if last_usage == None:
            print("No tokens used yet. Please start a conversation to track usage.")
        else:
            print("------------------------------")
            print("Prompt tokens: ", last_usage.prompt_tokens)
            print("Completion tokens: ", last_usage.completion_tokens)
            print("Total tokens: ", last_usage.total_tokens)
            print("------------------------------")

    elif user_input == "/clear":
        os.system("cls")
        print("Conversation cleared. Please start a new chat below:")

        return [
            {"role": "system", "content": config.SYSTEM_PROMPT},
        ]

    elif user_input == "/help":
        print("==================== LLM CLI GUIDE ====================")
        print()
        print("Type any programming question and press Enter.")
        print("General Commands")
        print("----------------")
        print("/help        Show this help menu")
        print("/exit        Exit the application")
        print("/clear       Start a new conversation")
        print("/logs        Show conversation history")
        print("/usage       Show token usage for the last request")
        print()
        print("Conversation")
        print("------------")
        print("• The assistant remembers previous messages until /clear is used.")
        print("• Conversation history is sent with each request.")
        print()
        print("Tips")
        print("----")
        print("• Ask debugging questions.")
        print("• Request code generation.")
        print("• Ask for explanations of programming concepts.")
        print("• Paste error messages for help.")
        print("• Ask for code reviews or optimizations.")
        print()
        print("Examples")
        print("--------")
        print("> Explain Python decorators")
        print("> Why is my SQL query slow?")
        print("> Write a binary search in C++")
        print("> Debug this traceback")
        print("> Optimize this function")
        print("=======================================================")
    else:
        print("Command not recognized. Please refer to the guide by typing /help.")
    return messages
