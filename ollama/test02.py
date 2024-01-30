# 设置Ollama的地址
ollama_host = "localhost"
# 设置Ollama的端口
ollama_port = 11434
# 设置Ollama的模型
ollama_model = "llama2"

from langchain.document_loaders import OnlinePDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import GPT4AllEmbeddings
from langchain import PromptTemplate
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
import sys
import os


class SuppressStdout:
    # __enter__ 最先开始的时候会执行一次
    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, "w")
        sys.stderr = open(os.devnull, "w")

    # __exit__ 最后执行一次
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr


# 加载在线pdf并将其分成块
loader = OnlinePDFLoader(
    "https://d18rn0p25nwr6d.cloudfront.net/CIK-0001813756/975b3e9b-268e-4798-a9e4-2a9a7c92dc10.pdf"
)
data = loader.load()
# RecursiveCharacterTextSplitter是一个基于递归的字符级别的分词器。它可以将文本逐个字符地拆分，并且可以递归地处理包含其他词汇的字符，例如中文中的词语或日语中的汉字。
from langchain.text_splitter import RecursiveCharacterTextSplitter

# chunk_size 设置为分割块的大小
# chunk_overlap 设置每个分割块之间重叠的字符数。
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
# 使用Chroma数据库进行存储所有的分片，使用的分片方式是GPT4ALL
with SuppressStdout():
    vectorstore = Chroma.from_documents(
        documents=all_splits, embedding=GPT4AllEmbeddings()
    )
while True:
    query = input("\nQuery: ")
    # 退出设置
    if query == "exit":
        break
    # 收到空字符串将进行跳过
    if query.strip() == "":
        continue
    # Prompt 设置回答的规则模版
    template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer. 
    Use three sentences maximum and keep the answer as concise as possible. 
    {context}
    Question: {question}
    Helpful Answer:"""
    # 通过Prompt模版生成完整语句
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )
    # 开始调用
    llm = Ollama(
        model="llama2",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
    # llm = Ollama(model="llama2:13b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    # 通过设置大语言模型、向量存储和prompt创建一个QA链进行回答
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )
    result = qa_chain({"query": query})
    print(result)
