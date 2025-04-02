import pytest
from src.sentence_case import convert_to_sentence_case

def test_convert_to_sentence_case_normal_string():
    """Test conversion of a normal string to sentence case."""
    assert convert_to_sentence_case("hello world") == "Hello world"

def test_convert_to_sentence_case_already_capitalized():
    """Test conversion of an already capitalized string."""
    assert convert_to_sentence_case("Hello World") == "Hello world"

def test_convert_to_sentence_case_all_uppercase():
    """Test conversion of an all uppercase string."""
    assert convert_to_sentence_case("HELLO WORLD") == "Hello world"

def test_convert_to_sentence_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_sentence_case("") == ""

def test_convert_to_sentence_case_single_character():
    """Test conversion of a single character string."""
    assert convert_to_sentence_case("a") == "A"
    assert convert_to_sentence_case("Z") == "Z"

def test_convert_to_sentence_case_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_sentence_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_sentence_case(None)

def test_convert_to_sentence_case_mixed_case():
    """Test conversion of a mixed case string."""
    assert convert_to_sentence_case("hELLo WoRLd") == "Hello world"