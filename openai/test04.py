from langchain_openai import ChatOpenAI

# Create a new ChatOpenAI object with your OpenAI API key
chat = ChatOpenAI(
    temperature=0.9,
    model_name="gpt-4-1106-preview",
    api_key="sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102",
    base_url="https://oneapi.365jpshop.com/v1",
)

# Use the chat object to generate a response to a prompt
response = chat.invoke(input="帮我生成2条续保营销文案，每条不超过12个字，输出json格式")
print(response)
