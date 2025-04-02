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
    
    # Function to replace a single vowel
    def replace_single_vowel(char):
        # Check lowercase vowels
        if char in vowels_lower:
            index = vowels_lower.index(char)
            return vowels_lower[(index + 1) % 5]
        
        # Check uppercase vowels
        if char in vowels_upper:
            index = vowels_upper.index(char)
            return vowels_upper[(index + 1) % 5]
        
        # If not a vowel, return the original character
        return char
    
    # Transform the input string
    return ''.join(replace_single_vowel(char) for char in input_string)