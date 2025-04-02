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
    # Reset logging to start fresh
    logging.getLogger().handlers.clear()
    
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
        # Configure basic logging to the specific file
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s',
            filemode='w'  # Write mode to overwrite existing content
        )
    else:
        # Stream logging
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(message)s',
            stream=sys.stdout
        )
    
    # Get logger and log the input
    logger = logging.getLogger()
    logger.info(user_input)
    
    return user_input