import os
import stat
from datetime import datetime

def get_file_last_modified_date(file_path):
    """
    Get the last modified date of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        datetime: The last modified datetime of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there's an error accessing the file.
    """
    try:
        # Normalize the path to resolve any relative paths
        normalized_path = os.path.abspath(file_path)
        
        # Directly check for file existence to 
        # trigger the correct FileNotFoundError
        if not os.path.exists(normalized_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Check if it's a regular file
        if not os.path.isfile(normalized_path):
            raise OSError(f"Error accessing file: Not a regular file - {file_path}")
        
        # Check file permissions
        file_stats = os.stat(normalized_path)
        if not bool(file_stats.st_mode & stat.S_IRUSR):
            raise PermissionError("No read permission")
        
        # Get the last modified timestamp
        modified_timestamp = os.path.getmtime(normalized_path)
        
        # Convert timestamp to datetime object
        return datetime.fromtimestamp(modified_timestamp)
    except FileNotFoundError:
        raise
    except PermissionError:
        raise OSError(f"Error accessing file: Permission denied - {file_path}")
    except Exception as e:
        raise OSError(f"Error accessing file: {str(e)}")