from typing import List, Tuple, Optional

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find a continuous path of cells that form a prime number sequence.
    
    Args:
        grid (List[List[int]]): 2D grid of integers
    
    Returns:
        Optional[List[Tuple[int, int]]]: Path of cell coordinates forming a prime sequence,
        or None if no such path exists
    """
    # Validate input
    if not grid or not grid[0]:
        return None
    
    rows, cols = len(grid), len(grid[0])
    
    # Special case: single cell grid
    if rows == 1 and cols == 1:
        if is_prime(grid[0][0]):
            return [(0, 0)]
        return None
    
    # Possible movement directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if the move is within grid boundaries."""
        return 0 <= x < rows and 0 <= y < cols
    
    def dfs(x: int, y: int, current_path: List[Tuple[int, int]], 
            current_sequence: List[int]) -> Optional[List[Tuple[int, int]]]:
        """
        Depth-first search to find a prime number sequence path.
        
        Args:
            x (int): Current row
            y (int): Current column
            current_path (List[Tuple[int, int]]): Path of visited cells
            current_sequence (List[int]): Sequence of numbers in the path
        
        Returns:
            Optional[List[Tuple[int, int]]]: Path if a prime sequence is found
        """
        # Check if the current sequence forms a prime number
        # Special case: for two cells, check the first two-digit number
        if len(current_sequence) > 1:
            current_num = int(''.join(map(str, current_sequence)))
            if is_prime(current_num):
                return current_path.copy()
        
        # Try all four directions
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if the new position is valid and not already in path
            if (is_valid_move(new_x, new_y) and 
                (new_x, new_y) not in current_path):
                
                # Create new path and sequence
                new_path = current_path + [(new_x, new_y)]
                new_sequence = current_sequence + [grid[new_x][new_y]]
                
                # Recursively search from the new position
                result = dfs(new_x, new_y, new_path, new_sequence)
                if result:
                    return result
        
        return None
    
    # Try starting from each cell
    for i in range(rows):
        for j in range(cols):
            # Start DFS from each cell
            path = dfs(i, j, [(i, j)], [grid[i][j]])
            if path:
                return path
    
    return None