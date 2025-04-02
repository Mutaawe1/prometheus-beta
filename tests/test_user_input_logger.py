import os
import pytest
import logging
import sys
from io import StringIO
from src.user_input_logger import log_user_input

def test_log_user_input_default_logging(monkeypatch, caplog):
    """Test logging to default stream (stdout)"""
    # Capture stdout
    captured_output = StringIO()
    monkeypatch.setattr(sys, 'stdout', captured_output)
    
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda: "Test input")
    
    # Capture logging
    caplog.set_level(logging.INFO)
    
    # Run the function
    result = log_user_input()
    
    # Verify
    assert result == "Test input"
    
    # Check stdout
    captured_output.seek(0)
    stdout_content = captured_output.read()
    assert "Test input" in stdout_content

def test_log_user_input_to_file(tmp_path, monkeypatch):
    """Test logging to a specific file"""
    # Create a temp log file path
    log_file = str(tmp_path / "user_input.log")
    
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda: "Logged to file")
    
    # Run the function
    result = log_user_input(log_file)
    
    # Verify
    assert result == "Logged to file"
    
    # Check file contents
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert "Logged to file" in log_content

def test_log_user_input_empty_input(monkeypatch):
    """Test handling of empty input"""
    # Simulate empty input
    monkeypatch.setattr('builtins.input', lambda: "")
    
    # Expect ValueError
    with pytest.raises(ValueError, match="Input cannot be empty"):
        log_user_input()

def test_log_user_input_whitespace_input(monkeypatch):
    """Test handling of whitespace-only input"""
    # Simulate whitespace input
    monkeypatch.setattr('builtins.input', lambda: "   ")
    
    # Expect ValueError
    with pytest.raises(ValueError, match="Input cannot be empty"):
        log_user_input()