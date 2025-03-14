import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_prime_number():
    """Test when input is a prime number"""
    assert find_largest_prime_factor(17) == 17

def test_composite_number():
    """Test with a composite number"""
    assert find_largest_prime_factor(13195) == 29

def test_large_number():
    """Test with a large number"""
    assert find_largest_prime_factor(600851475143) == 6857

def test_even_number():
    """Test with an even number"""
    assert find_largest_prime_factor(24) == 3

def test_square_number():
    """Test with a square number"""
    assert find_largest_prime_factor(25) == 5

def test_invalid_input_less_than_two():
    """Test invalid input less than 2"""
    with pytest.raises(ValueError):
        find_largest_prime_factor(1)

def test_invalid_input_negative():
    """Test negative input"""
    with pytest.raises(ValueError):
        find_largest_prime_factor(-10)

def test_invalid_input_float():
    """Test float input"""
    with pytest.raises(ValueError):
        find_largest_prime_factor(3.14)

def test_invalid_input_zero():
    """Test zero input"""
    with pytest.raises(ValueError):
        find_largest_prime_factor(0)