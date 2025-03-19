import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_empty_items():
    """Test with empty items list"""
    assert solve_knapsack([], 10) == 0

def test_zero_capacity():
    """Test with zero capacity"""
    items = [(2, 3), (3, 4), (4, 5)]
    assert solve_knapsack(items, 0) == 0

def test_single_item_fits():
    """Test single item that fits in knapsack"""
    items = [(5, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 10

def test_single_item_does_not_fit():
    """Test single item that does not fit in knapsack"""
    items = [(6, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0

def test_multiple_item_combinations():
    """Test multiple possible item combinations"""
    items = [(1, 1), (3, 4), (4, 5), (5, 7)]
    capacity = 7
    assert solve_knapsack(items, capacity) == 9  # Corrected expected value

def test_invalid_items_type():
    """Test invalid items input (not a list)"""
    with pytest.raises(ValueError, match="Items must be a list"):
        solve_knapsack("not a list", 10)

def test_invalid_capacity_type():
    """Test invalid capacity input"""
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack([(1, 2)], "not an int")

def test_invalid_item_type():
    """Test invalid item tuple"""
    with pytest.raises(ValueError, match="Each item must be a"):
        solve_knapsack(["not a tuple"], 10)

def test_invalid_item_values():
    """Test invalid item values (negative)"""
    with pytest.raises(ValueError, match="Item weights and values must be non-negative"):
        solve_knapsack([(1, -2)], 10)

def test_large_capacity():
    """Test with large capacity"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 1000
    assert solve_knapsack(items, capacity) == 18