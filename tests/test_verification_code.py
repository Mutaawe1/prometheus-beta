import pytest
import time
from src.verification_code import VerificationCodeGenerator

def test_generate_code():
    """Test that generate_code creates a valid 6-digit code."""
    generator = VerificationCodeGenerator()
    code = generator.generate_code()
    
    # Check code length
    assert len(code) == 6
    
    # Check code contains only digits
    assert code.isdigit()

def test_unique_codes():
    """Test that generated codes are unique."""
    generator = VerificationCodeGenerator()
    codes = set()
    
    # Generate multiple codes
    for _ in range(100):
        code = generator.generate_code()
        assert code not in codes
        codes.add(code)

def test_code_validation():
    """Test code validation process."""
    generator = VerificationCodeGenerator()
    
    # Generate a valid code
    code = generator.generate_code()
    
    # Validate the code
    assert generator.validate_code(code) == True
    
    # Code should be invalid after validation
    assert generator.validate_code(code) == False

def test_invalid_code_formats():
    """Test validation of invalid code formats."""
    generator = VerificationCodeGenerator()
    
    # Test non-digit codes
    assert generator.validate_code('ABCDEF') == False
    assert generator.validate_code('12345') == False
    assert generator.validate_code('1234567') == False
    assert generator.validate_code('') == False

def test_code_expiration():
    """Test code expiration."""
    # Create generator with very short lifetime
    generator = VerificationCodeGenerator(code_lifetime=1)
    
    # Generate code
    code = generator.generate_code()
    
    # Wait for code to expire
    time.sleep(2)
    
    # Validate should return False
    assert generator.validate_code(code) == False