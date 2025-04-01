import pytest
from src.max_number import find_max_number

def test_find_max_number_positive_integers():
    """Test finding max in an array of positive integers."""
    assert find_max_number([1, 2, 3, 4, 5]) == 5

def test_find_max_number_negative_integers():
    """Test finding max in an array with negative integers."""
    assert find_max_number([-1, -2, -3, -4, -5]) == -1

def test_find_max_number_mixed_numbers():
    """Test finding max in an array with mixed positive and negative numbers."""
    assert find_max_number([-10, 0, 5, 3, -5]) == 5

def test_find_max_number_floating_point():
    """Test finding max in an array with floating point numbers."""
    assert find_max_number([1.5, 2.7, 0.3, 4.1]) == 4.1

def test_find_max_number_single_element():
    """Test finding max in an array with a single element."""
    assert find_max_number([42]) == 42

def test_find_max_number_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max_number([])

def test_find_max_number_non_numeric_raises_error():
    """Test that an array with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_max_number([1, 2, 'a', 3])

def test_find_max_number_mixed_types_raises_error():
    """Test that mixed numeric types raise a TypeError."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        find_max_number([1, 2.5, None, 3])