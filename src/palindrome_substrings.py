def find_non_overlapping_palindromes(s: str) -> list[str]:
    """
    Find all non-overlapping palindromic substrings in the input string.
    
    A non-overlapping palindrome means once a substring is used, 
    its characters cannot be reused in another palindrome.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list[str]: Sorted list of unique non-overlapping palindromic substrings
    
    Raises:
        TypeError: If input is not a string
    """
    # Input validation
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty or too short, return empty list
    if len(s) < 2:
        return []
    
    def is_palindrome(substr: str) -> bool:
        """Check if a substring is a palindrome."""
        return substr == substr[::-1]
    
    # Find all palindromic substrings
    all_palindromes = []
    for length in range(2, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start+length]
            if is_palindrome(substr):
                all_palindromes.append((substr, start, start+length))
    
    # Sort palindromes by length (descending) and lexicographically
    all_palindromes.sort(key=lambda x: (-len(x[0]), x[0]))
    
    # Greedy selection of non-overlapping palindromes
    result = []
    used_indices = set()
    
    for substr, start, end in all_palindromes:
        # Check if the current substring overlaps with already used indices
        if not any(idx in used_indices for idx in range(start, end)):
            result.append(substr)
            used_indices.update(range(start, end))
    
    # Sort result lexicographically
    return sorted(result)