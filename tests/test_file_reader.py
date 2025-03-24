"""
Tests for the file_reader module.
"""

import os
import pytest
from src.file_reader import read_text_file

def test_read_existing_file(tmp_path):
    """Test reading an existing text file."""
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!"
    test_file.write_text(test_content)

    # Read the file
    result = read_text_file(str(test_file))
    assert result == test_content

def test_read_empty_file(tmp_path):
    """Test reading an empty file."""
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()

    # Read the file
    result = read_text_file(str(test_file))
    assert result == ""

def test_read_nonexistent_file():
    """Test reading a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError, match="does not exist"):
        read_text_file("nonexistent_file.txt")

def test_read_file_with_unicode(tmp_path):
    """Test reading a file with unicode characters."""
    # Create a file with unicode content
    test_file = tmp_path / "unicode_file.txt"
    test_content = "こんにちは World! 🌍"
    test_file.write_text(test_content, encoding='utf-8')

    # Read the file
    result = read_text_file(str(test_file))
    assert result == test_content