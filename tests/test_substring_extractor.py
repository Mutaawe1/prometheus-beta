import pytest
from src.substring_extractor import extract_substrings

def test_basic_substring_extraction():
    """Test substring extraction for a simple string."""
    result = extract_substrings("abc")
    expected = ['', 'a', 'ab', 'abc', 'b', 'bc', 'c']
    assert sorted(result) == sorted(expected)

def test_empty_string():
    """Test substring extraction for an empty string."""
    result = extract_substrings("")
    assert result == ['']

def test_single_character_string():
    """Test substring extraction for a single character string."""
    result = extract_substrings("x")
    expected = ['', 'x']
    assert sorted(result) == sorted(expected)

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_substrings(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_substrings(None)

def test_string_with_special_characters():
    """Test substring extraction with special characters."""
    result = extract_substrings("a!b@c#")
    expected = ['', 'a', 'a!', 'a!b', 'a!b@', 'a!b@c', 'a!b@c#', 
                '!', '!b', '!b@', '!b@c', '!b@c#',
                'b', 'b@', 'b@c', 'b@c#',
                '@', '@c', '@c#',
                'c', 'c#', '#']
    assert len(result) == len(expected)
    assert sorted(result) == sorted(expected)

def test_repeated_characters_string():
    """Test substring extraction with repeated characters."""
    result = extract_substrings("aaa")
    expected = ['', 'a', 'aa', 'aaa', 'a', 'aa', 'a', 'aa', 'a']
    assert len(result) == 7  # Actual number of expected substrings
    assert all(x in result for x in expected)