import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert are_anagrams("rail safety", "fairy tales") == True
    assert are_anagrams("   stop   ", "   post   ") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams("abc", "abcd") == False
    assert are_anagrams("short", "shorter") == False

def test_type_errors():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "abc")
    with pytest.raises(TypeError):
        are_anagrams("abc", None)
    with pytest.raises(TypeError):
        are_anagrams([], "abc")