from collections import Counter
from typing import List

def sort_by_frequency(numbers: List[int]) -> List[int]:
    """
    Sort a list of integers based on their frequency.
    
    Less frequent elements appear first, and more frequent elements appear later.
    If multiple elements have the same frequency, maintain their relative order.
    
    Args:
        numbers (List[int]): Input list of integers to be sorted
    
    Returns:
        List[int]: Sorted list based on frequency (least frequent first)
    
    Examples:
        >>> sort_by_frequency([1, 1, 2, 2, 2, 3])
        [3, 1, 1, 2, 2, 2]
        >>> sort_by_frequency([])
        []
        >>> sort_by_frequency([4, 4, 4, 4, 4, 4])
        [4, 4, 4, 4, 4, 4]
    """
    # Handle empty list case
    if not numbers:
        return []
    
    # Count the frequency of each number
    freq_counter = Counter(numbers)
    
    # Sort the list based on frequency, then maintain original order for equal frequencies
    return sorted(numbers, key=lambda x: (freq_counter[x], numbers.index(x)))