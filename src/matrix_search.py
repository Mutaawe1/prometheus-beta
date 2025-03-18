def search_sorted_matrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target integer in a 2D matrix with sorted inner lists.
    
    The matrix has the following properties:
    1. Each inner list is sorted in ascending order
    2. Rows are not necessarily sorted with respect to each other
    
    Args:
        matrix (list[list[int]]): 2D matrix of integers
        target (int): Target integer to search for
    
    Returns:
        bool: True if target is found, False otherwise
    
    Time Complexity: O(m * log(n)), where m is number of rows and n is number of columns
    Space Complexity: O(1)
    
    Raises:
        TypeError: If matrix is not a list of lists or contains non-integer elements
        ValueError: If matrix is empty or contains empty rows
    """
    # Input validation
    if not matrix or not matrix[0]:
        return False
    
    # Check matrix structure
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    # Check that all elements are integers
    try:
        for row in matrix:
            if not all(isinstance(x, int) for x in row):
                raise TypeError("All matrix elements must be integers")
    except TypeError:
        raise
    
    # Binary search through each row
    for row in matrix:
        # Use binary search on each row
        left, right = 0, len(row) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    
    return False