import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

# ... (previous tests remain the same)

def test_negative_integers():
    """Test a sequence with negative integers."""
    arr = [-5, -3, -1, 0, 2, 4, 6]
    assert longest_increasing_subsequence(arr) == 5

def test_mixed_sign_integers():
    """Test a sequence with mixed positive and negative integers."""
    arr = [-2, 1, -1, 3, -3, 5, 4, 6]
    assert longest_increasing_subsequence(arr) == 4