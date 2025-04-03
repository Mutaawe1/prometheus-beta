def remove_duplicates(input_list):
    """
    Remove duplicate items from a list of integers while preserving the original order.

    Args:
        input_list (list): A list of integers potentially containing duplicates.

    Returns:
        list: A new list with duplicates removed, maintaining the original order 
              of first occurrence of each unique element.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not an integer.
    """
    # Validate input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("All elements must be integers")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result