"""
Tests for the file_writer module.
"""

import os
import pytest
import tempfile

from src.file_writer import write_string_to_file


def test_write_string_to_file_success():
    """Test successful file writing."""
    # Create a temporary file
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = os.path.join(tempdir, 'test_file.txt')
        test_content = "Hello, World!"
        
        # Write to file
        write_string_to_file(test_file, test_content)
        
        # Verify file contents
        with open(test_file, 'r') as file:
            assert file.read() == test_content


def test_write_string_to_file_empty_file():
    """Test writing to an empty file."""
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = os.path.join(tempdir, 'empty_file.txt')
        test_content = ""
        
        write_string_to_file(test_file, test_content)
        
        with open(test_file, 'r') as file:
            assert file.read() == ""


def test_write_string_to_file_non_english_characters():
    """Test writing file with non-English characters."""
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = os.path.join(tempdir, 'unicode_file.txt')
        test_content = "こんにちは Здравствуйте ✓"
        
        write_string_to_file(test_file, test_content)
        
        with open(test_file, 'r', encoding='utf-8') as file:
            assert file.read() == test_content


def test_write_string_to_file_nested_directory():
    """Test writing to a nested directory."""
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = os.path.join(tempdir, 'nested', 'dir', 'test_file.txt')
        test_content = "Nested directory test"
        
        write_string_to_file(test_file, test_content)
        
        assert os.path.exists(test_file)
        with open(test_file, 'r') as file:
            assert file.read() == test_content


def test_write_string_to_file_invalid_input_types():
    """Test error handling for invalid input types."""
    with tempfile.TemporaryDirectory() as tempdir:
        test_file = os.path.join(tempdir, 'test_file.txt')
        
        # Test non-string file path
        with pytest.raises(TypeError, match="file_path must be a string"):
            write_string_to_file(123, "content")
        
        # Test non-string content
        with pytest.raises(TypeError, match="content must be a string"):
            write_string_to_file(test_file, 123)


def test_write_string_to_file_empty_path():
    """Test error handling for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("   ", "content")
        write_string_to_file("", "content")