import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    assert pigeonhole_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]

def test_already_sorted():
    """Test list that is already sorted"""
    assert pigeonhole_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test list in reverse order"""
    assert pigeonhole_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    """Test list with duplicate elements"""
    assert pigeonhole_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_single_element():
    """Test list with a single element"""
    assert pigeonhole_sort([42]) == [42]

def test_empty_list():
    """Test empty list"""
    assert pigeonhole_sort([]) == []

def test_negative_numbers():
    """Test list with negative numbers"""
    assert pigeonhole_sort([-5, -2, -8, -1, -9]) == [-9, -8, -5, -2, -1]

def test_mixed_positive_negative():
    """Test list with mixed positive and negative numbers"""
    assert pigeonhole_sort([-3, 4, 0, -1, 2]) == [-3, -1, 0, 2, 4]

def test_invalid_input_type():
    """Test invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        pigeonhole_sort("not a list")

def test_non_integer_elements():
    """Test list with non-integer elements raises ValueError"""
    with pytest.raises(ValueError):
        pigeonhole_sort([1, 2, 3.5, 4])