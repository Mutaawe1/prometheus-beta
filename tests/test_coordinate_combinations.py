import pytest
from src.coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with simple coordinate pairs"""
    coords = [(1, 2), (3, 4), (1, 4), (3, 2)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [(1, 2), (1, 4), (3, 2), (3, 4)]

def test_duplicate_coordinates():
    """Test handling of duplicate coordinates"""
    coords = [(1, 1), (1, 1), (2, 2), (2, 2)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [(1, 1), (1, 2), (2, 1), (2, 2)]

def test_mixed_numeric_types():
    """Test with mixed integer and float coordinates"""
    coords = [(1, 2.5), (3.7, 4), (1, 4), (3.7, 2.5)]
    result = get_unique_coordinate_combinations(coords)
    assert result == [(1, 2.5), (1, 4), (3.7, 2.5), (3.7, 4)]

def test_empty_list():
    """Test with an empty list of coordinates"""
    coords = []
    result = get_unique_coordinate_combinations(coords)
    assert result == []

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_pair():
    """Test raising ValueError for invalid coordinate pairs"""
    with pytest.raises(ValueError, match="Each coordinate must be a pair"):
        get_unique_coordinate_combinations([(1, 2, 3)])

def test_invalid_coordinate_types():
    """Test raising TypeError for non-numeric coordinate values"""
    with pytest.raises(TypeError, match="Coordinate values must be numeric"):
        get_unique_coordinate_combinations([(1, 'a'), (2, 3)])