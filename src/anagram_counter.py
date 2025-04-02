import re

def count_anagrams(s):
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a substring that can be rearranged to form another substring.
    Considers all possible substrings and their permutations.
    
    Args:
        s (str): Input string containing only lowercase English letters.
    
    Returns:
        int: Number of distinct anagrams in the string.
    
    Raises:
        ValueError: If input is empty or contains non-lowercase letters.
    """
    # Validate input
    if not s:
        raise ValueError("Input must be a non-empty string")
    
    # Check if input contains only lowercase letters
    if not re.match(r'^[a-z]+$', s):
        raise ValueError("Input must contain only lowercase letters")
    
    # Set to store unique sorted anagram signatures
    anagram_signatures = set()
    
    # Generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # Get the substring
            substring = s[i:j]
            
            # Create a canonical signature by sorting the characters
            signature = ''.join(sorted(substring))
            
            # Add to set of unique signatures
            anagram_signatures.add(signature)
    
    # Return the count of unique anagram signatures
    return len(anagram_signatures)