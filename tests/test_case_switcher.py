import pytest
from src.case_switcher import switch_cases

def test_switch_cases_basic():
    """Test basic case switching"""
    assert switch_cases("HeLLo", "World") == "hEllO"

def test_switch_cases_all_upper():
    """Test string with all uppercase characters"""
    assert switch_cases("HELLO", "World") == "hello"

def test_switch_cases_all_lower():
    """Test string with all lowercase characters"""
    assert switch_cases("hello", "World") == "HELLO"

def test_switch_cases_mixed_case():
    """Test mixed case input"""
    assert switch_cases("HeLLo WoRLD", "Test") == "hEllO wOrld"

def test_switch_cases_empty_string():
    """Test empty string input"""
    assert switch_cases("", "Test") == ""

def test_switch_cases_non_alphabetic():
    """Test string with non-alphabetic characters"""
    assert switch_cases("H3ll0!", "Test") == "h3LL0!"

def test_switch_cases_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        switch_cases(123, "Test")
    
    with pytest.raises(TypeError):
        switch_cases("Hello", 456)
    
    with pytest.raises(TypeError):
        switch_cases(None, None)