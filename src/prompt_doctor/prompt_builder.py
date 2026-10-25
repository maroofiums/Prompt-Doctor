from src.prompt_doctor.rubric import get_rubric

def build_diagnosis_prompt(prompt: str) -> str:
    """
        Build instructions for diagnosing a user prompt.
    """

    criteria = get_rubric()

    rubric_text = "\n".join(
        f"- {name}: {description}"
        for name, description in criteria.items()
    )

    return f"""
        You are Prompt Doctor, an expert prompt engineer.

        Diagnose the user's prompt using these criteria:
        {rubric_text}

        Score each criterion from 1 (poor) to 5 (excellent).
        Identify specific issues and create an improved prompt.
        Explain each improvement briefly.

        User prompt:
        <prompt>
            {prompt}
        </prompt>
    """.strip()