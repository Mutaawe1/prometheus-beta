import pytest
from src.palindrome_finder import find_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindromic_substrings("") == []

def test_single_character():
    """Test a string with a single character."""
    assert find_palindromic_substrings("a") == ["a"]

def test_simple_palindrome():
    """Test a simple palindrome with multiple characters."""
    assert find_palindromic_substrings("abba") == ["a", "b", "bb", "abba"]

def test_multiple_palindromes():
    """Test a string with multiple palindromic substrings."""
    result = find_palindromic_substrings("aaa")
    assert sorted(result) == ["a", "aa", "aaa"]

def test_no_palindromes():
    """Test a string with no palindromic substrings."""
    assert find_palindromic_substrings("abc") == ["a", "b", "c"]

def test_complex_string():
    """Test a more complex string with various palindromes."""
    result = find_palindromic_substrings("racecar")
    expected = ["a", "c", "e", "r", "ac", "ce", "rr", "aca", "cec", "acara", "racecar"]
    assert sorted(result) == sorted(expected)

def test_case_sensitivity():
    """Test that the function is case-sensitive."""
    result = find_palindromic_substrings("Aba")
    assert sorted(result) == ["A", "a", "b"]

def test_long_string():
    """Test a longer string with multiple palindromic substrings."""
    result = find_palindromic_substrings("aabaa")
    expected = ["a", "b", "aa", "aba", "aabaa"]
    assert sorted(result) == sorted(expected)