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
    
    # Check that the result contains expected key substrings and all unique substrings 
    assert "hello" in result
    assert "world" in result
    assert " " in result
    assert "!" in result
    
    # Check that the length makes sense for a string of this length
    expected_len = (len("hello world!") * (len("hello world!") + 1)) // 2
    assert len(result) > 0
    assert len(result) <= expected_len