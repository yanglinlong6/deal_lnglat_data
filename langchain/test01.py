import langchain
import openai

# openai.api_base = "https://oneapi.365jpshop.com/v1"
from config import *
import os

# os.environ["OPENAI_API_KEY"] = "sk-hX6HRa25PqlfV9Tc19DeB5726e7c4f0c95C2F1023c6d7713"
os.environ[
    "OPENAI_API_KEY"
] = "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"  # 直连的key
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
import numpy as np
import time

llm = OpenAI(temperature=0.9, max_tokens=1000)
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
            "列举商城软件开发中2个关于" + inp + "的功能词汇，注意只输出2个功能词汇，用逗号隔开，注意不加序列号，不附带其他任何信息。必须是中文。"
        )
        response = llm(text)  # 似乎缺少OpenAI的详细调用信息，例如生成模型、令牌数量等
        print(response)
        return response


# 调用此函数时，需要同时传入nn作为参数
# tsc('黄帝内经', 10)


def tzh():
    text = "列举5个商城软件开发中的功能，注意只输出5个功能词汇，用英文逗号隔开，注意不加序列号，不附带其他任何信息。必须是中文。"
    response = llm(text)
    array = np.array(response.split(","))
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
        text = "详细解释一下，商城软件开发中" + a + "功能实现的业务逻辑，并生成php代码。中文回复。"
        llm = OpenAI(temperature=0.9, max_tokens=1000)
        response = llm(text, max_tokens=1000)
        #         time.sleep(5)
        response = a + "\n" + response
        print(response)
        global jiesh_array
        jiesh_array = np.append(jiesh_array, "\n\n" + response)
    # 将数组写入到一个文本文件中
    with open("d:/rgzhn_array.txt", "w") as f:
        for item in jiesh_array:
            f.write("%s\n" % item)
    return jiesh_array


jiesh()
# tzh()
