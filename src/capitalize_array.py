def capitalize_strings(string_array):
    """
    Capitalize each string in the given array.

    Args:
        string_array (list): A list of strings to be capitalized.

    Returns:
        list: A new list with each string capitalized.

    Raises:
        TypeError: If the input is not a list.
        TypeError: If any element in the list is not a string.
    """
    # Check if input is a list
    if not isinstance(string_array, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are strings
    if not all(isinstance(item, str) for item in string_array):
        raise TypeError("All elements must be strings")
    
    # Capitalize each string in the list
    return [item.capitalize() for item in string_array]