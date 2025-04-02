import lzma
import io
from typing import Union, BinaryIO

def compress_lzma2(input_data: Union[bytes, str, BinaryIO], 
                   preset: int = 6, 
                   check: int = lzma.CHECK_CRC64) -> bytes:
    """
    Compress data using LZMA2 compression algorithm.

    Args:
        input_data (Union[bytes, str, BinaryIO]): The data to compress. 
            Can be bytes, a string, or a file-like binary object.
        preset (int, optional): Compression level (0-9). Defaults to 6.
        check (int, optional): Integrity check type. Defaults to CRC64.

    Returns:
        bytes: Compressed data in LZMA2 format.

    Raises:
        ValueError: If input data is invalid or preset is out of range.
        TypeError: If input data is of an unsupported type.
    """
    # Validate compression preset
    if not 0 <= preset <= 9:
        raise ValueError(f"Compression preset must be between 0 and 9, got {preset}")

    # Handle different input types
    if isinstance(input_data, str):
        input_bytes = input_data.encode('utf-8')
    elif isinstance(input_data, bytes):
        input_bytes = input_data
    elif hasattr(input_data, 'read'):
        # If it's a file-like object, read its contents
        input_bytes = input_data.read()
    else:
        raise TypeError(f"Unsupported input type: {type(input_data)}")

    # Ensure input is not empty
    if not input_bytes:
        return b''

    # Create LZMA2 compressor with specified preset and check
    compressor = lzma.LZMACompressor(
        format=lzma.FORMAT_ALONE,  # LZMA2 uses ALONE format
        preset=preset,
        check=check
    )

    try:
        # Compress the entire input
        compressed = compressor.compress(input_bytes)
        compressed += compressor.flush()
        return compressed
    except Exception as e:
        raise ValueError(f"Compression failed: {str(e)}")