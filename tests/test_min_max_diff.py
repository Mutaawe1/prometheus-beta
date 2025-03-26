import pytest
from src.min_max_diff import find_min_max_difference

def test_basic_positive_numbers():
    """Test with basic positive comma-separated integers."""
    assert find_min_max_difference("1,5,3,9,2") == 8

def test_negative_numbers():
    """Test with a mix of positive and negative numbers."""
    assert find_min_max_difference("-5,0,10,-2,7") == 15

def test_single_number():
    """Test with a single number."""
    assert find_min_max_difference("42") == 0

def test_whitespace_handling():
    """Test with extra whitespace around numbers."""
    assert find_min_max_difference(" 1 , 5 , 3 , 9 , 2 ") == 8

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_min_max_difference("")

def test_non_integer_raises_error():
    """Test that non-integer input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a comma-separated string of integers"):
        find_min_max_difference("1,2,three,4")

def test_empty_after_parsing_raises_error():
    """Test that string with only non-integers raises a ValueError."""
    with pytest.raises(ValueError, match="No valid integers found in the input string"):
        find_min_max_difference("a,b,c")