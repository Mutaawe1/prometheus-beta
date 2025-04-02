def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        tuple: A tuple containing:
            - Length of the longest increasing subsequence (int)
            - The longest increasing subsequence itself (list)
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        (4, [2, 5, 7, 101])
        >>> find_longest_increasing_subsequence([])
        (0, [])
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return 0, []
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming arrays
    # lengths[i] stores the length of LIS ending at index i
    lengths = [1] * n
    # predecessors[i] stores the index of the previous element in the LIS
    predecessors = [None] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            # Modify condition to choose the subsequence with the smallest elements
            if arr[i] > arr[j] and (lengths[i] < lengths[j] + 1 or 
                                     (lengths[i] == lengths[j] + 1 and arr[i] < arr[max_index])):
                lengths[i] = lengths[j] + 1
                predecessors[i] = j
        
        # Track the overall maximum
        if lengths[i] > max_length or (lengths[i] == max_length and arr[i] < arr[max_index]):
            max_length = lengths[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current is not None:
        subsequence.insert(0, arr[current])
        current = predecessors[current]
    
    return max_length, subsequence