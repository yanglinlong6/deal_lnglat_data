import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ[
    "SERPAPI_API_KEY"
] = "da8433eda3fc4629422e903b0b7eb9f642b1a5297a429b281ac7e1dc12c26042"

from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)
output = conversation.predict(input="Hi there!")
print(output)

output = conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
print(output)