from swift import PeftModel, PeftConfig
from modelscope.models.nlp import SbertForSequenceClassification
from modelscope.models.nlp.structbert import SbertConfig

from swift import LoraConfig, Swift

model = SbertForSequenceClassification(SbertConfig())
lora_config = LoraConfig(target_modules=["query", "key", "value"])
model = Swift.prepare_model(model, lora_config)
print(model)
