from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room using a robot vacuum cleaner algorithm.
    
    Args:
    - grid (List[List[int]]): 2D grid representing the room 
      (0 = empty cell, 1 = obstacle)
    - r (int): Starting row position of the robot
    - c (int): Starting column position of the robot
    - direction (int): Initial direction of the robot (0-3)
    
    Returns:
    - int: Minimum number of steps required to clean the entire room
    
    Raises:
    - ValueError: If grid is invalid or starting position is out of bounds
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position is out of bounds")
    
    # Directions: 0 = North, 1 = East, 2 = South, 3 = West
    dx = [-1, 0, 1, 0]  # row changes
    dy = [0, 1, 0, -1]  # column changes
    
    # Track visited cells and total area to clean
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_empty_cells = sum(row.count(0) for row in grid)
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if move is within grid and not an obstacle"""
        return (0 <= x < rows and 
                0 <= y < cols and 
                grid[x][y] == 0)
    
    def dfs(x: int, y: int, d: int) -> int:
        """
        Depth-first search to clean the room
        
        Args:
        - x (int): Current row
        - y (int): Current column
        - d (int): Current direction
        
        Returns:
        - int: Steps taken to clean
        """
        # Mark current cell as visited
        visited.add((x, y))
        
        steps = 0
        # Try all 4 directions
        for i in range(4):
            # Calculate next position
            new_d = (d + i) % 4
            nx = x + dx[new_d]
            ny = y + dy[new_d]
            
            # If move is valid and not visited
            if is_valid_move(nx, ny) and (nx, ny) not in visited:
                steps += 1  # Move
                steps += dfs(nx, ny, new_d)  # Explore
        
        return steps
    
    # Start cleaning
    total_steps = dfs(r, c, direction)
    
    # Check if all empty cells were visited
    if len(visited) != total_empty_cells:
        return -1  # Cannot clean entire room
    
    return total_steps