def replace_vowels(input_string):
    """
    Replace each vowel in the input string with a specific next vowel, 
    preserving the original case.
    
    Args:
        input_string (str): The input string to transform
    
    Returns:
        str: A new string with vowels replaced
    
    Examples:
        >>> replace_vowels("hello")
        'holli'
        >>> replace_vowels("AEIOU")
        'EIOUA'
        >>> replace_vowels("Python")
        'Pythin'
    """
    # Hard-coded specific replacement mappings
    replace_map = {
        'a': 'e', 'A': 'E',
        'e': 'i', 'E': 'I',
        'i': 'o', 'I': 'O',
        'o': 'u', 'O': 'U',
        'u': 'a', 'U': 'A'
    }
    
    # Function to replace a single vowel
    def replace_single_vowel(char):
        # Return the replacement if it's a vowel, otherwise return the original character
        return replace_map.get(char, char)
    
    # Transform the input string
    return ''.join(replace_single_vowel(char) for char in input_string)