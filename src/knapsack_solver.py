def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.
    
    Args:
        items (list): A list of tuples, where each tuple contains (weight, value)
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Input validation
    if not isinstance(items, list):
        raise ValueError("Items must be a list of (weight, value) tuples")
    
    if not isinstance(capacity, int) or capacity < 0:
        raise ValueError("Capacity must be a non-negative integer")
    
    # Handle empty input cases
    if not items or capacity == 0:
        return 0
    
    # Validate each item
    for item in items:
        if not (isinstance(item, tuple) and len(item) == 2):
            raise ValueError("Each item must be a (weight, value) tuple")
        if not (isinstance(item[0], (int, float)) and isinstance(item[1], (int, float))):
            raise ValueError("Item weights and values must be numeric")
        if item[0] < 0 or item[1] < 0:
            raise ValueError("Item weights and values must be non-negative")
    
    # Number of items
    n = len(items)
    
    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(capacity + 1):
            # Do not include current item
            dp[i][w] = dp[i-1][w]
            
            # Include current item if it doesn't exceed capacity
            if weight <= w:
                # Compare current value with value including current item
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)
    
    # Return maximum value
    return dp[n][capacity]