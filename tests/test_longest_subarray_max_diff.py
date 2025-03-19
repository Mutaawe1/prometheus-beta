import pytest
from src.longest_subarray_max_diff import find_longest_subarray_max_diff

def test_basic_scenarios():
    # Test basic scenarios with different inputs
    assert find_longest_subarray_max_diff([1, 5, 3, 8, 2], 3) == 3
    assert find_longest_subarray_max_diff([1, 2, 3, 4], 1) == 4
    assert find_longest_subarray_max_diff([1, 1, 1, 1], 0) == 4
    result = find_longest_subarray_max_diff([10, 1, 5, 8, 7], 2)
    print(f"Test case [10, 1, 5, 8, 7], k=2, result={result}")
    assert result == 3

def test_single_element_array():
    # Test array with single element
    assert find_longest_subarray_max_diff([5], 0) == 1
    assert find_longest_subarray_max_diff([5], 1) == 1

def test_edge_cases():
    # Test various edge cases
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_longest_subarray_max_diff([], 1)
    
    with pytest.raises(ValueError, match="Difference k must be non-negative"):
        find_longest_subarray_max_diff([1, 2, 3], -1)

def test_non_consecutive_scenarios():
    # Test scenarios where maximum subarray is not strictly consecutive
    assert find_longest_subarray_max_diff([3, 1, 4, 9, 2], 5) == 3
    result = find_longest_subarray_max_diff([8, 1, 6, 2, 5], 4)
    print(f"Test case [8, 1, 6, 2, 5], k=4, result={result}")
    assert result == 3

def test_large_differences():
    # Test scenarios with large differences
    result = find_longest_subarray_max_diff([100, 5, 90, 20, 80], 50)
    print(f"Test case [100, 5, 90, 20, 80], k=50, result={result}")
    assert result == 3
    assert find_longest_subarray_max_diff([1, 100, 50, 80, 20], 30) == 3