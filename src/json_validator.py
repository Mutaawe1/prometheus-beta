import json

def is_valid_json(json_string: str) -> bool:
    """
    Check if a given string is a valid JSON.

    Args:
        json_string (str): The string to validate as JSON.

    Returns:
        bool: True if the string is valid JSON, False otherwise.
    """
    try:
        # Attempt to parse the string as JSON
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        # Return False for invalid JSON or non-string inputs
        return False