def process_array(numbers):
    """
    Process an array of numbers by:
    1. Multiplying every third number by 2
    2. Finding the sum of all even numbers, excluding the modified numbers

    Args:
        numbers (list): A list of numbers to process

    Returns:
        int: Sum of even numbers, excluding modified numbers

    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric elements
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numeric")
    
    # Create a copy of the input list to avoid modifying the original
    processed_numbers = numbers.copy()
    
    # Modify every third number
    for i in range(2, len(processed_numbers), 3):
        processed_numbers[i] *= 2
    
    # Sum even numbers, excluding modified numbers
    even_sum = sum(
        num for i, num in enumerate(numbers) 
        if num % 2 == 0 and (i % 3 != 2 or num * 2 != processed_numbers[i])
    )
    
    return even_sum