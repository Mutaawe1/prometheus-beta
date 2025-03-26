import pytest
from src.pair_product_calculator import calculate_pair_products

def test_basic_pair_products():
    """Test basic functionality with a simple list of integers."""
    result = calculate_pair_products([1, 2, 3])
    assert result == [1, 2, 3, 2, 4, 6, 3, 6, 9]

def test_negative_numbers():
    """Test functionality with negative numbers."""
    result = calculate_pair_products([-1, 0, 1])
    assert result == [1, 0, -1, 0, 0, 0, -1, 0, 1]

def test_single_element():
    """Test functionality with a single-element list."""
    result = calculate_pair_products([5])
    assert result == [25]

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_pair_products("not a list")

def test_invalid_input_non_integers():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_pair_products([1, 2, "3"])

def test_empty_list():
    """Test that a ValueError is raised for an empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        calculate_pair_products([])