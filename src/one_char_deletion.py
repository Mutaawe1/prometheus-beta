def can_convert_by_one_deletion(word1: str, word2: str) -> bool:
    """
    Check if word1 can be converted to word2 by deleting exactly one character.
    
    Args:
        word1 (str): The first input string
        word2 (str): The target string to convert to
    
    Returns:
        bool: True if word1 can be converted to word2 by deleting exactly one character, 
              False otherwise
    
    Raises:
        TypeError: If either input is not a string
    
    Examples:
        >>> can_convert_by_one_deletion('abcd', 'abc')  # delete 'd'
        True
        >>> can_convert_by_one_deletion('abc', 'abcd')  # too short
        False
        >>> can_convert_by_one_deletion('abc', 'abc')  # same word
        False
    """
    # Type checking
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Both inputs must be strings")
    
    # If lengths differ by more than 1, conversion is impossible
    if len(word1) - len(word2) != 1:
        return False
    
    # Try removing each character from word1 and check if it matches word2
    for i in range(len(word1)):
        # Create a new string with the i-th character removed
        candidate = word1[:i] + word1[i+1:]
        
        # If this candidate matches word2, return True
        if candidate == word2:
            return True
    
    # If no deletion results in word2, return False
    return False