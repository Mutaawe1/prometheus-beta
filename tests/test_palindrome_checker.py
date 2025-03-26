import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    """Test non-palindrome scenarios."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_case_insensitive():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaceCar") == True

def test_punctuation_and_spaces():
    """Test palindromes with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_empty_and_single_char():
    """Test edge cases with empty and single-character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_type_error():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])