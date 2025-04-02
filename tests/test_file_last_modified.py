import os
import pytest
from datetime import datetime, timedelta
from src.file_last_modified import get_file_last_modified_date

def test_get_file_last_modified_date_existing_file(tmp_path):
    """Test getting last modified date for an existing file."""
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, world!")
    
    # Get the last modified date
    modified_date = get_file_last_modified_date(str(test_file))
    
    # Check that it returns a datetime object
    assert isinstance(modified_date, datetime)
    
    # Check that the date is very recent (within last 5 seconds)
    assert datetime.now() - modified_date < timedelta(seconds=5)

def test_get_file_last_modified_date_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError, match="File not found: non_existent_file.txt"):
        get_file_last_modified_date("non_existent_file.txt")

def test_get_file_last_modified_date_directory(tmp_path):
    """Test that an error is raised when trying to get modified date of a directory."""
    with pytest.raises(OSError, match="Error accessing file: Not a regular file"):
        get_file_last_modified_date(str(tmp_path))

def test_get_file_last_modified_date_permissions(tmp_path):
    """Test handling of files without read permissions."""
    # Create a file and remove read permissions
    test_file = tmp_path / "no_read_file.txt"
    test_file.write_text("No read access")
    test_file.chmod(0o000)  # Remove all permissions
    
    try:
        with pytest.raises(OSError, match="Error accessing file: Permission denied"):
            get_file_last_modified_date(str(test_file))
    finally:
        # Restore permissions to avoid cleanup issues
        test_file.chmod(0o644)