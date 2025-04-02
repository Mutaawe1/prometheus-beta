def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a string in a file.

    Args:
        file_path (str): Path to the file to modify
        old_string (str): The string to be replaced
        new_string (str): The string to replace with

    Returns:
        int: Number of replacements made

    Raises:
        FileNotFoundError: If the specified file does not exist
        TypeError: If any of the arguments are not strings
        ValueError: If old_string is empty
    """
    # Input validation
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(old_string, str):
        raise TypeError("old_string must be a string")
    if not isinstance(new_string, str):
        raise TypeError("new_string must be a string")
    
    if not old_string:
        raise ValueError("old_string cannot be empty")

    # Read the file contents
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    # Perform case-sensitive replacement
    replacements = content.count(old_string)
    modified_content = content.replace(old_string, new_string)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

    return replacements