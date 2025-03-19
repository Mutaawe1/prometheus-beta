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
    
    # Store non-overlapping palindromes
    non_overlapping = []
    used_indices = set()
    
    # Preference order: longer palindromes first, then lexicographic order
    candidates = []
    for length in range(len(s), 1, -1):
        for start in range(len(s) - length + 1):
            substr = s[start:start+length]
            if is_palindrome(substr):
                candidates.append((len(substr), substr, start))
    
    # Sort by length (descending), then lexicographically
    candidates.sort(key=lambda x: (-x[0], x[1]))
    
    # Greedily select non-overlapping palindromes
    for _, substr, start in candidates:
        # Check if any indices are already used
        if not any(idx in used_indices for idx in range(start, start+len(substr))):
            non_overlapping.append(substr)
            used_indices.update(range(start, start+len(substr)))
    
    # Sort lexicographically and return
    return sorted(set(non_overlapping))