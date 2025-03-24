import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) is True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_numbers = [12, 15, 18, 20, 100]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) is False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases for the perfect number function."""
    # Test 0 and negative numbers
    assert is_perfect_number(0) is False
    assert is_perfect_number(-6) is False
    assert is_perfect_number(-28) is False

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("6")
    
    with pytest.raises(ValueError):
        is_perfect_number(None)