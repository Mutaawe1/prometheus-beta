def reverse_string(input_str: str) -> str:
    """
    Reverse a given string, preserving special characters and handling multi-word inputs.
    
    Args:
        input_str (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("hello world!")
        '!dlrow olleh'
        >>> reverse_string("a1b2c3")
        '3c2b1a'
    """
    # Validate input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_str:
        return ""
    
    # Reverse the string
    return input_str[::-1]