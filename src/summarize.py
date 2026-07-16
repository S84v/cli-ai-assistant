from openai import OpenAI
import config
import json

def summarize_conversation(client, messages):
    previous_summary = None
    conversation_start = 1

    if (len(messages)>1 and messages[1]["role"] == "system" and messages[1]["content"].startswith("Conversation summary:")):
        previous_summary = messages[1]["content"]
        conversation_start = 2
    older_messages = messages[conversation_start:-config.SUMMARY_MESSAGES_TO_KEEP]
    recent_messages = messages[-config.SUMMARY_MESSAGES_TO_KEEP:]

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": config.SUMMARY_PROMPT
            },
            {
                "role": "user",
                "content": json.dumps(older_messages)
            }
        ],
        model=config.MODEL_FLASH,
        max_tokens=config.SUMMARY_MAX_TOKENS,
        temperature=config.TEMPERATURE,
        stream=False,
        extra_body={"thinking": {"type": "disabled"}},
    )

    summary = response.choices[0].message.content

    return summary, recent_messages
