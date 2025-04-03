import pytest
from src.bubble_sort import bubble_sort

def test_bubble_sort_normal_list():
    """Test sorting a normal unsorted list."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_bubble_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert bubble_sort(arr) == []

def test_bubble_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert bubble_sort(arr) == [42]

def test_bubble_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bubble_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_bubble_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-1, -5, 4, 0, -3, 10]
    assert bubble_sort(arr) == [-5, -3, -1, 0, 4, 10]

def test_bubble_sort_invalid_input():
    """Test that an invalid input raises a TypeError."""
    with pytest.raises(TypeError):
        bubble_sort("not a list")
    with pytest.raises(TypeError):
        bubble_sort(123)
    with pytest.raises(TypeError):
        bubble_sort(None)