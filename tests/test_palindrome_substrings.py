import pytest
from src.palindrome_substrings import find_non_overlapping_palindromes

def test_basic_palindromes():
    """Test finding basic non-overlapping palindromes."""
    assert find_non_overlapping_palindromes("aabaa") == ["aa", "aba"]

def test_empty_string():
    """Test empty string returns empty list."""
    assert find_non_overlapping_palindromes("") == []

def test_single_char():
    """Test single character string returns empty list."""
    assert find_non_overlapping_palindromes("a") == []

def test_no_palindromes():
    """Test string with no palindromes."""
    assert find_non_overlapping_palindromes("abcd") == []

def test_multiple_palindromes():
    """Test finding multiple non-overlapping palindromes."""
    result = find_non_overlapping_palindromes("abacabad")
    assert result == ["aba", "aa"]

def test_lexicographic_order():
    """Test palindromes are returned in lexicographic order."""
    result = find_non_overlapping_palindromes("xyyxxzzzz")
    assert result == ["xx", "yyy", "zzzz"]

def test_nested_palindromes():
    """Test handling of nested palindromes."""
    result = find_non_overlapping_palindromes("racecaranna")
    assert result == ["anna", "racecar"]

def test_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        find_non_overlapping_palindromes(123)

def test_unicode_palindromes():
    """Test finding palindromes with unicode characters."""
    result = find_non_overlapping_palindromes("ままなら")
    assert result == ["まま", "なら"]