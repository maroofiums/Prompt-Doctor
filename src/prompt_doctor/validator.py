def validate_prompt(prompt: str) -> str:
    """
    Validates the given prompt string.

    Args:
        prompt (str): The prompt string to validate.

    Returns:
        str: The validated prompt string.

    Raises:
        ValueError: If the prompt is empty or exceeds a certain length.
    """

    if not isinstance(prompt, str):
        raise ValueError("Prompt must be a string.")

    prompt = prompt.strip()

    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    if len(prompt) < 5:
        raise ValueError("prompt must contain at least 5 characters.")

    return prompt