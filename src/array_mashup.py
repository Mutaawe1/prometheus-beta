def arrayMashup(array1, array2):
    """
    Combine two arrays by summing elements at corresponding indices.

    Args:
        array1 (list): First input array of positive integers
        array2 (list): Second input array of positive integers

    Returns:
        list: A new array where each element is the sum of elements 
              at corresponding indices from input arrays

    Raises:
        TypeError: If inputs are not lists
        ValueError: If lists contain non-positive or non-integer values
        ValueError: If input lists have different lengths
    """
    # Type checking
    if not isinstance(array1, list) or not isinstance(array2, list):
        raise TypeError("Inputs must be lists")
    
    # Length checking
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have equal length")
    
    # Validate input values
    for arr in [array1, array2]:
        if not all(isinstance(x, int) and x > 0 for x in arr):
            raise ValueError("All elements must be positive integers")
    
    # Perform element-wise summation
    return [a + b for a, b in zip(array1, array2)]