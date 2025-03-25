import pytest
from src.array_reverser import reverse_integer_array

def test_reverse_integer_array_normal():
    """Test reversing a standard list of integers."""
    input_arr = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_integer_array(input_arr) == expected

def test_reverse_integer_array_empty():
    """Test reversing an empty list."""
    input_arr = []
    expected = []
    assert reverse_integer_array(input_arr) == expected

def test_reverse_integer_array_single_element():
    """Test reversing a list with a single element."""
    input_arr = [42]
    expected = [42]
    assert reverse_integer_array(input_arr) == expected

def test_reverse_integer_array_negative_numbers():
    """Test reversing a list with negative numbers."""
    input_arr = [-1, -2, -3, -4, -5]
    expected = [-5, -4, -3, -2, -1]
    assert reverse_integer_array(input_arr) == expected

def test_reverse_integer_array_mixed_positive_negative():
    """Test reversing a list with mixed positive and negative numbers."""
    input_arr = [-10, 0, 5, 10, -5]
    expected = [-5, 10, 5, 0, -10]
    assert reverse_integer_array(input_arr) == expected

def test_reverse_integer_array_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        reverse_integer_array(42)

def test_reverse_integer_array_non_integer_elements():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        reverse_integer_array([1, 2, "3", 4, 5])

def test_reverse_integer_array_preserves_original():
    """Verify that the original list is not modified."""
    input_arr = [1, 2, 3, 4, 5]
    original_copy = input_arr.copy()
    _ = reverse_integer_array(input_arr)
    assert input_arr == original_copy