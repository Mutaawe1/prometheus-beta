import pytest
import requests
from unittest.mock import patch
from src.http_utils import send_http_get_request

def test_successful_get_request():
    """Test a successful HTTP GET request."""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "Success"
        mock_response.headers = {'content-type': 'application/json'}
        mock_response.json.return_value = {"key": "value"}

        result = send_http_get_request('https://example.com')
        
        assert result['status_code'] == 200
        assert result['text'] == "Success"
        assert result['json'] == {"key": "value"}

def test_invalid_url_error():
    """Test handling of invalid URL."""
    with pytest.raises(ValueError):
        send_http_get_request('')

def test_request_with_headers_and_params():
    """Test GET request with custom headers and parameters."""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200

        headers = {'Authorization': 'Bearer token'}
        params = {'key1': 'value1', 'key2': 'value2'}

        send_http_get_request('https://example.com', headers=headers, params=params)
        
        mock_get.assert_called_once_with(
            'https://example.com', 
            headers=headers, 
            params=params, 
            timeout=10
        )

def test_request_network_error():
    """Test handling of network-related exceptions."""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.ConnectionError("Network error")

        with pytest.raises(requests.ConnectionError):
            send_http_get_request('https://example.com')

def test_non_json_response():
    """Test handling of non-JSON response."""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "Plain text response"
        mock_response.headers = {'content-type': 'text/plain'}
        mock_response.json.side_effect = ValueError

        result = send_http_get_request('https://example.com')
        
        assert result['json'] is None
        assert result['text'] == "Plain text response"

def test_http_error_response():
    """Test handling of HTTP error responses."""
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("Not Found")

        with pytest.raises(requests.HTTPError):
            send_http_get_request('https://example.com')