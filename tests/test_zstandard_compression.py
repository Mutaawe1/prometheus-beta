import os
import pytest
import tempfile
import src.zstandard_compression as zstd_comp

def create_test_file(content):
    """Helper function to create a temporary test file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(content.encode())
        return temp_file.name

def test_compress_file_basic():
    """Test basic file compression functionality."""
    test_content = "Hello, Zstandard compression!"
    input_file = create_test_file(test_content)
    
    try:
        compressed_file = zstd_comp.compress_file(input_file)
        assert os.path.exists(compressed_file)
        assert compressed_file.endswith('.zst')
    finally:
        # Clean up files
        os.unlink(input_file)
        if 'compressed_file' in locals() and os.path.exists(compressed_file):
            os.unlink(compressed_file)

def test_compress_decompress_round_trip():
    """Test compression and decompression round trip."""
    test_content = "Testing Zstandard compression and decompression"
    input_file = create_test_file(test_content)
    
    try:
        # Compress
        compressed_file = zstd_comp.compress_file(input_file)
        
        # Decompress
        decompressed_file = zstd_comp.decompress_file(compressed_file)
        
        # Verify content
        with open(decompressed_file, 'rb') as f:
            assert f.read().decode() == test_content
    finally:
        # Clean up files
        os.unlink(input_file)
        if 'compressed_file' in locals() and os.path.exists(compressed_file):
            os.unlink(compressed_file)
        if 'decompressed_file' in locals() and os.path.exists(decompressed_file):
            os.unlink(decompressed_file)

def test_compress_custom_output():
    """Test compression with custom output path."""
    test_content = "Custom output path test"
    input_file = create_test_file(test_content)
    custom_output = input_file + '.custom.zst'
    
    try:
        compressed_file = zstd_comp.compress_file(input_file, output_path=custom_output)
        assert compressed_file == custom_output
        assert os.path.exists(compressed_file)
    finally:
        # Clean up files
        os.unlink(input_file)
        if os.path.exists(custom_output):
            os.unlink(custom_output)

def test_compress_invalid_level():
    """Test compression with invalid compression level."""
    test_content = "Invalid compression level"
    input_file = create_test_file(test_content)
    
    try:
        with pytest.raises(ValueError, match="Compression level must be between 1 and 22"):
            zstd_comp.compress_file(input_file, compression_level=23)
    finally:
        # Clean up file
        os.unlink(input_file)

def test_compress_nonexistent_file():
    """Test compression of a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        zstd_comp.compress_file('/path/to/nonexistent/file')

def test_decompress_nonzst_file():
    """Test decompression of a non-.zst file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Not a zst file")
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError, match="Input file must be a .zst file"):
            zstd_comp.decompress_file(temp_file_path)
    finally:
        # Clean up file
        os.unlink(temp_file_path)

def test_decompress_nonexistent_file():
    """Test decompression of a nonexistent file."""
    with pytest.raises(FileNotFoundError):
        zstd_comp.decompress_file('/path/to/nonexistent/file.zst')