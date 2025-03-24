import pytest
import logging
import sys
import io

from src.api_payload_logger import log_api_response_payload_size

# Mock Response Classes to simulate different library responses
class MockRequestsResponse:
    def __init__(self, content):
        self.content = content.encode('utf-8')
        self.text = content

class MockUrllib3Response:
    def __init__(self, body):
        self.body = body.encode('utf-8')

def test_log_api_response_payload_size_requests_response():
    response = MockRequestsResponse("Hello, World!")
    size = log_api_response_payload_size(response)
    assert size == 13

def test_log_api_response_payload_size_urllib3_response():
    response = MockUrllib3Response("Test Payload")
    size = log_api_response_payload_size(response)
    assert size == 12

def test_log_api_response_payload_size_with_custom_logger():
    # Capture log output
    log_capture = io.StringIO()
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(log_capture)
    logger.addHandler(handler)

    response = MockRequestsResponse("Custom Logger Test")
    size = log_api_response_payload_size(response, logger=logger)
    
    log_output = log_capture.getvalue().strip()
    assert "API Response Payload Size: 18 bytes" in log_output
    assert size == 18

def test_log_api_response_payload_size_invalid_input():
    with pytest.raises(TypeError):
        log_api_response_payload_size(None)

def test_log_api_response_payload_size_empty_response():
    response = MockRequestsResponse("")
    size = log_api_response_payload_size(response)
    assert size == 0

def test_unsupported_response_type():
    class UnsupportedResponse:
        pass

    with pytest.raises(ValueError):
        log_api_response_payload_size(UnsupportedResponse())