import pytest
from src.one_char_deletion import can_convert_by_one_deletion

def test_basic_conversion():
    """Test basic one-character deletion conversion"""
    assert can_convert_by_one_deletion('abcd', 'abc') == True
    assert can_convert_by_one_deletion('abcd', 'abd') == True
    assert can_convert_by_one_deletion('abcd', 'acd') == True

def test_no_conversion_possible():
    """Test cases where conversion is not possible"""
    assert can_convert_by_one_deletion('abc', 'abcd') == False  # too short
    assert can_convert_by_one_deletion('abc', 'abc') == False  # same word
    assert can_convert_by_one_deletion('abcd', 'efg') == False  # different chars

def test_edge_cases():
    """Test edge cases"""
    assert can_convert_by_one_deletion('', '') == False  # empty strings
    assert can_convert_by_one_deletion('a', '') == True  # single character
    assert can_convert_by_one_deletion('ab', 'a') == True
    assert can_convert_by_one_deletion('ab', 'b') == True

def test_type_handling():
    """Ensure function handles input types correctly"""
    with pytest.raises(TypeError):
        can_convert_by_one_deletion(None, 'abc')
    with pytest.raises(TypeError):
        can_convert_by_one_deletion('abc', None)