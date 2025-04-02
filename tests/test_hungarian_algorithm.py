import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_assignment

def test_basic_assignment():
    """Test a basic assignment problem"""
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 5, 9]
    ]
    assignments = hungarian_assignment(cost_matrix)
    
    # Validate number of assignments
    assert len(assignments) == 3
    
    # Validate unique assignments
    assigned_rows = set(a[0] for a in assignments)
    assigned_cols = set(a[1] for a in assignments)
    assert len(assigned_rows) == 3
    assert len(assigned_cols) == 3

def test_rectangular_matrix():
    """Test a rectangular cost matrix"""
    cost_matrix = [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 5, 7, 9]
    ]
    assignments = hungarian_assignment(cost_matrix)
    
    # Validate number of assignments (should be min of rows or cols)
    assert len(assignments) == 3

def test_single_element_matrix():
    """Test a single element matrix"""
    cost_matrix = [[5]]
    assignments = hungarian_assignment(cost_matrix)
    
    assert assignments == [(0, 0)]

def test_empty_matrix():
    """Test an empty matrix"""
    cost_matrix = []
    assignments = hungarian_assignment(cost_matrix)
    
    assert assignments == []

def test_invalid_input():
    """Test invalid input raises ValueError"""
    with pytest.raises(ValueError):
        hungarian_assignment(None)
    
    with pytest.raises(ValueError):
        hungarian_assignment("not a matrix")

def test_complex_assignment():
    """Test a more complex assignment scenario"""
    cost_matrix = [
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ]
    assignments = hungarian_assignment(cost_matrix)
    
    # Validate number of assignments
    assert len(assignments) == 4
    
    # Validate unique assignments
    assigned_rows = set(a[0] for a in assignments)
    assigned_cols = set(a[1] for a in assignments)
    assert len(assigned_rows) == 4
    assert len(assigned_cols) == 4