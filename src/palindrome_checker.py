import re

def is_palindrome(s: str) -> bool:
    """
    Determine if a given string is a palindrome, ignoring spaces, 
    punctuation, and capitalization.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]