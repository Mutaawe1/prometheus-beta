import pytest
from src.interval_scheduler import max_simultaneous_intervals

def test_basic_overlap():
    """Test basic scenario with overlapping intervals"""
    intervals = [(1, 3), (2, 4), (3, 5)]
    assert max_simultaneous_intervals(intervals) == 3

def test_no_overlap():
    """Test scenario with no overlapping intervals"""
    intervals = [(1, 2), (3, 4), (5, 6)]
    assert max_simultaneous_intervals(intervals) == 1

def test_empty_input():
    """Test empty input returns 0"""
    assert max_simultaneous_intervals([]) == 0

def test_single_interval():
    """Test single interval returns 1"""
    intervals = [(1, 5)]
    assert max_simultaneous_intervals(intervals) == 1

def test_complex_overlap():
    """Test complex overlapping scenario"""
    intervals = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
    assert max_simultaneous_intervals(intervals) == 3

def test_equal_times():
    """Test intervals with equal start and end times"""
    intervals = [(1, 1), (1, 1), (2, 2)]
    assert max_simultaneous_intervals(intervals) == 3

def test_nested_intervals():
    """Test nested intervals"""
    intervals = [(1, 5), (2, 4), (3, 3)]
    assert max_simultaneous_intervals(intervals) == 3

def test_none_input_raises_error():
    """Test None input raises ValueError"""
    with pytest.raises(ValueError, match="Input cannot be None"):
        max_simultaneous_intervals(None)

def test_invalid_interval_raises_error():
    """Test invalid intervals raise ValueError"""
    with pytest.raises(ValueError, match="Invalid interval"):
        max_simultaneous_intervals([(3, 1)])
    
    with pytest.raises(ValueError, match="Intervals must contain numeric values"):
        max_simultaneous_intervals([(1, 'a')])

def test_non_integer_valid_intervals():
    """Test intervals with floating point values"""
    intervals = [(1.5, 2.5), (2.0, 3.0), (2.3, 3.3)]
    assert max_simultaneous_intervals(intervals) == 3