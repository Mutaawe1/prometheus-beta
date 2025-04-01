import pytest
from src.edit_distance import edit_distance

def test_identical_strings():
    """Test edit distance between identical strings"""
    assert edit_distance("hello", "hello") == 0

def test_completely_different_strings():
    """Test edit distance between completely different strings"""
    assert edit_distance("kitten", "sitting") == 3

def test_empty_strings():
    """Test edit distance involving empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_single_character_differences():
    """Test edit distance with single character differences"""
    assert edit_distance("cat", "cut") == 1
    assert edit_distance("cat", "bat") == 1
    assert edit_distance("cat", "car") == 1

def test_multiple_character_changes():
    """Test edit distance with multiple character changes"""
    assert edit_distance("sunday", "saturday") == 3

def test_case_sensitivity():
    """Test edit distance is case-sensitive"""
    assert edit_distance("Hello", "hello") == 1

def test_type_errors():
    """Test type error handling"""
    with pytest.raises(TypeError):
        edit_distance(123, "hello")
    
    with pytest.raises(TypeError):
        edit_distance("hello", [1, 2, 3])
    
    with pytest.raises(TypeError):
        edit_distance(None, "test")

def test_unicode_strings():
    """Test edit distance with unicode strings"""
    assert edit_distance("café", "cafe") == 1
    assert edit_distance("résumé", "resume") == 2