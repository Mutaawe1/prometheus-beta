import pytest
from src.bit_operations import count_set_bits

def test_count_set_bits_positive_numbers():
    """Test counting set bits for various positive integers."""
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(5) == 2   # Binary: 101
    assert count_set_bits(7) == 3   # Binary: 111
    assert count_set_bits(15) == 4  # Binary: 1111
    assert count_set_bits(255) == 8 # Binary: 11111111

def test_count_set_bits_negative_numbers():
    """Test counting set bits for negative integers."""
    assert count_set_bits(-5) == 2   # Absolute value of 5
    assert count_set_bits(-15) == 4  # Absolute value of 15
    assert count_set_bits(-1) == 1   # All 1s in two's complement

def test_count_set_bits_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_set_bits("not an integer")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_set_bits(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_set_bits(None)

def test_count_set_bits_large_numbers():
    """Test counting set bits for large numbers."""
    large_num = 2**30 - 1  # Large positive number with many set bits
    assert count_set_bits(large_num) == 30