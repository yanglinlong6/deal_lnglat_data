from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key="2544ea141595d420ca10f891833096ac.deW5ICKFVh4JivTN"
)  # 请填写您自己的APIKey

response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "user", "content": "你好！你叫什么名字"},
    ],
    tools=[
        {
            "type": "retrieval",
            "retrieval": '''
                "knowledge_id": "your knowledge id",
                "prompt_template":"从文档"
                """
                {{knowledge}}
                """
                中找问题
                """
                {{question}}
                """
                的答案，找到答案就仅使用文档语句回答问题，找不到答案就用自身知识回答并且告诉用户该信息不是来自文档。

                不要复述问题，直接开始回答。"
            ''',
        }
    ],
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta)
