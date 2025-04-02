import pytest
from src.vowel_cipher import replace_vowels

def test_replace_vowels_lowercase():
    """Test replacing lowercase vowels"""
    assert replace_vowels("hello") == "holli"
    assert replace_vowels("python") == "pythin"
    assert replace_vowels("aeiou") == "eioua"

def test_replace_vowels_uppercase():
    """Test replacing uppercase vowels"""
    assert replace_vowels("HELLO") == "HOLLI"
    assert replace_vowels("PYTHON") == "PYTHIN"
    assert replace_vowels("AEIOU") == "EIOUA"

def test_replace_vowels_mixed_case():
    """Test replacing vowels in mixed case strings"""
    assert replace_vowels("Hello World") == "Holli Wirld"
    assert replace_vowels("AeIoU") == "EiOuA"

def test_replace_vowels_no_vowels():
    """Test strings with no vowels"""
    assert replace_vowels("rhythm") == "rhythm"
    assert replace_vowels("123!@#") == "123!@#"

def test_replace_vowels_empty_string():
    """Test empty string"""
    assert replace_vowels("") == ""

def test_replace_vowels_special_characters():
    """Test strings with special characters and vowels"""
    assert replace_vowels("h3ll0!") == "h3lli!"
    assert replace_vowels("a@e#i$o%u") == "e@i#o$u%a"