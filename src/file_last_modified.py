import os
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
        # Get the last modified timestamp
        modified_timestamp = os.path.getmtime(file_path)
        
        # Convert timestamp to datetime object
        return datetime.fromtimestamp(modified_timestamp)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except OSError as e:
        raise OSError(f"Error accessing file {file_path}: {str(e)}")