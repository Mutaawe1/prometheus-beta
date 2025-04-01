def count_words(text: str) -> int:
    """
    Count the number of words in a given string.

    Args:
        text (str): The input string to count words in.

    Returns:
        int: The number of words in the string.

    Notes:
        - Words are defined as sequences of non-whitespace characters
        - Multiple consecutive whitespaces are treated as a single separator
        - Empty strings or strings with only whitespace return 0
    """
    # Handle None or empty string cases
    if not text or not isinstance(text, str):
        return 0
    
    # Strip leading/trailing whitespace and split on whitespace
    # filter removes any empty strings from multiple consecutive spaces
    words = list(filter(bool, text.strip().split()))
    
    return len(words)