import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiples():
    """Test basic scenario with simple multiples."""
    result = sum_of_multiples(10, [3, 5])
    print(f"Result: {result}")
    print(f"Expected multiples: 3, 5, 6, 9")
    assert result == 23  # 3 + 5 + 6 + 9 = 23

def test_single_multiple():
    """Test with a single multiple."""
    assert sum_of_multiples(10, [3]) == 18  # 3 + 6 + 9

def test_larger_limit():
    """Test with a larger limit."""
    result = sum_of_multiples(20, [3, 5])
    print(f"Result: {result}")
    print(f"Expected multiples: 3, 5, 6, 9, 10, 12, 15, 18")
    assert result == 78  # 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18

def test_no_multiples():
    """Test when no multiples are found."""
    assert sum_of_multiples(2, [7]) == 0

def test_error_on_negative_limit():
    """Test that ValueError is raised for negative limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(-5, [3, 5])

def test_error_on_zero_limit():
    """Test that ValueError is raised for zero limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(0, [3, 5])

def test_error_on_negative_multiple():
    """Test that ValueError is raised for negative multiple."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, -5])

def test_error_on_zero_multiple():
    """Test that ValueError is raised for zero multiple."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, 0])

def test_empty_multiples():
    """Test with empty multiples list."""
    assert sum_of_multiples(10, []) == 0

def test_overlapping_multiples():
    """Test case with overlapping multiples to ensure no double counting."""
    result = sum_of_multiples(15, [3, 5])
    print(f"Result: {result}")
    print(f"Expected multiples: 3, 5, 6, 9, 10, 12, 15")
    assert result == 45  # 3 + 5 + 6 + 9 + 10 + 12 + 15