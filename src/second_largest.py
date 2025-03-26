def find_second_largest(arr):
    """
    Find the second largest element in an array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The second largest unique integer in the array.

    Raises:
        ValueError: If the input array has fewer than 2 unique elements.
    """
    # Check if input is valid
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) < 2:
        raise ValueError("Array must contain at least 2 unique elements")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    # Check if there are at least 2 unique elements
    if len(unique_sorted) < 2:
        raise ValueError("Array must contain at least 2 unique elements")
    
    # Return the second element (which is the second largest)
    return unique_sorted[1]