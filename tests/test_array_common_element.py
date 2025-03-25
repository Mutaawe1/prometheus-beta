import pytest
from src.array_common_element import has_common_element

def test_common_element_exists():
    """Test when a common element exists"""
    assert has_common_element([1, 2, 3], [4, 5, 3]) == True
    assert has_common_element(['a', 'b', 'c'], ['d', 'b', 'e']) == True

def test_no_common_element():
    """Test when no common element exists"""
    assert has_common_element([1, 2, 3], [4, 5, 6]) == False
    assert has_common_element(['a', 'b', 'c'], ['d', 'e', 'f']) == False

def test_empty_arrays():
    """Test behavior with empty arrays"""
    assert has_common_element([], [1, 2, 3]) == False
    assert has_common_element([1, 2, 3], []) == False
    assert has_common_element([], []) == False

def test_large_arrays():
    """Test with large arrays with a common element deep in the array"""
    large_arr1 = list(range(1000)) + [1001]
    large_arr2 = list(range(500, 1500))
    assert has_common_element(large_arr1, large_arr2) == True

def test_invalid_input_types():
    """Test input type validation"""
    with pytest.raises(TypeError):
        has_common_element(123, [1, 2, 3])
    with pytest.raises(TypeError):
        has_common_element([1, 2, 3], "not a list")
    with pytest.raises(TypeError):
        has_common_element(None, [1, 2, 3])

def test_different_types():
    """Test arrays with different types of elements"""
    assert has_common_element([1, 'a', True], ['b', 1, False]) == True
    assert has_common_element([1, 'a', True], ['b', 2, False]) == False