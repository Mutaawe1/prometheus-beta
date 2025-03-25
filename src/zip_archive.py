import os
import zipfile
from typing import List, Union


def create_zip_archive(files: List[str], archive_path: str) -> bool:
    """
    Create a zip archive containing multiple files.

    Args:
        files (List[str]): List of file paths to be added to the archive
        archive_path (str): Path where the zip archive will be created

    Returns:
        bool: True if archive creation is successful, False otherwise

    Raises:
        ValueError: If no files are provided or archive path is invalid
        FileNotFoundError: If any of the source files do not exist
    """
    # Validate input
    if not files:
        raise ValueError("At least one file must be provided")
    
    # Validate archive path
    if not archive_path.lower().endswith('.zip'):
        archive_path += '.zip'
    
    # Ensure directory exists for archive
    os.makedirs(os.path.dirname(archive_path) or '.', exist_ok=True)

    try:
        # Create zip archive
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add each file to the archive
            for file_path in files:
                # Check if file exists
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File not found: {file_path}")
                
                # Add file to archive, preserving directory structure
                zipf.write(file_path, os.path.basename(file_path))
        
        return True
    except Exception as e:
        # Log or handle any unexpected errors
        print(f"Error creating zip archive: {e}")
        return False