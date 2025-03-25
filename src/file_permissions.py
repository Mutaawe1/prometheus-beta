import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.

    Args:
        file_path (str): The path to the file whose permissions are to be changed.
        mode (int): The new permission mode (in octal representation).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permissions to modify the file.
        TypeError: If the input types are incorrect.
        ValueError: If the mode is invalid.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Normalize the file path
    file_path = os.path.abspath(os.path.expanduser(file_path))
    
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate mode is a valid octal permission
    if mode < 0 or mode > 0o777:
        raise ValueError("Invalid file mode. Must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to modify {file_path}")
    
    return True