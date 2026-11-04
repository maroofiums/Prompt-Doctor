from src.prompt_doctor.schemas import PromptDiagnosis
from src.prompt_doctor.model import generate_response
from src.prompt_doctor.validator import validate_prompt
from src.prompt_doctor.prompt_builder import build_diagnosis_prompt


def parse_diagnosis(response: dict) -> PromptDiagnosis:
    """Validate the model's diagnosis response."""
    return PromptDiagnosis.model_validate(response)


def prepare_diagnosis(prompt: str) -> str:
    """Validate input and build diagnosis instructions."""
    prompt = validate_prompt(prompt)
    return build_diagnosis_prompt(prompt)


def diagnose(prompt: str) -> str:
    """Generate an AI diagnosis for the user's prompt."""
    instructions = prepare_diagnosis(prompt)
    return generate_response(instructions)
