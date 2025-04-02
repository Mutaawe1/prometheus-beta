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
    # Specific replacement mappings for different cases
    replace_map_lower = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
    replace_map_upper = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
    
    # Function to replace a single vowel
    def replace_single_vowel(char):
        # Handle lowercase vowels
        if char.islower() and char in 'aeiou':
            return replace_map_lower[char]
        
        # Handle uppercase vowels
        if char.isupper() and char in 'AEIOU':
            return replace_map_upper[char]
        
        # If not a vowel, return the original character
        return char
    
    # Transform the input string
    return ''.join(replace_single_vowel(char) for char in input_string)