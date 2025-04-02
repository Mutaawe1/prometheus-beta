def run_length_encode(data):
    """
    Implement Run-Length Encoding (RLE) compression.
    
    Args:
        data (str or list): Input data to be compressed
    
    Returns:
        str or list: Compressed data using Run-Length Encoding
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input is an empty string or list
    """
    # Validate input
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    # Raise ValueError for empty inputs
    if len(data) == 0:
        raise ValueError("Input cannot be empty")
    
    # If input is a string, convert to list of characters
    if isinstance(data, str):
        data = list(data)
    
    # Perform Run-Length Encoding
    compressed = []
    current_item = data[0]
    count = 1
    
    for item in data[1:]:
        if item == current_item:
            count += 1
        else:
            compressed.append((current_item, count))
            current_item = item
            count = 1
    
    # Add the last run
    compressed.append((current_item, count))
    
    return compressed

def run_length_decode(compressed_data):
    """
    Decode Run-Length Encoded data.
    
    Args:
        compressed_data (list): Compressed data as list of (item, count) tuples
    
    Returns:
        list: Decoded data
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If tuples are not in correct format or input is empty
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of (item, count) tuples")
    
    # Raise ValueError for empty inputs
    if len(compressed_data) == 0:
        raise ValueError("Input cannot be empty")
    
    # Decode the compressed data
    decoded = []
    for item, count in compressed_data:
        if not isinstance(count, int) or count < 1:
            raise ValueError(f"Invalid count: {count}. Count must be a positive integer.")
        decoded.extend([item] * count)
    
    return decoded