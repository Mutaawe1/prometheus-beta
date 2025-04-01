import pytest
from src.word_counter import count_words

def test_count_words_normal_case():
    """Test counting words in a normal sentence."""
    assert count_words("Hello world") == 2

def test_count_words_multiple_spaces():
    """Test handling multiple spaces between words."""
    assert count_words("Hello   world  test") == 3

def test_count_words_leading_trailing_spaces():
    """Test handling leading and trailing spaces."""
    assert count_words("  Hello world  ") == 2

def test_count_words_empty_string():
    """Test empty string returns zero words."""
    assert count_words("") == 0

def test_count_words_whitespace_only():
    """Test string with only whitespace returns zero words."""
    assert count_words("   \t\n  ") == 0

def test_count_words_none_input():
    """Test None input returns zero words."""
    assert count_words(None) == 0

def test_count_words_single_word():
    """Test single word input."""
    assert count_words("Hello") == 1

def test_count_words_complex_whitespace():
    """Test handling complex whitespace scenarios."""
    assert count_words("Hello \t world\n test") == 3