import os
import pytest
import stat
import tempfile

from src.file_permissions import change_file_permissions

def test_change_file_permissions_success():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Initially set a default permission
        os.chmod(temp_path, 0o644)
        
        # Change permissions to read-only
        result = change_file_permissions(temp_path, 0o444)
        assert result is True
        
        # Verify the new permissions
        current_mode = stat.S_IMODE(os.stat(temp_path).st_mode)
        assert current_mode == 0o444
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_change_file_permissions_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        change_file_permissions('/path/to/nonexistent/file.txt', 0o666)

def test_change_file_permissions_invalid_mode():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test invalid mode (too large)
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, 0o1000)
        
        # Test invalid mode (negative)
        with pytest.raises(ValueError):
            change_file_permissions(temp_path, -1)
    finally:
        os.unlink(temp_path)

def test_change_file_permissions_invalid_input_types():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Test invalid file path type
        with pytest.raises(TypeError):
            change_file_permissions(123, 0o666)
        
        # Test invalid mode type
        with pytest.raises(TypeError):
            change_file_permissions(temp_path, '666')
    finally:
        os.unlink(temp_path)

def test_change_file_permissions_handles_relative_paths():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Create a relative path to the temp file
        current_dir = os.getcwd()
        relative_path = os.path.relpath(temp_path, current_dir)
        
        # Change permissions using the relative path
        result = change_file_permissions(relative_path, 0o555)
        assert result is True
        
        # Verify the new permissions
        current_mode = stat.S_IMODE(os.stat(temp_path).st_mode)
        assert current_mode == 0o555
    finally:
        os.unlink(temp_path)