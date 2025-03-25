import pytest
from src.robot_vacuum import cleanRoom

def test_basic_room_cleaning():
    """Test a simple room cleaning scenario"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 1, 1, 0)
    assert steps > 0

def test_room_with_obstacles():
    """Test room cleaning with obstacles"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps > 0

def test_partially_blocked_room():
    """Test a room that cannot be fully cleaned"""
    grid = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    steps = cleanRoom(grid, 0, 0, 1)
    assert steps == -1

def test_single_cell_room():
    """Test a single-cell room"""
    grid = [[0]]
    steps = cleanRoom(grid, 0, 0, 0)
    assert steps == 0

def test_invalid_input_empty_grid():
    """Test handling of empty grid"""
    with pytest.raises(ValueError):
        cleanRoom([], 0, 0, 0)

def test_invalid_input_out_of_bounds():
    """Test handling of out of bounds starting position"""
    grid = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError):
        cleanRoom(grid, 2, 2, 0)

def test_multiple_path_scenarios():
    """Test different room configurations"""
    scenarios = [
        {
            'grid': [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            'start_r': 1,
            'start_c': 1,
            'direction': 0,
            'expected_min_steps': 8
        },
        {
            'grid': [
                [0, 0, 1],
                [0, 1, 0],
                [1, 0, 0]
            ],
            'start_r': 0,
            'start_c': 0,
            'direction': 1,
            'expected_min_steps': -1
        }
    ]
    
    for scenario in scenarios:
        steps = cleanRoom(
            scenario['grid'], 
            scenario['start_r'], 
            scenario['start_c'], 
            scenario['direction']
        )
        if scenario['expected_min_steps'] != -1:
            assert steps > 0
        else:
            assert steps == -1