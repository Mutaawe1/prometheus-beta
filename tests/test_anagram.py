import pytest
from src.anagram import isAnagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert isAnagram("listen", "silent") == True
    assert isAnagram("triangle", "integral") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert isAnagram("hello", "world") == False
    assert isAnagram("python", "java") == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert isAnagram("Debit Card", "Bad Credit") == True
    assert isAnagram("Astronomer", "Moon starer") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert isAnagram("rail safety", "fairy tales") == True
    assert isAnagram("   listen", "silent   ") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert isAnagram("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert isAnagram("abc", "abcd") == False
    assert isAnagram("a", "") == False

def test_unicode_characters():
    """Test with unicode characters"""
    assert isAnagram("résumé", "sumére") == True

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert isAnagram("aab", "aba") == True
    assert isAnagram("aab", "abc") == False