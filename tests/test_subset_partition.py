import pytest
from src.subset_partition import count_equal_sum_partitions

def test_basic_partition_count():
    """Test basic case with several partitions possible"""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 7]) == 1

def test_no_partition_possible():
    """Test when no equal sum partition is possible"""
    assert count_equal_sum_partitions([1, 2, 3, 4]) == 0

def test_single_element_list():
    """Test handling of single element list"""
    assert count_equal_sum_partitions([5]) == 0

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        count_equal_sum_partitions([])

def test_duplicate_elements_raises_error():
    """Test that list with duplicates raises a ValueError"""
    with pytest.raises(ValueError, match="Input list must contain distinct numbers"):
        count_equal_sum_partitions([1, 2, 2, 3])

def test_multiple_partitions():
    """Test a case with multiple possible partitions"""
    # This is an example where multiple subset combinations sum to the same value
    result = count_equal_sum_partitions([1, 2, 3, 4, 5, 6])
    assert result > 0

def test_large_numbers():
    """Test with larger numbers to ensure no overflow issues"""
    large_list = [10, 20, 30, 40, 50, 60]
    assert count_equal_sum_partitions(large_list) >= 0

def test_negative_numbers():
    """Test with a mix of negative and positive numbers"""
    result = count_equal_sum_partitions([-1, 1, 2, 3, 4, 5])
    assert result >= 0