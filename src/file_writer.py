"""
Module for writing strings to text files.
"""

import os


def write_string_to_file(file_path: str, content: str, encoding: str = 'utf-8') -> None:
    """
    Write a string to a text file.

    Args:
        file_path (str): The path to the file where the string will be written.
        content (str): The string content to write to the file.
        encoding (str, optional): The encoding to use when writing the file. 
                                  Defaults to 'utf-8'.

    Raises:
        TypeError: If file_path or content is not a string.
        ValueError: If file_path is an empty string.
        PermissionError: If the file cannot be written due to permissions.
        IOError: If there's an issue writing to the file.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    
    # Validate file path is not empty
    if not file_path.strip():
        raise ValueError("file_path cannot be an empty string")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    
    # Write the content to the file
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot write to {file_path}")
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {str(e)}")