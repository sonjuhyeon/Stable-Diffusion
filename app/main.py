from fastapi import FastAPI, Query
from generator import generate_image

app = FastAPI()

@app.get("/generate")
def generate(prompt: str = Query(..., description="프롬프트 입력")):
  image_path = generate_image(prompt)
  return {"image_path": image_path}
