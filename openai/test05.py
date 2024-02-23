import langchain
import openai

openai.api_base = "https://oneapi.365jpshop.com/v1"
# from config import *
import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# os.environ["OPENAI_API_KEY"] = "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"#直连的key
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
import time

# model = "chatglm3"
# model = "gemini-pro"
from datetime import datetime

import numpy as np

# from langchain.llms import OpenAI
# from langchain_community.llms import OpenAIChat
from langchain_openai import ChatOpenAI

# from langchain_community.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

model = "gpt-4-1106-preview"
# llm = OpenAIChat(temperature=0.9, model_name=model)
llm = ChatOpenAI(
    temperature=0.9,
    model_name=model,
    api_key="sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102",
    base_url="https://oneapi.365jpshop.com/v1",
)

# client = OpenAIChat()
# llm = OpenAI(temperature=0.9,max_tokens=1000)
nn = 5
my_array = np.array([])
jiesh_array = np.array([])


# 这个函数需要一个额外的参数nn，因为在递归的环境中，
# 我们无法修改外部作用域的变量。
def tsc(inp: str, nn: int) -> str:

    # 这是基线条件，当nn等于0时，函数返回my_array
    if nn == 0:
        return my_array
    else:
        nn -= 1
        text = (
            "列举机器学习算法中10个关于"
            + inp
            + "的学术词，注意只输出十个学术词，用逗号隔开，不附带其他任何信息。必须只是中文。"
        )
        response = llm.invoke(
            input=text
        )  # 似乎缺少OpenAI的详细调用信息，例如生成模型、令牌数量等
        print(response.content)
        return response.content


def tzh():
    # text = "列举20个机器学习算法中的学术词，注意只输出二十个学术词，用中文逗号隔开，不附带其他任何信息。必须只是中文。"
    text = "列表一个商城项目的所有功能点,实现方案,用中文逗号隔开,附带主要技术实现方案，不附带其他任何信息。必须只是中文。"
    response = llm.invoke(input=text)
    array = np.array(response.content.split(","))
    print(array)
    for key in array:
        arr = tsc(key, 10)
        arr = np.array(arr.split(","))
        global my_array
        my_array = np.append(my_array, arr)
    return my_array


def jiesh():
    arr = tzh()
    #     arr = np.array(arr.split(','))
    for a in arr:
        text = "详细解释一下，什么是" + a + "。回复字数在50字左右，回复必须只是中文。"
        # llm = OpenAIChat(temperature=0.9, model_name=model)
        llm = ChatOpenAI(temperature=0.9, model_name=model)
        response = llm.invoke(input=text)
        response_content = a + "\n" + response.content
        print(response_content)
        global jiesh_array
        jiesh_array = np.append(jiesh_array, "\n\n" + response_content)
    # 将数组写入到一个文本文件中
    with open("rgzhn_array.txt", "w") as f:
        for item in jiesh_array:
            f.write("%s\n" % item)
    return jiesh_array


if __name__ == "__main__":
    # 调用此函数时，需要同时传入nn作为参数
    # tsc("黄帝内经", 10)
    # tzh()
    jiesh()
# end main
