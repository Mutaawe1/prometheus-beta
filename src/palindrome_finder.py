def find_palindromic_substrings(s: str) -> list[str]:
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a contiguous sequence of characters 
    that reads the same backwards as forwards.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list[str]: A list of all unique palindromic substrings found in the input string.
    
    Examples:
        >>> find_palindromic_substrings("aaa")
        ['a', 'aa', 'aaa']
        >>> find_palindromic_substrings("abba")
        ['a', 'b', 'bb', 'abba']
    """
    # Handle edge cases
    if not s:
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Check if substring is a palindrome
            substring = s[i:j+1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Sort by length (shorter first) and then lexicographically
    return sorted(list(palindromes), key=lambda x: (len(x), x))