import timm
import torch

x = torch.randn(1, 3, 224, 224)
model = timm.create_model("mobilenetv3_large_100", pretrained=True)
features = model.forward_features(x)
print(features.shape)

timm.data.create_transform((3, 224, 224))
