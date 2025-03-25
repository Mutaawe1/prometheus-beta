import pytest
from src.text_character_counter import count_vowels_consonants

def test_basic_text():
    """Test counting vowels and consonants in a simple text."""
    result = count_vowels_consonants("hello world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_mixed_case():
    """Test that the function is case-insensitive."""
    result = count_vowels_consonants("HeLLo WoRLD")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string returns zero counts."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("rhythm")
    assert result == {'vowels': 0, 'consonants': 6}

def test_with_punctuation_and_spaces():
    """Test that non-alphabetic characters are ignored."""
    result = count_vowels_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(None)