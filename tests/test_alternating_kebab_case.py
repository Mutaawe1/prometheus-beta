import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert to_alternating_kebab_case("hello world") == "hello-WORLD"
    assert to_alternating_kebab_case("python is awesome") == "python-IS-awesome"

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_kebab_case("hello") == "hello"

def test_multiple_words():
    """Test conversion with multiple words."""
    assert to_alternating_kebab_case("this is a test string") == "this-IS-a-TEST-string"

def test_empty_string():
    """Test conversion of an empty string."""
    assert to_alternating_kebab_case("") == ""

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        to_alternating_kebab_case(123)
    
    with pytest.raises(TypeError):
        to_alternating_kebab_case(None)

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_alternating_kebab_case("MiXeD CaSe InPuT") == "mixed-CASE-input"

def test_long_multiword_string():
    """Test conversion of a long multi-word string."""
    input_str = "this is a very long string with multiple words"
    expected = "this-IS-a-VERY-long-STRING-with-MULTIPLE-words"
    assert to_alternating_kebab_case(input_str) == expected