def convert_to_sentence_case(text):
    """
    Convert a string to sentence case.

    Sentence case capitalizes the first character of the string 
    and ensures the rest of the characters are lowercase.

    Args:
        text (str): The input string to convert to sentence case.

    Returns:
        str: The input string converted to sentence case.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not text:
        return text
    
    # Capitalize the first character and make the rest lowercase
    return text[0].upper() + text[1:].lower()