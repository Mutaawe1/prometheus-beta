import random
import re
import time

class VerificationCodeGenerator:
    """
    A class to generate and validate unique 6-digit verification codes.
    
    Attributes:
        _generated_codes (set): A set to keep track of generated codes to ensure uniqueness.
        _code_lifetime (int): Lifetime of a verification code in seconds.
    """
    
    def __init__(self, code_lifetime=600):  # Default lifetime of 10 minutes
        """
        Initialize the VerificationCodeGenerator.
        
        Args:
            code_lifetime (int, optional): Lifetime of a verification code in seconds. Defaults to 600.
        """
        self._generated_codes = set()
        self._code_lifetime = code_lifetime
        self._code_timestamps = {}
    
    def generate_code(self) -> str:
        """
        Generate a unique 6-digit verification code.
        
        Returns:
            str: A unique 6-digit verification code.
        """
        while True:
            # Generate a 6-digit code as a string
            code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            
            # Ensure code is unique
            if code not in self._generated_codes:
                self._generated_codes.add(code)
                self._code_timestamps[code] = time.time()
                return code
    
    def validate_code(self, code: str) -> bool:
        """
        Validate a verification code.
        
        Args:
            code (str): The code to validate.
        
        Returns:
            bool: True if the code is valid, False otherwise.
        """
        # Check if code is a 6-digit string
        if not re.match(r'^\d{6}$', code):
            return False
        
        # Check if code was generated
        if code not in self._generated_codes:
            return False
        
        # Check code lifetime
        current_time = time.time()
        code_time = self._code_timestamps.get(code, 0)
        
        if current_time - code_time > self._code_lifetime:
            # Remove expired code
            self._generated_codes.discard(code)
            del self._code_timestamps[code]
            return False
        
        # Remove used code
        self._generated_codes.discard(code)
        del self._code_timestamps[code]
        return True