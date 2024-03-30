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
