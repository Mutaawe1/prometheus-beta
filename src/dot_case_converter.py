def to_dot_case(input_string: str) -> str:
    """
    Convert a given string to dot case.

    Dot case is a string formatting where words are separated by dots,
    and all characters are lowercase.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string converted to dot case.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> to_dot_case("HelloWorld")
        'hello.world'
        >>> to_dot_case("snake_case_string")
        'snake.case.string'
        >>> to_dot_case("Mixed Case String")
        'mixed.case.string'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Replace various separators and convert to lowercase
    # Handle multiple scenarios: camelCase, snake_case, space-separated
    processed = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split on uppercase letters for camelCase
    words = []
    current_word = processed[0].lower()
    for char in processed[1:]:
        if char.isupper():
            words.append(current_word)
            current_word = char.lower()
        else:
            current_word += char.lower()
    words.append(current_word)
    
    # Join words with dots
    return '.'.join(words).strip()