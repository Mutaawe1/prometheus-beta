def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.

    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray

    Returns:
        int: Maximum sum of a subarray of length k
        
    Raises:
        ValueError: If k is less than 1 or greater than array length
        TypeError: If input is not a list or k is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Edge case checks
    if k < 1:
        raise ValueError("k must be at least 1")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # If array is empty and k is valid (impossible scenario), return 0
    if len(arr) == 0:
        return 0
    
    # Sliding window approach
    # Initialize the sum of first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max_sum
    for i in range(k, len(arr)):
        # Remove the first element of previous window
        # Add the next element to create new window
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum