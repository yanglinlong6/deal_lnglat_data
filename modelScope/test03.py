from ppdiffusers import StableDiffusionPipeline
import paddle

model_path = "sword_out"
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1", paddle_dtype=paddle.float32
)
# 注意：如果我们想从 HF Hub 加载权重，那么我们需要设置 from_hf_hub=True
pipe.unet.load_attn_procs(model_path, from_hf_hub=False)

prompt = "sword_1bug,sword,simple background,upward"
image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
image.save("sword.png")
