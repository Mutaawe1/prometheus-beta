from collections import Counter
from typing import List

def sort_by_frequency(numbers: List[int]) -> List[int]:
    """
    Sort a list of integers based on their frequency.
    
    Less frequent elements appear first, and more frequent elements appear later.
    If multiple elements have the same frequency, maintain their original order.
    
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
    
    # Create a stable sort using the original list's indices
    # This ensures that for equal frequencies, the original order is maintained
    def custom_key(x):
        # Tuple with frequency first, then index
        # Using enumerate() with original list to get correct indices
        for i, num in enumerate(numbers):
            if num == x:
                return (freq_counter[x], i)
    
    return sorted(numbers, key=custom_key)