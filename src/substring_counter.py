def count_substring_occurrences(main_string: str, substring: str) -> int:
    """
    Count the number of times a substring occurs in a given string using O(n) time complexity.
    
    Uses the KMP (Knuth-Morris-Pratt) algorithm for efficient substring counting.
    
    Args:
        main_string (str): The string to search in.
        substring (str): The substring to count occurrences of.
    
    Returns:
        int: The number of times the substring appears in the main string.
    
    Raises:
        TypeError: If inputs are not strings.
        ValueError: If substring is an empty string.
    
    Time Complexity: O(n + m), where n is the length of main_string and m is the length of substring
    Space Complexity: O(m)
    """
    # Input validation
    if not isinstance(main_string, str) or not isinstance(substring, str):
        raise TypeError("Both inputs must be strings")
    
    # Check for empty substring 
    if not substring:
        raise ValueError("Substring cannot be an empty string")
    
    # Special case: if substring is longer than main string, return 0
    if len(substring) > len(main_string):
        return 0
    
    # Compute the longest proper prefix which is also a suffix (LPS) array
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    # Compute LPS array for the substring
    lps = compute_lps(substring)
    
    # Count occurrences using KMP algorithm
    occurrences = 0
    i = 0  # index for main_string
    j = 0  # index for substring
    
    while i < len(main_string):
        # If characters match, move both pointers
        if main_string[i] == substring[j]:
            i += 1
            j += 1
        
        # If full substring is matched, increment count and reset j
        if j == len(substring):
            occurrences += 1
            j = lps[j - 1]
        
        # If characters don't match
        elif i < len(main_string) and main_string[i] != substring[j]:
            # If j is not at the start, use LPS to skip characters
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return occurrences