import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_normal_case():
    """Test bitwise AND for a standard range of numbers."""
    assert bitwise_and_range(5, 7) == 4  # 101 & 110 & 111 = 100 (4)

def test_bitwise_and_range_same_number():
    """Test when start and end are the same number."""
    assert bitwise_and_range(10, 10) == 10

def test_bitwise_and_range_zero_to_zero():
    """Test range from 0 to 0."""
    assert bitwise_and_range(0, 0) == 0

def test_bitwise_and_range_larger_range():
    """Test a larger range of numbers."""
    assert bitwise_and_range(10, 20) == 0

def test_bitwise_and_range_single_number_range():
    """Test a range with a single number."""
    assert bitwise_and_range(15, 15) == 15

def test_bitwise_and_range_invalid_input_start_greater_end():
    """Test that an error is raised when start is greater than end."""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)

def test_bitwise_and_range_negative_input():
    """Test that an error is raised for negative inputs."""
    with pytest.raises(ValueError, match="Both start and end must be non-negative integers"):
        bitwise_and_range(-1, 5)
    
    with pytest.raises(ValueError, match="Both start and end must be non-negative integers"):
        bitwise_and_range(5, -1)