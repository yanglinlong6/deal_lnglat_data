from modelscope import Model
from swift import Swift, LoRAConfig
import torch

model = Model.from_pretrained(
    "ZhipuAI/chatglm2-6b", torch_dtype=torch.bfloat16, device_map="auto"
)
lora_config = LoRAConfig(
    r=16, target_modules=["query_key_value"], lora_alpha=32, lora_dropout=0.0
)
model = Swift.prepare_model(model, lora_config)
# use model to do other things
print(model)
