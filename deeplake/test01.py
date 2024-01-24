import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
os.environ[
    "ACTIVELOOP_TOKEN"
] = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTcwNjA4Mjc0NywiZXhwIjoxNzM4MzA5OTM0fQ.eyJpZCI6InlhbmdsaW5sb25nNiJ9.SNbGhqyihTBsiGhk6SOobDtvWwl0mxW-8YIokUGlvZdu2Z4-db4bnMWK_LIexTwZHHQeYmdHNlqE3gulUULTeg"

# Please manually enter OpenAI Key

from langchain.document_loaders import TextLoader

# root_dir = "../"
root_dir = "H:\\WorkSpaces\\temp\\develop\\car-service-ordercenter"

docs = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    print("filenames", filenames)
    for file in filenames:
        # if file.endswith(".py") and "/.venv/" not in dirpath:
        if (
            file.endswith(".java")
            or file.endswith(".xml")
            or file.endswith(".properties")
            and "/.venv/" not in dirpath
            and "/target/" not in dirpath
            and "/test/" not in dirpath
        ):
            try:
                loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
                docs.extend(loader.load_and_split())
            except Exception as e:
                pass

print(f"{len(docs)}")

from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

print(f"{len(texts)}")

from langchain.embeddings.openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

from langchain.vectorstores import DeepLake

db = DeepLake.from_documents(
    # texts, embeddings, dataset_path=f"hub://yanglinlong6/my-code"
    texts,
    embeddings,
    dataset_path=f"hub://yanglinlong6/car-service-ordercenter",
)

print(db)
