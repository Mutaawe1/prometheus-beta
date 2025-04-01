def edit_distance(str1: str, str2: str) -> int:
    """
    Calculate the Levenshtein (Edit) Distance between two strings.
    
    The Edit Distance is the minimum number of single-character edits 
    (insertions, deletions, or substitutions) required to change one string into another.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: The minimum number of edits required to transform str1 into str2
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Create a matrix to store edit distances
    m, n = len(str1), len(str2)
    
    # Initialize the dynamic programming matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Compute the edit distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters are the same, no edit needed
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Minimum of insert, delete, or substitute
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # deletion
                    dp[i][j-1],    # insertion
                    dp[i-1][j-1]   # substitution
                )
    
    # Return the bottom-right cell which contains the edit distance
    return dp[m][n]