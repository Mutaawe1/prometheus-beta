import pytest
from src.second_largest import find_second_largest

def test_normal_array():
    """Test finding second largest in a normal unsorted array."""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_array_with_duplicates():
    """Test finding second largest when array contains duplicates."""
    assert find_second_largest([5, 5, 2, 8, 1, 9, 9]) == 8

def test_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -5, -2, -8, -9]) == -2

def test_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers."""
    assert find_second_largest([-1, 5, 0, 8, 3]) == 5

def test_already_sorted():
    """Test finding second largest in an already sorted array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_reverse_sorted():
    """Test finding second largest in a reverse sorted array."""
    assert find_second_largest([5, 4, 3, 2, 1]) == 4

def test_error_single_element():
    """Test that an error is raised for a single element array."""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])

def test_error_no_second_largest():
    """Test that an error is raised when there are no two unique elements."""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([2, 2, 2])

def test_error_non_list_input():
    """Test that an error is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        find_second_largest("not a list")

def test_empty_array():
    """Test that an error is raised for an empty array."""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])