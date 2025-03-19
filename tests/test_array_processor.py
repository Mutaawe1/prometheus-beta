import pytest
from src.array_processor import process_array

def test_basic_processing():
    """Test basic functionality of the array processing"""
    assert process_array([1, 2, 3, 4, 5, 6]) == 6  # 2 and 4 remain, 3rd number (3) modified

def test_empty_list():
    """Test processing an empty list"""
    assert process_array([]) == 0

def test_no_even_numbers():
    """Test list with no even numbers"""
    assert process_array([1, 3, 5, 7, 9]) == 0

def test_all_even_numbers():
    """Test list with all even numbers"""
    assert process_array([2, 4, 6, 8, 10, 12]) == 30  # 6 is modified, so excluded

def test_mixed_numbers():
    """Test list with mixed positive and negative numbers"""
    assert process_array([-2, 1, -3, 4, 5, -6]) == -2  # -2 and 4 remain

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        process_array("not a list")

def test_non_numeric_elements():
    """Test that ValueError is raised for non-numeric elements"""
    with pytest.raises(ValueError):
        process_array([1, 2, "three", 4])

def test_single_element_list():
    """Test processing a single-element list"""
    assert process_array([2]) == 2

def test_two_element_list():
    """Test processing a two-element list"""
    assert process_array([2, 4]) == 6

def test_three_element_list():
    """Test processing a three-element list with third element modified"""
    assert process_array([1, 2, 3]) == 2