def has_common_element(arr1, arr2):
    """
    Check if two arrays have at least one common element.
    
    Args:
        arr1 (list): First input array
        arr2 (list): Second input array
    
    Returns:
        bool: True if arrays have at least one common element, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Raises:
        TypeError: If inputs are not lists
    
    Examples:
        >>> has_common_element([1, 2, 3], [4, 5, 3])
        True
        >>> has_common_element([1, 2, 3], [4, 5, 6])
        False
    """
    # Validate input types
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("Both inputs must be lists")
    
    # Use a set for O(n) lookup time
    element_set = set(arr1)
    
    # Check for common elements in O(n)
    for item in arr2:
        if item in element_set:
            return True
    
    return False