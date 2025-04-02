import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sleep_sort import sleep_sort

def test_sleep_sort_empty_list():
    """Test sorting an empty list."""
    assert sleep_sort([]) == []

def test_sleep_sort_single_element():
    """Test sorting a list with a single element."""
    assert sleep_sort([5]) == [5]

def test_sleep_sort_multiple_elements():
    """Test sorting multiple elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected_output = sorted(input_list)
    assert sleep_sort(input_list) == expected_output

def test_sleep_sort_all_same_elements():
    """Test sorting a list with all same elements."""
    input_list = [2, 2, 2, 2]
    assert sleep_sort(input_list) == input_list

def test_sleep_sort_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort([-1, 2, 3])

def test_sleep_sort_zero_included():
    """Test sorting a list that includes zero."""
    input_list = [3, 0, 1, 4, 2]
    expected_output = sorted(input_list)
    assert sleep_sort(input_list) == expected_output