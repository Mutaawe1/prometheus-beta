def extract_substrings(input_string):
    """
    Extract all possible substrings from the given input string.

    This function returns a list of all contiguous substrings 
    of the input string, including empty string and the full string itself.

    Args:
        input_string (str): The input string to extract substrings from.

    Returns:
        list: A list of all substrings of the input string.

    Examples:
        >>> extract_substrings("abc")
        ['', 'a', 'ab', 'abc', 'b', 'bc', 'c']
        >>> extract_substrings("")
        ['']
    """
    # Handle edge case of empty string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Generate all possible substrings
    substrings = ['']
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substrings.append(input_string[start:end])
    
    return substrings