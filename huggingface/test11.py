import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
os.environ["HF_HOME"] = "G:\huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"
os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

# from transformers import AutoTokenizer, AutoModel

# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True)
# model = (
#     AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).half().cuda()
# )
# model = model.eval()
# response, history = model.chat(tokenizer, "你好", history=[])
# print(response)
# response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
# print(response)

from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = (
    AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
)
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
# 👋!我是人工智能助手 ChatGLM-6B,很高兴见到你,欢迎问我任何问题。
response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
print(response)
