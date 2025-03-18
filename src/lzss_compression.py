"""
LZSS (Lempel-Ziv-Storer-Szymanski) Compression Algorithm Implementation.

This module provides functions for LZSS compression and decompression.
LZSS is a dictionary-based compression algorithm that replaces repeated 
sequences with references to previous occurrences.
"""

class LZSSCompressor:
    def __init__(self, window_size=4096, min_match_length=3):
        """
        Initialize the LZSS Compressor.
        
        Args:
            window_size (int): Size of the sliding window for searching matches.
            min_match_length (int): Minimum length of a match to be encoded.
        """
        self.window_size = window_size
        self.min_match_length = min_match_length

    def compress(self, data):
        """
        Compress the input data using LZSS algorithm.
        
        Args:
            data (bytes or str): Input data to compress.
        
        Returns:
            bytes: Compressed data.
        
        Raises:
            TypeError: If input is not bytes or str.
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes or str")
        
        # Initialize compression variables
        compressed = bytearray()
        data_length = len(data)
        current_position = 0

        while current_position < data_length:
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Define the search range (sliding window)
            search_start = max(0, current_position - self.window_size)
            search_end = current_position
            
            # Search for the longest match
            for start in range(search_start, search_end):
                match_length = 0
                
                # Check how long the match continues
                while (current_position + match_length < data_length and
                       data[start + match_length] == data[current_position + match_length] and
                       match_length < 255):
                    match_length += 1
                
                # Update best match if current match is longer
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_position - start
            
            # Encode the result
            if best_length >= self.min_match_length:
                # Matched sequence: encode as (offset, length)
                compressed.append(0)  # Flag for matched sequence
                compressed.append(best_offset & 0xFF)  # Lower 8 bits of offset
                compressed.append((best_offset >> 8) & 0xFF)  # Upper 8 bits of offset
                compressed.append(best_length)
                current_position += best_length
            else:
                # Unmatched byte: encode as literal
                compressed.append(1)  # Flag for literal
                compressed.append(data[current_position])
                current_position += 1
        
        return bytes(compressed)

    def decompress(self, compressed_data):
        """
        Decompress LZSS compressed data.
        
        Args:
            compressed_data (bytes): Compressed input data.
        
        Returns:
            bytes: Decompressed data.
        
        Raises:
            TypeError: If input is not bytes.
            ValueError: If compressed data is invalid.
        """
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check if we've reached the end of compressed data
            if i + 1 >= len(compressed_data):
                raise ValueError("Invalid compressed data")
            
            # Check flag byte
            flag = compressed_data[i]
            i += 1
            
            if flag == 0:  # Matched sequence
                # Ensure we have enough bytes for offset and length
                if i + 3 > len(compressed_data):
                    raise ValueError("Invalid compressed data")
                
                # Extract offset and length
                offset = compressed_data[i] | (compressed_data[i+1] << 8)
                length = compressed_data[i+2]
                i += 3
                
                # Reconstruct matched sequence
                start = len(decompressed) - offset
                for j in range(length):
                    if start + j < 0:
                        raise ValueError("Invalid offset in compressed data")
                    decompressed.append(decompressed[start + j])
            
            elif flag == 1:  # Literal byte
                if i >= len(compressed_data):
                    raise ValueError("Invalid compressed data")
                decompressed.append(compressed_data[i])
                i += 1
            
            else:
                raise ValueError(f"Invalid flag byte: {flag}")
        
        return bytes(decompressed)