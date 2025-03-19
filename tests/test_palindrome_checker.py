import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_insensitive_palindromes():
    """Test palindromes with mixed case."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_special_characters_palindromes():
    """Test palindromes with special characters and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge cases like empty string, single character, etc."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_string_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        is_palindrome(12321)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["racecar"])