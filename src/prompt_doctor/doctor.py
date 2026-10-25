from src.prompt_doctor.validator import validate_prompt
from src.prompt_doctor.prompt_builder import build_diagnosis_prompt


def prepare_diagnosis(prompt: str) -> str:
    
    """Validate a prompt and prepare it for diagnosis."""

    prompt = validate_prompt(prompt)
    prompt = build_diagnosis_prompt(prompt)

    return prompt