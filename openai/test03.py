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
# import mysql.connector
from datetime import datetime

import numpy as np
# from langchain.llms import OpenAI
from langchain_community.llms import OpenAIChat

# from langchain_community.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent, load_tools

# 创建数据库连接
# cnx = mysql.connector.connect(user='root',
#                               password='',
#                               host='localhost',  # 通常为 'localhost'
#                               database='wd')
# cursor = cnx.cursor()

model = "gpt-4-1106-preview"
llm = OpenAIChat(temperature=0.9, model_name=model)
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
        response = llm(text)  # 似乎缺少OpenAI的详细调用信息，例如生成模型、令牌数量等
        print(response)
        return response


# 调用此函数时，需要同时传入nn作为参数
# tsc('黄帝内经', 10)


def tzh():
    text = "列举20个机器学习算法中的学术词，注意只输出二十个学术词，用中文逗号隔开，不附带其他任何信息。必须只是中文。"
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
        text = "详细解释一下，什么是" + a + "。回复字数在200字左右，回复必须只是中文。"
        llm = OpenAIChat(temperature=0.9, model_name=model)
        response = llm(text)
        #         time.sleep(5)
        con = response
        response = a + "\n" + response
        # 插入数据库
        # 准备要插入的数据
        title = a
        content = con
        current_time = datetime.now()  # 获取当前时间
        # 执行插入操作
        insert_query = """
        INSERT INTO zhishi (title, content, time) VALUES (%s, %s, %s)
        """
        # cursor.execute(insert_query, (title, content, current_time))

        # 提交事务
        # cnx.commit()

        # 输出插入的行数
        # print(f"Inserted {cursor.rowcount} row.")

        print(response)
        global jiesh_array
        jiesh_array = np.append(jiesh_array, "\n\n" + response)
    # 将数组写入到一个文本文件中
    with open("d:/rgzhn_array.txt", "w") as f:
        for item in jiesh_array:
            f.write("%s\n" % item)
    # 关闭游标和连接
    # cursor.close()
    # cnx.close()
    return jiesh_array


jiesh()
# tzh()
