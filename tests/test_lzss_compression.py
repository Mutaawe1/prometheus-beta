"""
Test suite for LZSS compression algorithm.

This test suite covers various scenarios including:
- Basic compression and decompression
- Edge cases
- Error handling
"""

import pytest
import random
import string
from src.lzss_compression import LZSSCompressor

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string."""
    compressor = LZSSCompressor()
    test_string = "Hello, World! Hello, World!"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_repeated_pattern_compression():
    """Test compression of a string with many repeated patterns."""
    compressor = LZSSCompressor()
    test_string = "ABCABCABCABCABCABC" * 10
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_random_bytes_compression():
    """Test compression of random bytes."""
    compressor = LZSSCompressor()
    
    # Generate random bytes
    random.seed(42)
    test_bytes = bytes(random.randint(0, 255) for _ in range(1000))
    
    # Compress
    compressed = compressor.compress(test_bytes)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed == test_bytes

def test_empty_input():
    """Test compression and decompression of empty input."""
    compressor = LZSSCompressor()
    test_string = ""
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_long_input():
    """Test compression of a very long input with some repetition."""
    compressor = LZSSCompressor()
    test_string = ''.join(random.choices(string.ascii_letters, k=10000))
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    compressor = LZSSCompressor()
    
    # Test compress
    with pytest.raises(TypeError):
        compressor.compress(123)
    
    # Test decompress
    with pytest.raises(TypeError):
        compressor.decompress(123)

def test_invalid_compressed_data():
    """Test error handling for invalid compressed data."""
    compressor = LZSSCompressor()
    
    # Malformed compressed data
    with pytest.raises(ValueError):
        compressor.decompress(bytes([0, 1, 2]))  # Incomplete data
    
    with pytest.raises(ValueError):
        compressor.decompress(bytes([2, 1, 2]))  # Invalid flag byte

def test_custom_window_size():
    """Test compression with a custom window size."""
    compressor = LZSSCompressor(window_size=128, min_match_length=2)
    test_string = "ABCABCABCABCABCABC" * 10
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    # Verify
    assert decompressed.decode('utf-8') == test_string