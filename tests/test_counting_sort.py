import pytest
from src.counting_sort import counting_sort

def test_counting_sort_basic():
    """Test basic sorting of a list of non-negative integers."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = [1, 2, 2, 3, 3, 4, 8]
    assert counting_sort(input_list) == expected

def test_counting_sort_empty_list():
    """Test sorting an empty list."""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element."""
    assert counting_sort([5]) == [5]

def test_counting_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == input_list

def test_counting_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == expected

def test_counting_sort_all_same_values():
    """Test sorting a list with all identical values."""
    input_list = [3, 3, 3, 3, 3]
    assert counting_sort(input_list) == input_list

def test_counting_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_counting_sort_negative_values():
    """Test that a ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        counting_sort([1, 2, -3, 4])

def test_counting_sort_non_integer_values():
    """Test that a ValueError is raised for non-integer values."""
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        counting_sort([1, 2, 3.5, 4])

def test_counting_sort_large_numbers():
    """Test sorting a list with large numbers."""
    input_list = [1000, 10, 100, 1, 10000]
    expected = [1, 10, 100, 1000, 10000]
    assert counting_sort(input_list) == expected