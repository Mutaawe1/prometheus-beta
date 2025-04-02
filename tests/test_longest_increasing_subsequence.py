import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    """Test a typical case with multiple increasing subsequences"""
    length, subsequence = find_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
    assert length == 4
    assert subsequence == [2, 5, 7, 101]

def test_empty_list():
    """Test an empty list input"""
    length, subsequence = find_longest_increasing_subsequence([])
    assert length == 0
    assert subsequence == []

def test_single_element():
    """Test a list with a single element"""
    length, subsequence = find_longest_increasing_subsequence([42])
    assert length == 1
    assert subsequence == [42]

def test_all_increasing():
    """Test a list that is already increasing"""
    length, subsequence = find_longest_increasing_subsequence([1, 2, 3, 4, 5])
    assert length == 5
    assert subsequence == [1, 2, 3, 4, 5]

def test_all_decreasing():
    """Test a list that is decreasing"""
    length, subsequence = find_longest_increasing_subsequence([5, 4, 3, 2, 1])
    assert length == 1
    assert subsequence in [[5], [4], [3], [2], [1]]

def test_with_duplicates():
    """Test a list with duplicate values"""
    length, subsequence = find_longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    assert length == 6
    assert subsequence == [0, 2, 6, 9, 13, 15]

def test_invalid_input_type():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_invalid_element_type():
    """Test that a list with non-numeric elements raises ValueError"""
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, "three", 4])