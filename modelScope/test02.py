import timm

model = timm.create_model("hf_hub:notmahi/dobb-e", pretrained=True)

model.eval()