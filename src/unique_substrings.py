def get_unique_substrings(input_string):
    """
    Generate an array of all unique substrings within the given input string.
    
    Args:
        input_string (str): The input string to extract substrings from.
    
    Returns:
        list: A list of unique substrings, sorted alphabetically.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return []
    
    # Use a set to ensure uniqueness, then convert to sorted list
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substring = input_string[start:end]
            # Ensure single characters and special characters are included
            unique_substrings.add(substring)
    
    # Return sorted list of unique substrings
    return sorted(list(unique_substrings))