import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
# os.environ["HF_HOME"] = "G:\huggingface"
# os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
# os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"
# os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
# os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

from modelscope import AutoModelForCausalLM
import torch

model = AutoModelForCausalLM.from_pretrained(
    "qwen/Qwen-1_8B-Chat", trust_remote_code=True
)
model.to(0)
# model.to('cuda:0') 同样也可以
a = torch.tensor([1.0])
a = a.to(0)
# 注意！model.to操作不需要承接返回值，这是因为torch.nn.Module(模型基类)的这个操作是in-place(替换)的
# 而tensor的操作不是in-place的，需要承接返回值
