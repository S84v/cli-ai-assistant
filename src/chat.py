from openai import OpenAI
import config


def get_response(client: OpenAI, messages: list, assistant_response: str):
    usage = None

    response = client.chat.completions.create(
        messages=messages,
        model=config.MODEL_FLASH,
        max_tokens=config.MAX_TOKENS,
        temperature=config.TEMPERATURE,
        stream=True,
        stream_options={"include_usage": True},
        extra_body={"thinking": {"type": "disabled"}},
    )

    for chunk in response:
        delta = chunk.choices[0].delta.content or ""
        assistant_response += delta
        print(delta, end="", flush=True)
        if chunk.usage:
            usage = chunk.usage
    print()

    return usage, assistant_response
