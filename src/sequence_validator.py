def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Empty or single-element list is considered valid
    if len(arr) <= 1:
        return True
    
    # Check for distinct integers in strictly increasing order
    for i in range(1, len(arr)):
        # Check if current element is strictly greater than previous
        if arr[i] <= arr[i-1]:
            return False
    
    return True