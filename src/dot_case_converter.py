import re

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
    
    # Remove non-alphanumeric characters
    input_string = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Use regex to split camelCase, PascalCase
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', input_string)
    
    # Convert to lowercase
    words = [word.lower() for word in words]
    
    # Join with dots
    return '.'.join(words)