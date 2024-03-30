from swift import ResTuningConfig

config = ResTuningConfig(
    dims=768,
    root_modules=r".*blocks.0$",
    stem_modules=r".*blocks\.\d+$",
    target_modules=r"norm",
    tuner_cfg="res_adapter",
)

from swift import Swift
import timm, torch

model = timm.create_model("vit_base_patch16_224", pretrained=False, num_classes=100)
model_tune = Swift.prepare_model(model, config)
print(model_tune.get_trainable_parameters())
print(model(torch.ones(1, 3, 224, 224)).shape)
