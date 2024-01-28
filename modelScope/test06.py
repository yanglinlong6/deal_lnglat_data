import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
# os.environ["HF_HOME"] = "G:\huggingface"
# os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
# os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"


# os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
# os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from modelscope import AutoModelForSequenceClassification, AutoTokenizer, MsDataset
from transformers import default_data_collator

from swift import Trainer, LoRAConfig, Swift, TrainingArguments


model = AutoModelForSequenceClassification.from_pretrained(
    "AI-ModelScope/bert-base-uncased", revision="v1.0.0"
)
tokenizer = AutoTokenizer.from_pretrained(
    "AI-ModelScope/bert-base-uncased", revision="v1.0.0"
)
lora_config = LoRAConfig(target_modules=["query", "key", "value"])
model = Swift.prepare_model(model, config=lora_config)

train_dataset = (
    MsDataset.load("clue", subset_name="afqmc", split="train")
    .to_hf_dataset()
    .select(range(100))
)
val_dataset = (
    MsDataset.load("clue", subset_name="afqmc", split="validation")
    .to_hf_dataset()
    .select(range(100))
)


def tokenize_function(examples):
    return tokenizer(
        examples["sentence1"],
        examples["sentence2"],
        padding="max_length",
        truncation=True,
        max_length=128,
    )


train_dataset = train_dataset.map(tokenize_function)
val_dataset = val_dataset.map(tokenize_function)

arguments = TrainingArguments(
    output_dir="./outputs",
    per_device_train_batch_size=16,
)

trainer = Trainer(
    model,
    arguments,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    data_collator=default_data_collator,
)

trainer.train()
