import pytest
from src.json_validator import is_valid_json

def test_valid_json_object():
    """Test a valid JSON object."""
    assert is_valid_json('{"key": "value"}') == True

def test_valid_json_array():
    """Test a valid JSON array."""
    assert is_valid_json('[1, 2, 3]') == True

def test_valid_json_nested():
    """Test a nested valid JSON object."""
    assert is_valid_json('{"key": {"nested": "value"}}') == True

def test_invalid_json_missing_quotes():
    """Test JSON with missing quotes."""
    assert is_valid_json('{key: "value"}') == False

def test_invalid_json_syntax():
    """Test JSON with syntax errors."""
    assert is_valid_json('{key: "value",}') == False

def test_empty_string():
    """Test empty string."""
    assert is_valid_json('') == False

def test_non_string_input():
    """Test non-string input."""
    assert is_valid_json(123) == False

def test_malformed_json():
    """Test various malformed JSON inputs."""
    test_cases = [
        '{',
        '}',
        '[',
        ']',
        'hello',
        '{"incomplete"'
    ]
    for case in test_cases:
        assert is_valid_json(case) == False