def get_unique_coordinate_combinations(coordinates):
    """
    Generate a list of unique x and y coordinate combinations in ascending order.

    Args:
        coordinates (list): A list of coordinate pairs, where each pair is a tuple/list of (x, y)

    Returns:
        list: A sorted list of unique coordinate combinations

    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
        ValueError: If coordinate pairs are not valid (must be of length 2)
    """
    # Validate input
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate coordinate pairs
    for coord in coordinates:
        if not isinstance(coord, (list, tuple)) or len(coord) != 2:
            raise ValueError("Each coordinate must be a pair (x, y)")
        if not all(isinstance(val, (int, float)) for val in coord):
            raise TypeError("Coordinate values must be numeric")
    
    # Extract unique x and y values, sort them
    x_values = sorted(set(coord[0] for coord in coordinates))
    y_values = sorted(set(coord[1] for coord in coordinates))
    
    # Create unique combinations
    unique_combinations = [(x, y) for x in x_values for y in y_values]
    
    return unique_combinations