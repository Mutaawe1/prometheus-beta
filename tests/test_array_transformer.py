import pytest
from src.array_transformer import transform_array

def test_transform_array_zero_elements():
    """Test that zero elements remain zero."""
    assert transform_array([0, 0, 0]) == [0, 0, 0]

def test_transform_array_non_zero_elements():
    """Test transformation of non-zero elements."""
    assert transform_array([1, 2, 3]) == [2, 5, 10]

def test_transform_array_mixed_elements():
    """Test array with mix of zero and non-zero elements."""
    assert transform_array([0, 1, 2, 0, 3]) == [0, 2, 5, 0, 10]

def test_transform_array_empty_list():
    """Test transformation of an empty list."""
    assert transform_array([]) == []

def test_transform_array_invalid_input_type():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        transform_array("not a list")

def test_transform_array_negative_numbers():
    """Test that negative numbers raise TypeError."""
    with pytest.raises(TypeError, match="All numbers must be non-negative"):
        transform_array([1, -1, 2])