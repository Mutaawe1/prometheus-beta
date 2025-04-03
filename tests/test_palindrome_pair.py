import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(11) == True
    assert is_palindrome(121) == True
    assert is_palindrome(12) == False
    assert is_palindrome(0) == True
    assert is_palindrome(1) == True

def test_palindrome_pair_basic_cases():
    """Test basic scenarios of palindrome pair function."""
    # Note: the function checks ALL possible pairs
    # Pairs with palindrome differences
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # pairs like 3-2 = 1 is a palindrome
    assert palindrome_pair([10, 20, 30, 40]) == False  # no palindrome differences in this case
    
    # No palindrome difference pairs
    assert palindrome_pair([2, 4, 6, 8]) == False

def test_palindrome_pair_edge_cases():
    """Test edge cases for palindrome pair function."""
    # Empty list
    assert palindrome_pair([]) == False
    
    # Single element list
    assert palindrome_pair([1]) == False
    
    # List with repeated elements
    assert palindrome_pair([1, 1, 2, 2]) == True  # 1-1 = 0 is a palindrome

def test_palindrome_pair_error_handling():
    """Test error handling for invalid inputs."""
    # Non-list input
    with pytest.raises(TypeError):
        palindrome_pair("not a list")
    
    # List with non-integer elements
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, "3", 4])
    with pytest.raises(ValueError):
        palindrome_pair([1.5, 2.5, 3.5])

def test_palindrome_pair_large_numbers():
    """Test palindrome pair function with larger numbers."""
    assert palindrome_pair([11, 22, 33, 44, 55]) == True  # multiple palindrome differences
    assert palindrome_pair([1000, 2000, 3000, 4000]) == False  # no palindrome differences