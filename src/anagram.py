import unicodedata

def isAnagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. This implementation is case-insensitive
    and ignores whitespace and accents.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Examples:
        >>> isAnagram("listen", "silent")
        True
        >>> isAnagram("hello", "world")
        False
    """
    # Normalize Unicode characters, remove accents, convert to lowercase
    def normalize(s: str) -> str:
        # Decompose characters, remove non-spacing marks, convert to lowercase
        normalized = ''.join(
            char.lower() for char in unicodedata.normalize('NFKD', s) 
            if not unicodedata.combining(char)
        )
        # Remove whitespace
        return ''.join(normalized.split())

    # Normalize and compare
    cleaned_str1 = normalize(str1)
    cleaned_str2 = normalize(str2)

    # Check if the lengths are different
    if len(cleaned_str1) != len(cleaned_str2):
        return False

    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}

    # Count character frequencies
    for char in cleaned_str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in cleaned_str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compare character frequency dictionaries
    return char_count1 == char_count2