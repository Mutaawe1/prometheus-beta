import io
import lzma
import pytest
from src.lzma2_compression import compress_lzma2

def test_compress_bytes():
    """Test compression of byte data."""
    input_data = b'Hello, world! This is a test of LZMA2 compression.'
    compressed = compress_lzma2(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)

def test_compress_string():
    """Test compression of string data."""
    input_data = "Hello, world! This is a test of LZMA2 compression."
    compressed = compress_lzma2(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_compress_file_like_object():
    """Test compression of file-like object."""
    input_data = io.BytesIO(b'Hello, world! This is a test of LZMA2 compression.')
    compressed = compress_lzma2(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_compression_levels():
    """Test different compression levels."""
    input_data = b'Hello, world!' * 1000  # Create a larger input
    
    # Test various presets
    results = {}
    for preset in [0, 3, 6, 9]:
        results[preset] = len(compress_lzma2(input_data, preset=preset))
    
    # Verify that higher compression levels generally result in smaller output
    assert results[0] >= results[3]
    assert results[3] >= results[6]
    assert results[6] >= results[9]

def test_empty_input():
    """Test compression of empty input."""
    assert compress_lzma2(b'') == b''
    assert compress_lzma2('') == b''

def test_invalid_preset():
    """Test handling of invalid compression preset."""
    with pytest.raises(ValueError, match="Compression preset must be between 0 and 9"):
        compress_lzma2(b'test', preset=10)
    with pytest.raises(ValueError, match="Compression preset must be between 0 and 9"):
        compress_lzma2(b'test', preset=-1)

def test_unsupported_input_type():
    """Test handling of unsupported input types."""
    with pytest.raises(TypeError, match="Unsupported input type"):
        compress_lzma2(123)
    with pytest.raises(TypeError, match="Unsupported input type"):
        compress_lzma2(None)

def test_different_check_types():
    """Test different integrity check types."""
    input_data = b'Hello, world! This is a test of LZMA2 compression.'
    
    # Test different check types supported by lzma
    checks = [
        lzma.CHECK_NONE,
        lzma.CHECK_CRC32,
        lzma.CHECK_CRC64,
        lzma.CHECK_SHA256
    ]
    
    for check in checks:
        compressed = compress_lzma2(input_data, check=check)
        assert isinstance(compressed, bytes)
        assert len(compressed) > 0