import pytest
from src.graph_cycle_detector import detect_cycle_in_directed_graph

def test_graph_with_cycle():
    """Test a graph that contains a cycle."""
    graph = {
        0: [1],
        1: [2],
        2: [3],
        3: [1]  # Creates a cycle 1 -> 2 -> 3 -> 1
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_graph_without_cycle():
    """Test a graph without a cycle."""
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_empty_graph():
    """Test an empty graph."""
    graph = {}
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_self_cycle():
    """Test a graph with a single node pointing to itself."""
    graph = {0: [0]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_complex_cycle():
    """Test a more complex graph with multiple nodes in a cycle."""
    graph = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [4, 5],
        4: [1],  # Creates a cycle 1 -> 3 -> 4 -> 1
        5: []
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_invalid_input_none():
    """Test handling of None input."""
    with pytest.raises(ValueError, match="Graph cannot be None"):
        detect_cycle_in_directed_graph(None)

def test_invalid_input_not_dict():
    """Test handling of non-dictionary input."""
    with pytest.raises(ValueError, match="Graph must be a dictionary"):
        detect_cycle_in_directed_graph([1, 2, 3])

def test_disconnected_graph_with_cycle():
    """Test a graph with disconnected components, one of which has a cycle."""
    graph = {
        0: [1],
        1: [2],
        2: [0],  # Cycle in first component
        3: [4],
        4: [5],
        5: []
    }
    assert detect_cycle_in_directed_graph(graph) == True