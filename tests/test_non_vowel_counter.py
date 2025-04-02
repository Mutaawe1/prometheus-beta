import pytest
from src.non_vowel_counter import count_non_vowel_characters

def test_basic_counting():
    """Test basic non-vowel character counting."""
    assert count_non_vowel_characters("hello") == 3  # h, l, l
    assert count_non_vowel_characters("world") == 3  # w, r, l

def test_case_insensitivity():
    """Test case-insensitive vowel detection."""
    assert count_non_vowel_characters("HELLO") == 3
    assert count_non_vowel_characters("World") == 3

def test_mixed_characters():
    """Test strings with mixed characters."""
    assert count_non_vowel_characters("a1b2c3") == 3  # b, c, numbers don't count
    assert count_non_vowel_characters("Hello, World!") == 3  # h, l, l (punctuation ignored)

def test_only_vowels():
    """Test strings containing only vowels."""
    assert count_non_vowel_characters("aeiou") == 0
    assert count_non_vowel_characters("AEIOU") == 0

def test_only_non_vowels():
    """Test strings containing only non-vowel characters."""
    assert count_non_vowel_characters("bcdfg") == 5
    assert count_non_vowel_characters("BCDFG") == 5

def test_empty_string():
    """Test empty string input."""
    assert count_non_vowel_characters("") == 0

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        count_non_vowel_characters(123)
    with pytest.raises(TypeError):
        count_non_vowel_characters(None)
    with pytest.raises(TypeError):
        count_non_vowel_characters(["hello"])