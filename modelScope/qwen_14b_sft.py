import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
os.environ["HF_HOME"] = "G:\huggingface"
os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"


os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

os.environ["CUDA_VISIBLE_DEVICES"] = "4,5,6,7"

from swift.llm import DatasetName, ModelType, SftArguments, sft_main

sft_args = SftArguments(
    model_type=ModelType.qwen_14b_chat,
    # model_cache_dir="Qwen-14B-Chat",
    dataset=[DatasetName.alpaca_zh, DatasetName.alpaca_en],
    train_dataset_sample=500,
    eval_steps=50,
    batch_size=16,
    logging_steps=20,
    num_train_epochs=40,
    learning_rate=1e-4,
    save_total_limit=3,
    output_dir="output",
    lora_target_modules="ALL",
    self_cognition_sample=500,
    model_name=["小黄", "Xiao Huang"],
    model_author=["魔搭", "ModelScope"],
)
output = sft_main(sft_args)
best_model_checkpoint = output["best_model_checkpoint"]
print(f"best_model_checkpoint: {best_model_checkpoint}")
