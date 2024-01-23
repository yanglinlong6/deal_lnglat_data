import os
import torch

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
os.environ["HF_HOME"] = "G:\huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"


os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

from transformers import PerceiverTokenizer, PerceiverForMaskedLM

# 创建一个名为 device 的设备对象，表示使用 CPU
device = torch.device("cpu")

# 创建一个名为 device 的设备对象，表示使用 GPU（如果可用）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = PerceiverTokenizer.from_pretrained("deepmind/language-perceiver")
model = PerceiverForMaskedLM.from_pretrained("deepmind/language-perceiver")

text = "This is an incomplete sentence where some words are missing."
# prepare input
encoding = tokenizer(text, padding="max_length", return_tensors="pt")
# mask " missing.". Note that the model performs much better if the masked span starts with a space.
encoding.input_ids[0, 52:61] = tokenizer.mask_token_id
inputs, input_mask = encoding.input_ids.to(device), encoding.attention_mask.to(device)

# forward pass
outputs = model(inputs=inputs, attention_mask=input_mask)
logits = outputs.logits
masked_tokens_predictions = logits[0, 51:61].argmax(dim=-1)
print(tokenizer.decode(masked_tokens_predictions))
# >>> should print " missing."
