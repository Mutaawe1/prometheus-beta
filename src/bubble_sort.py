def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    This implementation improves standard Bubble Sort by:
    1. Breaking early if no swaps occur in a pass
    2. Reducing iterations for already sorted portions of the list
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Get the length of the list
    n = len(sorted_arr)
    
    # Iterate through the list
    for i in range(n):
        # Flag to track if any swaps occurred in this pass
        swapped = False
        
        # Last i elements are already in place, so reduce the inner loop range
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap the elements
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return sorted_arr