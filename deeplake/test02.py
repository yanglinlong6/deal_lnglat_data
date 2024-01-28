import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
os.environ[
    "ACTIVELOOP_TOKEN"
] = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTcwNjA4Mjc0NywiZXhwIjoxNzM4MzA5OTM0fQ.eyJpZCI6InlhbmdsaW5sb25nNiJ9.SNbGhqyihTBsiGhk6SOobDtvWwl0mxW-8YIokUGlvZdu2Z4-db4bnMWK_LIexTwZHHQeYmdHNlqE3gulUULTeg"

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake

embeddings = OpenAIEmbeddings()

db = DeepLake(
    # dataset_path=f"hub://yanglinlong6/my-code",
    dataset_path=f"hub://yanglinlong6/car-service-ordercenter",
    read_only=True,
    embedding_function=embeddings,
)
print("db", db)

# Dataset(
#     path="hub://yanglinlong6/langchain-code",
#     read_only=True,
#     tensors=["embedding", "ids", "metadata", "text"],
# )

retriever = db.as_retriever()
retriever.search_kwargs["distance_metric"] = "cos"
retriever.search_kwargs["fetch_k"] = 20
retriever.search_kwargs["maximal_marginal_relevance"] = True
retriever.search_kwargs["k"] = 20


def filter(x):
    # filter based on source code
    if "something" in x["text"].data()["value"]:
        return False

    # filter based on path e.g. extension
    metadata = x["metadata"].data()["value"]
    return "only_this" in metadata["source"] or "also_that" in metadata["source"]


### turn on below for custom filtering

# retriever.search_kwargs['filter'] = filter

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI(model_name="gpt-4")  # 'ada' 'gpt-3.5-turbo' 'gpt-4',
qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)

questions = [
    # "What is the class hierarchy?",
    # "简要总结一下这个项目"
    # "简要总结一下这个项目每个模块,总结文字尽量在100字以内"
    "简要说明一下CarOrderApiController这个类的作用,总结文字尽量在150字以内"
    # "What classes are derived from the Chain class?",
    # "What classes and functions in the ./langchain/utilities/ forlder are not covered by unit tests?",
    # "What one improvement do you propose in code in relation to the class herarchy for the Chain class?",
]

chat_history = [("项目", " 总结")]
for question in questions:
    result = qa({"question": question, "chat_history": chat_history})
    # result = qa({"question": question})
    chat_history.append((question, result["answer"]))
    print(f"-> \*\*Question\*\*: {question} ")
    print(f"\*\*Answer\*\*: {result['answer']} ")
