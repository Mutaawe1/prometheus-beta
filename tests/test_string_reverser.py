import pytest
from src.string_reverser import reverse_string

def test_reverse_simple_string():
    """Test reversing a simple string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_multi_word_string():
    """Test reversing a multi-word string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_punctuation():
    """Test reversing a string with special characters."""
    assert reverse_string("hello, world!") == "!dlrow ,olleh"

def test_reverse_alphanumeric_string():
    """Test reversing a string with numbers and letters."""
    assert reverse_string("a1b2c3") == "3c2b1a"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_character():
    """Test reversing a single character."""
    assert reverse_string("a") == "a"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
        reverse_string(None)
        reverse_string(["hello"])