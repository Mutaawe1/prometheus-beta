import pytest
from src.anagram_counter import count_anagrams

def test_count_anagrams_basic():
    """Test basic anagram counting functionality."""
    assert count_anagrams('abab') == 6

def test_count_anagrams_single_char():
    """Test a string with a single unique character."""
    assert count_anagrams('a') == 1

def test_count_anagrams_repeated_chars():
    """Test a string with repeated characters."""
    assert count_anagrams('aaa') == 3

def test_count_anagrams_longer_string():
    """Test a longer string with multiple anagram possibilities."""
    assert count_anagrams('abcd') == 10

def test_input_validation_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError):
        count_anagrams('')

def test_input_validation_uppercase():
    """Test that uppercase letters raise a ValueError."""
    with pytest.raises(ValueError):
        count_anagrams('Abab')

def test_input_validation_special_chars():
    """Test that special characters raise a ValueError."""
    with pytest.raises(ValueError):
        count_anagrams('ab!ab')