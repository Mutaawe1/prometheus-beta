import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_standard_case():
    """Test a standard case with a mix of increasing and non-increasing numbers."""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr) == 6

def test_another_standard_case():
    """Test another standard case with a more complex sequence."""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert longest_increasing_subsequence(arr) == 6

def test_empty_list():
    """Test behavior with an empty list."""
    arr = []
    assert longest_increasing_subsequence(arr) == 0

def test_single_element():
    """Test behavior with a single element list."""
    arr = [5]
    assert longest_increasing_subsequence(arr) == 1

def test_already_sorted():
    """Test a list that is already sorted in ascending order."""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert longest_increasing_subsequence(arr) == 9

def test_reverse_sorted():
    """Test a list sorted in descending order."""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1

def test_all_same_elements():
    """Test a list with all identical elements."""
    arr = [5, 5, 5, 5, 5]
    assert longest_increasing_subsequence(arr) == 1

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        longest_increasing_subsequence("not a list")

def test_non_integer_elements():
    """Test that a ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        longest_increasing_subsequence([1, 2, "3", 4, 5])

def test_complex_increasing_subsequence():
    """Test a more complex case with non-consecutive increasing subsequence."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert longest_increasing_subsequence(arr) == 4