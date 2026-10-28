import pytest

from src.prompt_doctor.validator import validate_prompt


def test_valid_prompt():
    assert validate_prompt("  Explain machine learning  ") == (
        "Explain machine learning"
    )


def test_empty_prompt():
    with pytest.raises(ValueError):
        validate_prompt("   ")


def test_short_prompt():
    with pytest.raises(ValueError):
        validate_prompt("AI")


def test_non_string_prompt():
    with pytest.raises(TypeError):
        validate_prompt(123)