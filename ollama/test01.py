# 设置Ollama的地址
ollama_host = "localhost"
# 设置Ollama的端口
ollama_port = 11434
# 设置Ollama的模型
ollama_model = "llama2"
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

if __name__ == "__main__":
    # 通过API的方式调用Ollama
    # StreamingStdOutCallbackHandler 使用流式输出结果
    llm = Ollama(
        base_url=f"http://{ollama_host}:{ollama_port}",
        model=ollama_model,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    )
    # 通过命令行的方式调用Ollama
    while True:
        query = input("\n\n Enter a query: ")
        llm(query)
