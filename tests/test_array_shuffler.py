import pytest
import random
from src.array_shuffler import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of a list of integers."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Verify shuffled list has same elements as original
    assert sorted(shuffled) == sorted(original)
    
    # Verify shuffled list is not identical to original 
    # (unless by very rare chance)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty list."""
    assert shuffle_array([]) == []

def test_shuffle_array_single_element():
    """Test shuffling a list with a single element."""
    single_elem = [42]
    assert shuffle_array(single_elem) == single_elem

def test_shuffle_array_multiple_types():
    """Test shuffling a list with multiple types of elements."""
    mixed_list = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(mixed_list)
    
    # Verify shuffled list has same elements as original
    assert sorted(shuffled, key=str) == sorted(mixed_list, key=str)

def test_shuffle_array_randomness():
    """Test the randomness of shuffling by running multiple shuffles."""
    original = list(range(10))
    
    # Collect multiple shuffled results
    shuffled_results = [shuffle_array(original) for _ in range(100)]
    
    # Verify that not all shuffles are the same
    unique_shuffles = set(tuple(shuffle) for shuffle in shuffled_results)
    assert len(unique_shuffles) > 1

def test_shuffle_array_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(None)