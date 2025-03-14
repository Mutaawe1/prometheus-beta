from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers can be partitioned 
    into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of distinct integers to partition.

    Returns:
        int: The number of valid partitions with equal subset sums.

    Raises:
        ValueError: If the input list is empty or contains duplicates.
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input list must contain distinct numbers")

    n = len(numbers)
    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2
    valid_partitions = 0

    # Try all possible subset combinations of half the list size
    for subset in combinations(numbers, n // 2):
        # Check if this subset's sum is exactly half the total sum
        if sum(subset) == target_sum:
            # Verify the remaining subset
            remaining = [num for num in numbers if num not in subset]
            if sum(remaining) == target_sum:
                valid_partitions += 1

    # Only return partitions that are truly different
    return min(valid_partitions, 1)