def find_min_max_difference(number_string):
    """
    Calculate the difference between the largest and smallest numbers in a comma-separated string of integers.
    
    Args:
        number_string (str): A string of comma-separated integers.
    
    Returns:
        int: The difference between the largest and smallest numbers.
    
    Raises:
        ValueError: If the input string is empty or contains non-integer values.
    """
    # Check for empty input
    if not number_string:
        raise ValueError("Input string cannot be empty")
    
    # Split the string and convert to integers
    numbers = []
    for num in number_string.split(','):
        try:
            numbers.append(int(num.strip()))
        except ValueError:
            # If any part of the string cannot be converted to an integer, raise an error
            raise ValueError("Input must be a comma-separated string of integers")
    
    # Check for empty list after parsing
    if not numbers:
        raise ValueError("No valid integers found in the input string")
    
    # Find and return the difference between max and min
    return max(numbers) - min(numbers)