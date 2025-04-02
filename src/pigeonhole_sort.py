def pigeonhole_sort(arr):
    """
    Implement the Pigeonhole Sort algorithm.
    
    Pigeonhole sort is an efficient sorting algorithm for lists with a limited range of integers.
    It works by distributing elements into a set of 'pigeonholes' and then collecting them back.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A sorted list of integers.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-integer elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find the range of the input
    min_val = min(arr)
    max_val = max(arr)
    
    # Create pigeonholes
    range_size = max_val - min_val + 1
    pigeonholes = [0] * range_size
    
    # Count occurrences of each element
    for num in arr:
        pigeonholes[num - min_val] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(range_size):
        # Add each number its corresponding number of times
        sorted_arr.extend([i + min_val] * pigeonholes[i])
    
    return sorted_arr