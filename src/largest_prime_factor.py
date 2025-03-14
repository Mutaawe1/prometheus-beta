def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        int: The largest prime factor of the input number.

    Raises:
        ValueError: If the input is not a positive integer greater than 1.
    """
    # Validate input
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be a positive integer greater than 1")

    # Find largest prime factor using trial division
    largest_prime_factor = 1
    
    # Handle even numbers first
    while n % 2 == 0:
        largest_prime_factor = 2
        n = n // 2
    
    # Check odd factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        # If factor divides n, remove it as many times as possible
        while n % factor == 0:
            largest_prime_factor = factor
            n = n // factor
        
        # Move to next odd factor
        factor += 2
    
    # If n is still > 1, it is the largest prime factor
    if n > 1:
        largest_prime_factor = n
    
    return largest_prime_factor