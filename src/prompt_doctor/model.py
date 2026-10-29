import torch
from transformers import pipeline


MODEL_NAME = "google/flan-t5-base"

_generator = None

def get_generator():
    global _generator

    if _generator in None:
        _generator = pipeline(
            "text2text-generation",
            model=MODEL_NAME,
            device=0 if torch.cuda.is_available() else -1,
        )

    return _generator

def generate_response(prompt: str) -> str:

    result = get_generator()(
        prompt,
        max_new_tokens=256,
        do_sample=False
    )

    return result[0]["generated_text"]