import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
# os.environ["HF_HOME"] = "G:\huggingface"
# os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
# os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"
# os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
# os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

from modelscope import AutoModelForSequenceClassification, AutoTokenizer
from swift import Trainer, LoRAConfig, Swift


model = AutoModelForSequenceClassification.from_pretrained(
    "AI-ModelScope/bert-base-uncased", revision="v1.0.0"
)
tokenizer = AutoTokenizer.from_pretrained(
    "AI-ModelScope/bert-base-uncased", revision="v1.0.0"
)
lora_config = LoRAConfig(target_modules=["query", "key", "value"])
model = Swift.from_pretrained(model, model_id="./outputs/checkpoint-21")

print(model(**tokenizer("this is a test", return_tensors="pt")))
