import pytest
from src.array_mashup import arrayMashup

def test_basic_mashup():
    """Test basic array mashup with simple positive integers"""
    result = arrayMashup([1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9], "Should sum corresponding elements"

def test_single_element_arrays():
    """Test mashup with single-element arrays"""
    result = arrayMashup([10], [20])
    assert result == [30], "Should work with single-element arrays"

def test_empty_arrays():
    """Test mashup with empty arrays"""
    result = arrayMashup([], [])
    assert result == [], "Should return empty list for empty input arrays"

def test_different_length_arrays():
    """Test that different length arrays raise ValueError"""
    with pytest.raises(ValueError, match="Input arrays must have equal length"):
        arrayMashup([1, 2], [1, 2, 3])

def test_non_positive_integers():
    """Test that non-positive integers raise ValueError"""
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        arrayMashup([1, 2, -3], [4, 5, 6])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 0], [4, 5, 6])

def test_non_integer_inputs():
    """Test that non-integer inputs raise TypeError or ValueError"""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        arrayMashup(123, [1, 2, 3])
    
    with pytest.raises(ValueError, match="All elements must be positive integers"):
        arrayMashup([1, 2, 3.5], [4, 5, 6])

def test_large_numbers():
    """Test mashup with large positive integers"""
    result = arrayMashup([1000000, 2000000], [3000000, 4000000])
    assert result == [4000000, 6000000], "Should handle large positive integers"