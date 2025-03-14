import pytest
from src.substring_counter import count_substring_occurrences

def test_basic_substring_count():
    """Test basic substring counting"""
    assert count_substring_occurrences("hello hello", "hello") == 2
    assert count_substring_occurrences("banana", "an") == 2
    assert count_substring_occurrences("mississippi", "iss") == 2

def test_no_occurrences():
    """Test when substring does not exist in the main string"""
    assert count_substring_occurrences("hello world", "xyz") == 0
    assert count_substring_occurrences("abc", "def") == 0

def test_single_character_substring():
    """Test counting single character substrings"""
    assert count_substring_occurrences("aaa", "a") == 3
    assert count_substring_occurrences("hello", "l") == 2

def test_substring_longer_than_main_string():
    """Test when substring is longer than main string"""
    assert count_substring_occurrences("short", "longer substring") == 0

def test_substring_at_string_boundaries():
    """Test substrings at the start and end of the string"""
    assert count_substring_occurrences("prefixhellohellohollo", "hello") == 2
    assert count_substring_occurrences("prefixhellohellohollo", "hollo") == 1

def test_error_handling():
    """Test error cases"""
    with pytest.raises(TypeError):
        count_substring_occurrences(123, "test")
    
    with pytest.raises(TypeError):
        count_substring_occurrences("test", 123)
    
    with pytest.raises(ValueError):
        count_substring_occurrences("test", "")

def test_empty_main_string():
    """Test with an empty main string"""
    assert count_substring_occurrences("", "test") == 0
    assert count_substring_occurrences("", "") == 0

def test_overlapping_substrings():
    """Test overlapping substring occurrences"""
    assert count_substring_occurrences("aaaaa", "aa") == 4