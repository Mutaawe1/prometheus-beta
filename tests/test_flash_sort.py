import pytest
from src.flash_sort import flash_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert flash_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert flash_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert flash_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert flash_sort(input_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert flash_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 3, -2, 0, 7, -1, 4]
    assert flash_sort(input_list) == [-5, -2, -1, 0, 3, 4, 7]

def test_all_same_elements():
    """Test sorting a list with all elements the same."""
    input_list = [42, 42, 42, 42, 42]
    assert flash_sort(input_list) == input_list

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        flash_sort("not a list")

def test_large_list():
    """Test sorting a larger list with mixed elements."""
    import random
    random.seed(42)  # For reproducibility
    input_list = [random.randint(-1000, 1000) for _ in range(1000)]
    assert flash_sort(input_list) == sorted(input_list)

def test_floating_point_numbers():
    """Test sorting a list of floating point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert flash_sort(input_list) == [0.58, 1.41, 2.23, 2.71, 3.14]