import os
import shutil

def delete_empty_directory(path):
    """
    Delete an empty directory.

    Args:
        path (str): Path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: If the directory is not empty or cannot be deleted.
    """
    # Normalize the path to remove any trailing separators
    path = os.path.normpath(path)

    # Check if directory exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")

    # Check if it's actually a directory
    if not os.path.isdir(path):
        raise OSError(f"Path is not a directory: {path}")

    # Check if directory is empty
    if os.listdir(path):
        raise OSError(f"Directory is not empty: {path}")

    try:
        # Remove the directory
        os.rmdir(path)
    except PermissionError:
        raise OSError(f"Permission denied: Cannot delete directory {path}")
    except Exception as e:
        raise OSError(f"Error deleting directory: {e}")