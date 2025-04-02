def replace_vowels(input_string):
    """
    Replace each vowel in the input string with the next vowel in the alphabet, 
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
    # Define vowel sequences (lowercase and uppercase)
    vowels_lower = 'aeiou'
    vowels_upper = 'AEIOU'
    
    # Define a specific replacement mapping
    replace_map_lower = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}
    replace_map_upper = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
    
    # Function to replace a single vowel
    def replace_single_vowel(char):
        # Check and replace lowercase vowels
        if char in vowels_lower:
            return replace_map_lower[char]
        
        # Check and replace uppercase vowels
        if char in vowels_upper:
            return replace_map_upper[char]
        
        # If not a vowel, return the original character
        return char
    
    # Transform the input string
    return ''.join(replace_single_vowel(char) for char in input_string)