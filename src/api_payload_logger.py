import logging
import sys
from typing import Any, Optional, Union

def log_api_response_payload_size(
    response: Any, 
    logger: Optional[logging.Logger] = None, 
    log_level: int = logging.INFO
) -> int:
    """
    Log the size of an API response payload.

    Args:
        response: The API response object to measure. Can be from various HTTP libraries.
        logger: Optional custom logger. If None, uses root logger.
        log_level: Logging level (default is logging.INFO)

    Returns:
        int: Size of the payload in bytes

    Raises:
        TypeError: If response is None or cannot be measured
        ValueError: If payload size cannot be determined
    """
    # Validate input
    if response is None:
        raise TypeError("Response cannot be None")

    # Attempt to get payload size through different methods
    payload_size = 0
    try:
        # Try method 1: Check for .content (requests library)
        if hasattr(response, 'content'):
            payload_size = len(response.content)
        
        # Try method 2: Check for .text (requests library)
        elif hasattr(response, 'text'):
            payload_size = len(response.text.encode('utf-8'))
        
        # Try method 3: Check for .body (urllib3)
        elif hasattr(response, 'body'):
            payload_size = len(response.body)
        
        # Try method 4: Raw data if available
        elif hasattr(response, 'data'):
            payload_size = len(response.data)
        
        else:
            raise ValueError("Unable to determine payload size")

    except Exception as e:
        raise ValueError(f"Error measuring payload size: {str(e)}")

    # Use provided logger or root logger
    log = logger or logging.getLogger()
    log.log(log_level, f"API Response Payload Size: {payload_size} bytes")

    return payload_size