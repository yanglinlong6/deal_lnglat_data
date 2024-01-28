import os

import torch

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# os.environ["HF_DATASETS_CACHE"] = "G:\huggingface"
# os.environ["HF_HOME"] = "G:\huggingface"
# os.environ["HUGGINGFACE_HUB_CACHE"] = "G:\huggingface"
# os.environ["TRANSFORMERS_CACHE"] = "G:\huggingface"


# os.environ["MODELSCOPE_CACHE"] = "G:\modelscope"
# os.environ["MODELSCOPE_MODULES_CACHE"] = "G:\modelscope"

from modelscope.models.nlp import SbertForSequenceClassification
from modelscope.models.nlp.structbert import SbertConfig

from swift import LoraConfig, Swift

model = SbertForSequenceClassification(SbertConfig())
lora_config = LoraConfig(target_modules=["query", "key", "value"])
model = Swift.prepare_model(model, lora_config)
