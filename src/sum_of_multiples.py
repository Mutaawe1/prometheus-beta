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
    
    # Use a set to store unique multiples to avoid double-counting
    unique_multiples = set()
    
    # Find all multiples for each number in the multiples list
    for multiple in multiples:
        # Start from the multiple itself and go up to the limit
        for i in range(multiple, limit + 1, multiple):
            # Only add if the number is less than or equal to the limit
            if i <= limit:
                unique_multiples.add(i)
    
    # Return the sum of unique multiples
    return sum(unique_multiples)