import requests
from typing import Dict, Any, Optional

def send_http_get_request(url: str, 
                           headers: Optional[Dict[str, str]] = None, 
                           params: Optional[Dict[str, Any]] = None, 
                           timeout: int = 10) -> Dict[str, Any]:
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The target URL to send the GET request to.
        headers (Optional[Dict[str, str]], optional): Optional headers to include in the request. Defaults to None.
        params (Optional[Dict[str, Any]], optional): Optional query parameters to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        Dict[str, Any]: A dictionary containing the response details.

    Raises:
        ValueError: If the URL is empty or invalid.
        requests.RequestException: For network-related errors or invalid responses.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Send GET request
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=timeout
        )
        
        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return comprehensive response details
        return {
            'status_code': response.status_code,
            'text': response.text,
            'headers': dict(response.headers),
            'json': response.json() if response.headers.get('content-type', '').startswith('application/json') else None
        }

    except requests.RequestException as e:
        # Handle and re-raise network or request-related exceptions
        raise