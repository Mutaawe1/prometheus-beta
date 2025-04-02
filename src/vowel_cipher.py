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
        if char.lower() in vowels_lower:
            # Determine the index in the appropriate vowel sequence
            vowel_sequence = vowels_lower if char.islower() else vowels_upper
            index = vowel_sequence.index(char.lower())
            next_vowel = vowel_sequence[(index + 1) % 5]
            
            # Return the next vowel with the same case as the original character
            return next_vowel.upper() if char.isupper() else next_vowel
        
        # If not a vowel, return the original character
        return char
    
    # Transform the input string
    return ''.join(replace_single_vowel(char) for char in input_string)