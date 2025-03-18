def switch_cases(str1: str, str2: str) -> str:
    """
    Swap the character cases between two input strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: A new string where characters from str1 have their case swapped,
             maintaining their original order
    
    Raises:
        TypeError: If either input is not a string
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Use a list comprehension to swap cases of str1
    return ''.join(
        c.lower() if c.isupper() else c.upper() 
        for c in str1
    )