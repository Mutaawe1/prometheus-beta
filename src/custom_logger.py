"""
Custom logging module with styled message functionality.

This module provides a flexible logging function that allows custom styling 
of log messages with various color and formatting options.
"""

def log_message(message, color=None, bold=False, italic=False, underline=False):
    """
    Log a message with optional custom styling.

    Args:
        message (str): The message to be logged.
        color (str, optional): Color of the message. 
            Supported colors: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.
        bold (bool, optional): Whether to make the text bold. Defaults to False.
        italic (bool, optional): Whether to make the text italic. Defaults to False.
        underline (bool, optional): Whether to underline the text. Defaults to False.

    Returns:
        str: Formatted log message with ANSI escape codes for styling.

    Raises:
        ValueError: If an unsupported color is provided.
        TypeError: If message is not a string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Define ANSI color codes
    color_codes = {
        'red': '\033[31m',
        'green': '\033[32m', 
        'yellow': '\033[33m',
        'blue': '\033[34m', 
        'magenta': '\033[35m',
        'cyan': '\033[36m', 
        'white': '\033[37m'
    }

    # Validate color
    if color is not None and color.lower() not in color_codes:
        raise ValueError(f"Unsupported color: {color}. Supported colors are: {', '.join(color_codes.keys())}")

    # Initialize styling codes
    style_codes = []
    reset_code = '\033[0m'

    # Add color
    if color:
        style_codes.append(color_codes[color.lower()])

    # Add text formatting
    if bold:
        style_codes.append('\033[1m')
    if italic:
        style_codes.append('\033[3m')
    if underline:
        style_codes.append('\033[4m')

    # Combine styling
    start_style = ''.join(style_codes)
    
    # Return styled message
    return f"{start_style}{message}{reset_code}"