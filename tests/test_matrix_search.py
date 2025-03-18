import pytest
from src.matrix_search import search_sorted_matrix

def test_matrix_search_basic():
    """Test basic matrix search scenarios"""
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    
    # Test existing values
    assert search_sorted_matrix(matrix, 3) == True
    assert search_sorted_matrix(matrix, 16) == True
    assert search_sorted_matrix(matrix, 50) == True
    
    # Test non-existing values
    assert search_sorted_matrix(matrix, 13) == False
    assert search_sorted_matrix(matrix, 0) == False
    assert search_sorted_matrix(matrix, 51) == False

def test_matrix_search_edge_cases():
    """Test edge cases"""
    # Empty matrix
    assert search_sorted_matrix([], 5) == False
    
    # Single row matrix
    matrix_single_row = [[1, 2, 3, 4, 5]]
    assert search_sorted_matrix(matrix_single_row, 3) == True
    assert search_sorted_matrix(matrix_single_row, 6) == False
    
    # Single column matrix
    matrix_single_col = [[1], [3], [5], [7]]
    assert search_sorted_matrix(matrix_single_col, 3) == True
    assert search_sorted_matrix(matrix_single_col, 4) == False

def test_matrix_search_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Non-list matrix
    with pytest.raises(TypeError):
        search_sorted_matrix("not a matrix", 5)
    
    # Matrix with non-integer elements
    with pytest.raises(TypeError):
        search_sorted_matrix([[1, 2], ['a', 'b']], 2)
    
    # Matrix with nested non-list
    with pytest.raises(TypeError):
        search_sorted_matrix([1, 2, 3], 2)

def test_matrix_search_more_scenarios():
    """Additional test scenarios"""
    # Asymmetric matrix
    matrix_asymmetric = [
        [1, 3],
        [4, 5, 6, 7],
        [8, 9, 10]
    ]
    assert search_sorted_matrix(matrix_asymmetric, 6) == True
    assert search_sorted_matrix(matrix_asymmetric, 2) == False
    
    # Matrix with negative numbers
    matrix_with_negatives = [
        [-10, -5, 0],
        [3, 4, 5],
        [6, 7, 8]
    ]
    assert search_sorted_matrix(matrix_with_negatives, -5) == True
    assert search_sorted_matrix(matrix_with_negatives, 1) == False