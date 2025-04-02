import pytest
from src.integer_sorter import merge_sort

def test_merge_sort_normal_case():
    """Test sorting a standard list of integers."""
    input_list = [5, 2, 9, 1, 7, 6, 3]
    expected = [1, 2, 3, 5, 6, 7, 9]
    assert merge_sort(input_list) == expected

def test_merge_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == input_list

def test_merge_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(input_list) == expected

def test_merge_sort_empty_list():
    """Test sorting an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert merge_sort(input_list) == input_list

def test_merge_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert merge_sort(input_list) == expected

def test_merge_sort_input_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_merge_sort_element_type_error():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        merge_sort([1, 2, "3", 4])

def test_merge_sort_preserves_original():
    """Test that the original list is not modified."""
    input_list = [5, 2, 1, 8, 3]
    original_copy = input_list.copy()
    merge_sort(input_list)
    assert input_list == original_copy