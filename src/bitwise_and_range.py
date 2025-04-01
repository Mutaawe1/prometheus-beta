def bitwise_and_range(start: int, end: int) -> int:
    """
    Calculate the bitwise AND of all numbers in the given range (inclusive).

    This function performs a bitwise AND operation on all integers from start to end.
    It handles various edge cases and ensures input validation.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Returns:
        int: The result of bitwise AND of all numbers in the range.

    Raises:
        ValueError: If start is greater than end or if either input is negative.
    """
    # Input validation
    if start < 0 or end < 0:
        raise ValueError("Both start and end must be non-negative integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    # Special case: If the range is a single number, return that number
    if start == end:
        return start
    
    # Find the common most significant bits
    result = start
    for num in range(start + 1, end + 1):
        result &= num
    
    return result