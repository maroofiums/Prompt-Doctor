RUBRIC = {
    "clarity": "Is the request clear and understandable?",
    "specificity": "Are the requirements specific enough?",
    "context": "Does the prompt provide sufficient context?",
    "output_format": "Does it specify the expected output format?",
}


def get_rubric() -> dict[str, str]:
    """Return the criteria used to diagnose a prompt."""
    return RUBRIC.copy()
