import sys
import logging
import os
from typing import Optional, TextIO

def log_user_input(log_file: Optional[str] = None) -> str:
    """
    Capture and log user input from the command line.
    
    Args:
        log_file (Optional[str]): Path to the log file. If None, uses default logging.
    
    Returns:
        str: The user input that was logged
    
    Raises:
        ValueError: If input is empty or contains only whitespace
    """
    # Ensure logging directory exists
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Prompt and capture user input
    print("Please enter your input:")
    user_input = input().strip()
    
    # Validate input
    if not user_input:
        raise ValueError("Input cannot be empty")
    
    # Configure logging
    if log_file:
        logging.basicConfig(filename=log_file, 
                            level=logging.INFO, 
                            format='%(asctime)s - %(message)s')
        logger = logging.getLogger()
    else:
        logger = logging.getLogger('default_logger')
        logger.setLevel(logging.INFO)
        # Create a stream handler if no file is specified
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(handler)
    
    # Log the input
    logger.info(user_input)
    
    return user_input