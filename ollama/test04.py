import os

from groq import Groq

client = Groq(
    # api_key=os.environ.get("GROQ_API_KEY"),
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)