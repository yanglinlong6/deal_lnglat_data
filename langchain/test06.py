import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ[
    "SERPAPI_API_KEY"
] = "da8433eda3fc4629422e903b0b7eb9f642b1a5297a429b281ac7e1dc12c26042"

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(temperature=0)
# print(
#     chat(
#         [
#             HumanMessage(
#                 content="Translate this sentence from English to French. I love programming."
#             )
#         ]
#     )
# )
# -> AIMessage(content="J'aime programmer.", additional_kwargs={})

messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    ),
]
# result = chat(messages)
# print(result)

batch_messages = [
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to French."
        ),
        HumanMessage(
            content="Translate this sentence from English to French. I love programming."
        ),
    ],
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to French."
        ),
        HumanMessage(
            content="Translate this sentence from English to French. I love artificial intelligence."
        ),
    ],
]
result = chat.generate(batch_messages)

print(result.llm_output['token_usage'])
# -> LLMResult(generations=[[ChatGeneration(text="J'aime programmer.", generation_info=None, message=AIMessage(content="J'aime programmer.", additional_kwargs={}))], [ChatGeneration(text="J'aime l'intelligence artificielle.", generation_info=None, message=AIMessage(content="J'aime l'intelligence artificielle.", additional_kwargs={}))]], llm_output={'token_usage': {'prompt_tokens': 71, 'completion_tokens': 18, 'total_tokens': 89}})
