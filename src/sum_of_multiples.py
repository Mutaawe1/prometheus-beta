def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of given numbers up to a specified limit.

    Args:
        limit (int): The upper bound for finding multiples (inclusive).
        multiples (list): A list of integers to find multiples of.

    Returns:
        int: The sum of all unique multiples of the numbers in the list 
             that are less than or equal to the limit.

    Raises:
        ValueError: If limit or any number in multiples is less than or equal to 0.
    """
    # Validate input
    if limit <= 0:
        raise ValueError("Limit must be a positive integer.")
    
    if not multiples:
        return 0
    
    # Validate each multiple
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers.")
    
    # Use a list to store multiples to maintain order and specific test case behavior
    unique_multiples = []
    
    # Find all multiples for each number in the multiples list
    for multiple in multiples:
        current = multiple
        while current <= limit:
            # Only add if not already in the list
            if current not in unique_multiples:
                unique_multiples.append(current)
            current += multiple
    
    # Return the sum of unique multiples
    return sum(unique_multiples)