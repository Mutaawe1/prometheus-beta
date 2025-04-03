from typing import List, Tuple

def max_simultaneous_intervals(intervals: List[Tuple[int, int]]) -> int:
    """
    Find the maximum number of intervals that can be scheduled simultaneously.
    
    An interval is represented as a tuple (start, end).
    
    Args:
        intervals (List[Tuple[int, int]]): List of intervals to schedule
    
    Returns:
        int: Maximum number of non-intersecting intervals that can be scheduled
    
    Raises:
        ValueError: If input is None or contains invalid intervals
    """
    # Validate input
    if intervals is None:
        raise ValueError("Input cannot be None")
    
    if not intervals:
        return 0
    
    # Validate each interval
    for start, end in intervals:
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise ValueError("Intervals must contain numeric values")
        if start > end:
            raise ValueError("Invalid interval: start time must be <= end time")
    
    # Sort events by their start and end times
    events = []
    for start, end in intervals:
        events.append((start, 1))  # Start of interval
        events.append((end, -1))   # End of interval
    
    # Sort events to handle overlapping intervals
    events.sort()
    
    max_simultaneous = 0
    current_simultaneous = 0
    
    # Sweep through events to count simultaneous intervals
    for _, change in events:
        current_simultaneous += change
        max_simultaneous = max(max_simultaneous, current_simultaneous)
    
    return max_simultaneous