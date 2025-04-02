import pytest
from src.rle_compression import run_length_encode, run_length_decode

def test_run_length_encode_string():
    """Test RLE encoding with a string input"""
    input_str = "AAAABBBCCCCC"
    expected = [('A', 4), ('B', 3), ('C', 5)]
    assert run_length_encode(input_str) == expected

def test_run_length_encode_list():
    """Test RLE encoding with a list input"""
    input_list = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C']
    expected = [('A', 4), ('B', 3), ('C', 5)]
    assert run_length_encode(input_list) == expected

def test_run_length_decode():
    """Test RLE decoding"""
    compressed = [('A', 4), ('B', 3), ('C', 5)]
    expected = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C']
    assert run_length_decode(compressed) == expected

def test_single_character():
    """Test RLE for a single character"""
    input_str = "X"
    expected = [('X', 1)]
    assert run_length_encode(input_str) == expected

def test_multiple_runs():
    """Test multiple different runs"""
    input_str = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWB"
    expected = [('W', 12), ('B', 1), ('W', 12), ('B', 3), ('W', 20), ('B', 1)]
    assert run_length_encode(input_str) == expected

def test_invalid_input_type():
    """Test error handling for invalid input type"""
    with pytest.raises(TypeError):
        run_length_encode(123)
    with pytest.raises(TypeError):
        run_length_decode(123)

def test_empty_input():
    """Test error handling for empty input"""
    with pytest.raises(ValueError):
        run_length_encode("")
    with pytest.raises(ValueError):
        run_length_decode([])

def test_invalid_compressed_data():
    """Test error handling for invalid compressed data"""
    with pytest.raises(ValueError):
        run_length_decode([('A', -1)])
    with pytest.raises(ValueError):
        run_length_decode([('A', 0)])

def test_roundtrip_encoding_decoding():
    """Test full roundtrip of encoding and decoding"""
    original = ['H', 'E', 'L', 'L', 'O', 'O', 'O']
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    assert decoded == original