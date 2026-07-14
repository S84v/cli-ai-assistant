def add_user_message(messages, user_input):
    messages.append({"role": "user", "content": user_input})


def add_assistant_message(messages, response):
    messages.append({"role": "assistant", "content": response})
