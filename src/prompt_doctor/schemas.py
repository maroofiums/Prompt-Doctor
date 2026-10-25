from pydantic import BaseModel, Field
from typing import List

class PromptDiagnosis(BaseModel):
    clarity: int = Field(ge=1, le=5)
    specificity: int = Field(ge=1, le=5)
    context: int = Field(ge=1, le=5)
    output_format: int = Field(ge=1, le=5)

    issues: List[str]
    improved_prompt: str
    explanation: List[str]