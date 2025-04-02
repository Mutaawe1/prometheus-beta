import os
import pytest
from src.file_string_replacer import replace_string_in_file

def test_basic_string_replacement(tmp_path):
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello world, hello python")
    
    # Replace string
    replacements = replace_string_in_file(str(test_file), "hello", "goodbye")
    
    # Check results
    assert replacements == 2
    assert test_file.read_text() == "Hello world, goodbye python"

def test_case_sensitive_replacement(tmp_path):
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello HELLO hello")
    
    # Replace string
    replacements = replace_string_in_file(str(test_file), "hello", "hi")
    
    # Check results
    assert replacements == 1
    assert test_file.read_text() == "Hello HELLO hi"

def test_no_replacements(tmp_path):
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Original content")
    
    # Try to replace non-existent string
    replacements = replace_string_in_file(str(test_file), "missing", "replacement")
    
    # Check results
    assert replacements == 0
    assert test_file.read_text() == "Original content"

def test_empty_new_string(tmp_path):
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello world")
    
    # Replace with empty string
    replacements = replace_string_in_file(str(test_file), "world", "")
    
    # Check results
    assert replacements == 1
    assert test_file.read_text() == "Hello "

def test_file_not_found():
    # Attempt to replace in non-existent file
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("non_existent_file.txt", "old", "new")

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "new")
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "old", 123)

def test_empty_old_string(tmp_path):
    # Attempt to replace with empty old string
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello world")
    
    with pytest.raises(ValueError):
        replace_string_in_file(str(test_file), "", "new")