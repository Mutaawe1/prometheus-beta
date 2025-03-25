import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test valid IP address formats"""
    valid_ips = [
        "1.2.3.4",
        "0.0.0.0",
        "9.9.9.9"
    ]
    for ip in valid_ips:
        assert validate_ip_address(ip) is True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test invalid IP address formats"""
    invalid_ips = [
        # Too few/many parts
        "1.2.3",
        "1.2.3.4.5",
        
        # Non-digit characters
        "a.1.2.3",
        "1.2.3.b",
        
        # Out of range digits
        "-1.2.3.4",
        "1.2.3.10",
        
        # Empty string
        "",
        
        # Non-string input
        None,
        123,
        [1, 2, 3, 4]
    ]
    for ip in invalid_ips:
        assert validate_ip_address(ip) is False, f"{ip} should be invalid"

def test_edge_cases():
    """Test various edge cases"""
    # Whitespace
    assert validate_ip_address(" 1.2.3.4") is False
    assert validate_ip_address("1.2.3.4 ") is False
    
    # Leading zeros
    assert validate_ip_address("01.2.3.4") is False
    
    # Special characters
    assert validate_ip_address("1.2.3.4!") is False
    assert validate_ip_address("1!2.3.4") is False