import pytest
from src.unique_substrings import get_unique_substrings

def test_get_unique_substrings_normal_case():
    """Test with a typical string input."""
    result = get_unique_substrings("abc")
    expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert result == expected

def test_get_unique_substrings_empty_string():
    """Test with an empty string."""
    result = get_unique_substrings("")
    assert result == []

def test_get_unique_substrings_single_char():
    """Test with a single character string."""
    result = get_unique_substrings("a")
    assert result == ['a']

def test_get_unique_substrings_repeated_chars():
    """Test with a string containing repeated characters."""
    result = get_unique_substrings("aaa")
    expected = ['a', 'aa', 'aaa']
    assert result == expected

def test_get_unique_substrings_invalid_input():
    """Test with invalid input types."""
    with pytest.raises(TypeError):
        get_unique_substrings(123)
    
    with pytest.raises(TypeError):
        get_unique_substrings(None)

def test_get_unique_substrings_special_chars():
    """Test with special characters and spaces."""
    result = get_unique_substrings("hello world!")
    expected = [
        ' ', '!', 'd', 'e', 'h', 'hello', 'hello ', 'hello w', 
        'hello wo', 'hello wor', 'hello worl', 'hello world', 
        'hello world!', 'l', 'll', 'lo', 'lo ', 'lo w', 
        'lo wo', 'lo wor', 'lo worl', 'lo world', 'lo world!', 
        'o', 'o ', 'o w', 'o wo', 'o wor', 'o worl', 'o world', 
        'o world!', 'r', 'rl', 'rld', 'rld!', 'w', 'wo', 
        'wor', 'worl', 'world', 'world!', 'd!', 'l!', 'o!', 
        'world!'
    ]
    assert sorted(result) == sorted(expected)