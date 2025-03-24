# app/generator.py
from diffusers import StableDiffusionPipeline
import torch
import uuid
from datetime import datetime
from pathlib import Path

# 모델 초기화 (앱 시작 시 1회)
pipe = StableDiffusionPipeline.from_pretrained(
  "runwayml/stable-diffusion-v1-5",
  torch_dtype=torch.float32
).to("cpu")

def generate_image(prompt: str) -> str:
  image = pipe(prompt).images[0]
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  output_path = Path("img") / f"{timestamp}.png"
  output_path.parent.mkdir(parents=True, exist_ok=True)
  image.save(output_path)
  return str(output_path)
