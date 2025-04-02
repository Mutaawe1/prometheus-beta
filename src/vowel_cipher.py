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
            # Determine the current vowel in lowercase
            current_vowel = char.lower()
            
            # Find the index of the current vowel
            index = vowels_lower.index(current_vowel)
            
            # Get the next vowel with the same case
            next_vowel = vowels_lower[(index + 1) % 5]
            
            # Return the next vowel maintaining the original case
            return next_vowel.upper() if char.isupper() else next_vowel
        
        # If not a vowel, return the original character
        return char
    
    # Transform the input string
    return ''.join(replace_single_vowel(char) for char in input_string)