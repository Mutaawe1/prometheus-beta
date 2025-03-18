import pytest
from src.list_rotation import rotate_list

def test_basic_rotation():
    """Test basic list rotation."""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test rotation equal to list length."""
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]

def test_partial_rotation():
    """Test partial rotation."""
    assert rotate_list([1, 2, 3, 4], 1) == [4, 1, 2, 3]

def test_zero_rotation():
    """Test rotation of 0 returns original list."""
    original = [1, 2, 3]
    assert rotate_list(original, 0) == original
    assert rotate_list(original, 0) is not original  # Ensure a copy is returned

def test_empty_list():
    """Test rotation of an empty list."""
    assert rotate_list([], 5) == []

def test_rotation_larger_than_list():
    """Test rotation amount larger than list length."""
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_list("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_list([1, 2, 3], "2")

def test_negative_rotation():
    """Test error handling for negative rotation."""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_list([1, 2, 3], -1)