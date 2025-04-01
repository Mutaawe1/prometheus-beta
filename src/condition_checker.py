def check_conditions(*conditions):
    """
    Validate multiple conditions using assert statements.
    
    Args:
        *conditions (tuple): A variable number of conditions to check.
                             Each condition should be a tuple of (condition, error_message).
    
    Raises:
        AssertionError: If any of the provided conditions evaluate to False.
    
    Examples:
        >>> check_conditions((5 > 3, "5 should be greater than 3"))
        >>> check_conditions(
        ...     (10 > 5, "10 should be greater than 5"),
        ...     (len([1,2,3]) == 3, "List should have 3 elements")
        ... )
    """
    # Validate input is not empty
    assert conditions, "At least one condition must be provided"
    
    # Check each condition
    for condition in conditions:
        # Validate condition input format
        assert isinstance(condition, tuple) and len(condition) == 2, \
            "Each condition must be a tuple of (condition, error_message)"
        
        # Unpack the condition and error message
        check, error_message = condition
        
        # Perform the assertion
        assert check, error_message