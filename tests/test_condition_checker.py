import pytest
from src.condition_checker import check_conditions

def test_single_valid_condition():
    """Test that a single valid condition passes without raising an assertion error."""
    check_conditions((5 > 3, "5 should be greater than 3"))

def test_multiple_valid_conditions():
    """Test that multiple valid conditions pass without raising an assertion error."""
    check_conditions(
        (10 > 5, "10 should be greater than 5"),
        (len([1,2,3]) == 3, "List should have 3 elements")
    )

def test_invalid_condition_single():
    """Test that an invalid condition raises an AssertionError with the correct message."""
    with pytest.raises(AssertionError, match="5 should be less than 3"):
        check_conditions((5 < 3, "5 should be less than 3"))

def test_invalid_condition_in_multiple():
    """Test that an invalid condition in a set of conditions raises an AssertionError."""
    with pytest.raises(AssertionError, match="10 should be less than 5"):
        check_conditions(
            (5 > 3, "5 should be greater than 3"),
            (10 < 5, "10 should be less than 5")
        )

def test_empty_conditions_input():
    """Test that providing no conditions raises an AssertionError."""
    with pytest.raises(AssertionError, match="At least one condition must be provided"):
        check_conditions()

def test_invalid_condition_format():
    """Test that invalid condition format raises an AssertionError."""
    with pytest.raises(AssertionError, match="Each condition must be a tuple of"):
        check_conditions("invalid")

def test_invalid_condition_format_with_wrong_tuple_length():
    """Test that a condition tuple with incorrect length raises an AssertionError."""
    with pytest.raises(AssertionError, match="Each condition must be a tuple of"):
        check_conditions((True,))