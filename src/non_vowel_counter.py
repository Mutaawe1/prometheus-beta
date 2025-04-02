def count_non_vowel_characters(input_string):
    """
    Count the number of non-vowel characters in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The number of non-vowel characters.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Define vowels (lowercase)
    vowels = set('aeiou')
    
    # Count non-vowel characters (case-insensitive, alphabetic characters only)
    return sum(1 for char in input_string.lower() 
               if char not in vowels and char.isalpha())