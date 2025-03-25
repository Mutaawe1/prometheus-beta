import pytest
from src.number_analysis import analyze_numbers

def test_mixed_numbers():
    """Test with a mix of even and odd numbers."""
    result = analyze_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_empty_list():
    """Test with an empty list."""
    result = analyze_numbers([])
    assert result == (0, 0)

def test_only_even_numbers():
    """Test with only even numbers."""
    result = analyze_numbers([2, 4, 6, 8])
    assert result == (20, 0)

def test_only_odd_numbers():
    """Test with only odd numbers."""
    result = analyze_numbers([1, 3, 5, 7])
    assert result == (0, 4)

def test_negative_numbers():
    """Test with negative numbers."""
    result = analyze_numbers([-1, -2, -3, -4, -5, -6])
    assert result == (-12, 3)

def test_zero_included():
    """Test with zero included."""
    result = analyze_numbers([0, 1, 2, 3])
    assert result == (2, 2)

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        analyze_numbers("not a list")

def test_invalid_input_non_integers():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        analyze_numbers([1, 2, "3", 4])