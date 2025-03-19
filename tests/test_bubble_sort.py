import pytest
from src.bubble_sort import optimized_bubble_sort

def test_basic_sorting():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert optimized_bubble_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_list_with_duplicates():
    """Test sorting a list with duplicate values"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert optimized_bubble_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert optimized_bubble_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert optimized_bubble_sort(input_list) == input_list

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        optimized_bubble_sort("not a list")
        optimized_bubble_sort(123)
        optimized_bubble_sort(None)

def test_original_list_not_modified():
    """Ensure the original list is not modified"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    optimized_bubble_sort(input_list)
    assert input_list == original_copy