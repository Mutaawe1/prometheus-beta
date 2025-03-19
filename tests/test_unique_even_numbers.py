import pytest
from src.unique_even_numbers import extract_unique_even_numbers

def test_extract_unique_even_numbers_basic():
    """Test basic functionality of extracting unique even numbers."""
    input_list = [1, 2, 3, 4, 2, 6, 4, 8]
    expected = [2, 4, 6, 8]
    assert extract_unique_even_numbers(input_list) == expected

def test_extract_unique_even_numbers_empty_list():
    """Test behavior with an empty list."""
    assert extract_unique_even_numbers([]) == []

def test_extract_unique_even_numbers_no_evens():
    """Test with a list containing only odd numbers."""
    input_list = [1, 3, 5, 7, 9]
    assert extract_unique_even_numbers(input_list) == []

def test_extract_unique_even_numbers_mixed_types():
    """Test with a mix of positive and negative even numbers."""
    input_list = [-2, 1, -2, 3, 4, -4, 6, 4, 8]
    expected = [-2, 4, -4, 6, 8]
    assert extract_unique_even_numbers(input_list) == expected

def test_extract_unique_even_numbers_large_numbers():
    """Test with larger numbers."""
    input_list = [10000, 20000, 10000, 30000, 20000]
    expected = [10000, 20000, 30000]
    assert extract_unique_even_numbers(input_list) == expected