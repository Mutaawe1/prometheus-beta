"""
Test suite for the file_reader module.

This module contains comprehensive tests for the read_text_file function,
covering various scenarios and edge cases.
"""

import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_existing_file():
    """Test reading a valid text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        test_content = "Hello, World!"
        temp_file.write(test_content)
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == test_content
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == ""
        finally:
            os.unlink(temp_file.name)

def test_nonexistent_file():
    """Test reading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("/path/to/nonexistent/file.txt")

def test_invalid_path_type():
    """Test that passing a non-string path raises TypeError."""
    with pytest.raises(TypeError):
        read_text_file(123)

def test_directory_path():
    """Test that passing a directory path raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        read_text_file("/tmp")

def test_utf8_content():
    """Test reading a file with UTF-8 encoded content."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        test_content = "Hello, 世界!"
        temp_file.write(test_content)
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == test_content
        finally:
            os.unlink(temp_file.name)