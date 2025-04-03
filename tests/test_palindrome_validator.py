import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with different cases and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("Madam, I'm Adam") == True

def test_simple_palindromes():
    """Test simple palindromes."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False

def test_case_insensitivity():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaCeCaR") == True

def test_special_characters():
    """Test handling of special characters and spaces."""
    assert is_palindrome("A!@#$%^&*()b,c.d,c b A") == True
    assert is_palindrome("Hello, World!") == False

def test_edge_cases():
    """Test edge cases."""
    assert is_palindrome(" ") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False