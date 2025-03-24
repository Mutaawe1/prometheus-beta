"""
Test suite for the custom logger module.

This module contains comprehensive tests for the log_message function 
to ensure it handles various input scenarios correctly.
"""

import pytest
from src.custom_logger import log_message

def test_basic_message():
    """Test basic logging without any styling."""
    result = log_message("Hello, World!")
    assert "Hello, World!" in result

def test_color_logging():
    """Test logging with different colors."""
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in colors:
        result = log_message("Test", color=color)
        assert f"\033[{colors.index(color)+31}m" in result

def test_bold_logging():
    """Test bold text styling."""
    result = log_message("Bold Text", bold=True)
    assert "\033[1m" in result

def test_italic_logging():
    """Test italic text styling."""
    result = log_message("Italic Text", italic=True)
    assert "\033[3m" in result

def test_underline_logging():
    """Test underline text styling."""
    result = log_message("Underlined Text", underline=True)
    assert "\033[4m" in result

def test_combined_styling():
    """Test multiple styling options together."""
    result = log_message("Combined Style", color='blue', bold=True, italic=True)
    assert "\033[34m" in result  # Blue color
    assert "\033[1m" in result   # Bold
    assert "\033[3m" in result   # Italic

def test_invalid_color():
    """Test that an invalid color raises a ValueError."""
    with pytest.raises(ValueError, match="Unsupported color"):
        log_message("Invalid Color", color="purple")

def test_non_string_input():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(123)

def test_none_message():
    """Test handling of None message input."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(None)

def test_empty_string():
    """Test logging an empty string."""
    result = log_message("")
    assert result == "\033[0m"