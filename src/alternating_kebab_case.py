def to_alternating_kebab_case(input_string: str) -> str:
    """
    Convert a string to alternating kebab case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating kebab case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_kebab_case("hello world")
        'hello-WORLD'
        >>> to_alternating_kebab_case("Python is awesome")
        'python-IS-awesome'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Convert words to alternating case
    converted_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words (0, 2, 4...) in lowercase
            converted_words.append(word.lower())
        else:
            # Odd index words (1, 3, 5...) in uppercase
            converted_words.append(word.upper())
    
    # Join with kebab case
    return '-'.join(converted_words)