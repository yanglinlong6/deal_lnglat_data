# Install transformers from source - only needed for versions <= v4.34
# pip install git+https://github.com/huggingface/transformers.git
# pip install accelerate

import torch
from modelscope import snapshot_download
from transformers import pipeline

model_dir = snapshot_download("AI-ModelScope/TinyLlama-1.1B-Chat-v1.0")
pipe = pipeline(
    "text-generation", model=model_dir, torch_dtype=torch.bfloat16, device_map="auto"
)

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "我们能干啥？"},
]
prompt = pipe.tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
outputs = pipe(
    prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95
)
print(outputs[0]["generated_text"])
# <|system|>
# You are a friendly chatbot who always responds in the style of a pirate.</s>
# <|user|>
# How many helicopters can a human eat in one sitting?</s>
# <|assistant|>
# ...
