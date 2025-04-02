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

    # Split the content into words while preserving the original string
    result_lines = []
    total_replacements = 0

    # Process each line separately to preserve line endings
    for line in content.splitlines(True):
        # Count case-insensitive replacements
        lower_line = line.lower()
        lower_old_string = old_string.lower()
        replacements = lower_line.count(lower_old_string)
        total_replacements += replacements

        # Replace case-insensitively
        if replacements > 0:
            new_line = ''
            last_index = 0
            for i in range(len(line)):
                # Check for case-insensitive match
                if line[last_index:i+1].lower() == lower_old_string:
                    new_line += new_string
                    last_index = i + 1
                elif i == len(line) - 1:
                    new_line += line[last_index:]
            line = new_line

        result_lines.append(line)

    # Join the modified lines
    modified_content = ''.join(result_lines)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

    return total_replacements