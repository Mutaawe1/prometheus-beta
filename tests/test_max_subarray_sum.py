import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_scenario():
    """Test basic scenario with normal input"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_single_element_subarrays():
    """Test when k is 1"""
    arr = [5, 2, 8, 1, 9]
    k = 1
    assert max_subarray_sum(arr, k) == 9

def test_entire_array_sum():
    """Test when k equals array length"""
    arr = [3, 7, 2, 1, 5]
    k = len(arr)
    assert max_subarray_sum(arr, k) == 18

def test_invalid_k_too_small():
    """Test invalid k (less than 1)"""
    arr = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError, match="k must be at least 1"):
        max_subarray_sum(arr, 0)

def test_invalid_k_too_large():
    """Test invalid k (larger than array length)"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum(arr, 4)

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        max_subarray_sum("not a list", 2)
    
    with pytest.raises(TypeError, match="k must be an integer"):
        max_subarray_sum([1, 2, 3], "not an int")

def test_empty_array():
    """Test empty array (impossible scenario)"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        max_subarray_sum([], 1)

def test_negative_numbers():
    """Test array with negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 3
    assert max_subarray_sum(arr, k) == -6  # -1 + -2 + -3 = -6