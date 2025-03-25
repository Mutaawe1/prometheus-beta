import os
import pytest
import tempfile
import shutil

from src.directory_utils import delete_empty_directory

def test_delete_empty_directory():
    """Test deleting an empty directory successfully."""
    with tempfile.TemporaryDirectory() as temp_dir:
        delete_empty_directory(temp_dir)
        assert not os.path.exists(temp_dir)

def test_delete_empty_directory_nested():
    """Test deleting an empty nested directory."""
    with tempfile.TemporaryDirectory() as base_dir:
        nested_dir = os.path.join(base_dir, 'nested')
        os.makedirs(nested_dir)
        delete_empty_directory(nested_dir)
        assert not os.path.exists(nested_dir)

def test_delete_non_existent_directory():
    """Test deleting a non-existent directory raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as base_dir:
        non_existent_path = os.path.join(base_dir, 'non_existent')
        with pytest.raises(FileNotFoundError):
            delete_empty_directory(non_existent_path)

def test_delete_non_empty_directory():
    """Test deleting a non-empty directory raises OSError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('test')
        
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(temp_dir)

def test_delete_file_instead_of_directory():
    """Test attempting to delete a file instead of a directory raises OSError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('test')
        
        with pytest.raises(OSError, match="Path is not a directory"):
            delete_empty_directory(file_path)