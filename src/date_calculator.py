from datetime import datetime, date

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime or date): First date 
        date2 (str or datetime or date): Second date

    Returns:
        int: Number of days between the two dates (absolute value)

    Raises:
        ValueError: If dates cannot be parsed or are invalid
    """
    # Convert inputs to date objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.strptime(date1, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for date1: {date1}. Use YYYY-MM-DD format.")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.strptime(date2, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for date2: {date2}. Use YYYY-MM-DD format.")
    
    # Convert datetime to date if necessary
    if isinstance(date1, datetime):
        date1 = date1.date()
    
    if isinstance(date2, datetime):
        date2 = date2.date()
    
    # Calculate absolute difference in days
    return abs((date2 - date1).days)