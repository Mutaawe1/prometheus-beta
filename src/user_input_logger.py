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
        os.makedirs(os.path.dirname(log_file) or os.curdir, exist_ok=True)
    
    # Prompt and capture user input
    print("Please enter your input:")
    user_input = input().strip()
    
    # Validate input
    if not user_input:
        raise ValueError("Input cannot be empty")
    
    # Configure logging
    if log_file:
        # Create file handler with full path
        logging.basicConfig(filename=log_file, 
                            level=logging.INFO, 
                            format='%(asctime)s - %(message)s',
                            filemode='a')  # Append mode to ensure file is created
        logger = logging.getLogger()
        
        # Close any existing handlers to prevent duplicate logging
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
            handler.close()
        
        # Add file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(file_handler)
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