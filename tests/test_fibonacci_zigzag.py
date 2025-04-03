import pytest
from src.fibonacci_zigzag import fibonacci_zigzag

def test_fibonacci_zigzag_basic():
    """Test basic functionality of fibonacci_zigzag"""
    assert fibonacci_zigzag(5) == [1, 1, 2, 3, 5]
    assert fibonacci_zigzag(7) == [1, 1, 2, 3, 5, 8, 13]

def test_fibonacci_zigzag_edge_cases():
    """Test edge cases of fibonacci_zigzag"""
    # Single element
    assert fibonacci_zigzag(1) == [1]
    
    # Two elements
    assert fibonacci_zigzag(2) == [1, 1]

def test_fibonacci_zigzag_invalid_input():
    """Test invalid input handling"""
    # Non-integer input
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(3.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag("5")

def test_fibonacci_zigzag_larger_sequence():
    """Test larger Fibonacci sequences"""
    result = fibonacci_zigzag(10)
    # Check sequence length
    assert len(result) == 10
    
    # Verify Fibonacci property
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]