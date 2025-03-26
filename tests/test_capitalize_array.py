import pytest
from src.capitalize_array import capitalize_strings

def test_capitalize_normal_strings():
    """Test capitalizing a list of normal strings."""
    input_array = ["hello", "world", "python"]
    expected = ["Hello", "World", "Python"]
    assert capitalize_strings(input_array) == expected

def test_capitalize_empty_list():
    """Test capitalizing an empty list."""
    assert capitalize_strings([]) == []

def test_capitalize_already_capitalized():
    """Test list with already capitalized strings."""
    input_array = ["Hello", "World"]
    assert capitalize_strings(input_array) == ["Hello", "World"]

def test_capitalize_mixed_case():
    """Test list with mixed case strings."""
    input_array = ["hElLo", "wORlD"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_array) == expected

def test_input_not_list():
    """Test that function raises TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        capitalize_strings("not a list")

def test_non_string_elements():
    """Test that function raises TypeError for non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        capitalize_strings(["hello", 123, "world"])

def test_single_char_strings():
    """Test capitalizing single character strings."""
    input_array = ["a", "b", "c"]
    expected = ["A", "B", "C"]
    assert capitalize_strings(input_array) == expected