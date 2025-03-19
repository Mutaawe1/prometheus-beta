import pytest
from src.two_sum import find_two_sum_pairs

def test_find_two_sum_pairs_basic():
    """Test basic functionality of finding pairs."""
    arr = [1, 2, 3, 4, 5]
    target = 7
    expected = [(2, 5), (3, 4)]
    assert sorted(find_two_sum_pairs(arr, target)) == expected

def test_find_two_sum_pairs_no_pairs():
    """Test when no pairs sum to target."""
    arr = [1, 2, 3, 4, 5]
    target = 20
    assert find_two_sum_pairs(arr, target) == []

def test_find_two_sum_pairs_single_pair():
    """Test when only one pair exists."""
    arr = [1, 2, 3, 4, 5]
    target = 9
    assert find_two_sum_pairs(arr, target) == [(4, 5)]

def test_find_two_sum_pairs_invalid_input_type():
    """Test raising TypeError for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum_pairs("not a list", 10)
    
    with pytest.raises(TypeError, match="Target sum must be an integer"):
        find_two_sum_pairs([1, 2, 3], "not an int")

def test_find_two_sum_pairs_duplicate_input():
    """Test raising ValueError for input with duplicates."""
    with pytest.raises(ValueError, match="Input array must not contain duplicate elements"):
        find_two_sum_pairs([1, 2, 2, 3], 5)

def test_find_two_sum_pairs_empty_list():
    """Test behavior with an empty list."""
    assert find_two_sum_pairs([], 10) == []

def test_find_two_sum_pairs_negative_numbers():
    """Test with negative numbers and negative target."""
    arr = [-1, -2, -3, -4, -5]
    target = -7
    expected = [(-2, -5), (-3, -4)]
    assert sorted(find_two_sum_pairs(arr, target)) == expected