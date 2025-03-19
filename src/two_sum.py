def find_two_sum_pairs(arr, target_sum):
    """
    Find all unique pairs of numbers in the array that add up to the target sum.

    Args:
        arr (list): A list of unique integers to search for pairs.
        target_sum (int): The target sum to find pairs for.

    Returns:
        list: A list of tuples, where each tuple contains two numbers that sum to target_sum.

    Raises:
        TypeError: If input is not a list or target_sum is not an integer.
        ValueError: If the input list contains duplicates.
    """
    # Validate input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not isinstance(target_sum, int):
        raise TypeError("Target sum must be an integer")

    # Check for duplicates
    if len(arr) != len(set(arr)):
        raise ValueError("Input array must not contain duplicate elements")

    # Use a set for O(n) time complexity
    seen = set()
    pairs = []

    for num in arr:
        complement = target_sum - num
        if complement in seen and complement != num:
            # Ensure pairs are sorted and unique
            pair = tuple(sorted((num, complement)))
            if pair not in pairs:
                pairs.append(pair)
        seen.add(num)

    return pairs