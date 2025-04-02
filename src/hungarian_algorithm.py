import numpy as np

def hungarian_assignment(cost_matrix):
    """
    Implement the Hungarian algorithm for solving the assignment problem.
    
    Args:
        cost_matrix (list of lists or numpy.ndarray): A rectangular matrix 
                     representing the cost of assigning each task to each worker.
    
    Returns:
        list: A list of (worker, task) assignments that minimize the total cost.
    
    Raises:
        ValueError: If the input is not a valid cost matrix.
    """
    # Validate input
    if not isinstance(cost_matrix, (list, np.ndarray)):
        raise ValueError("Input must be a list or numpy array")
    
    # Convert to numpy array for easier manipulation
    cost_matrix = np.array(cost_matrix, dtype=float)
    
    # Check for empty matrix
    if cost_matrix.size == 0:
        return []
    
    # Get matrix dimensions
    rows, cols = cost_matrix.shape
    
    # Step 1: Subtract row minimums
    for i in range(rows):
        row_min = np.min(cost_matrix[i])
        cost_matrix[i] -= row_min
    
    # Step 2: Subtract column minimums
    for j in range(cols):
        col_min = np.min(cost_matrix[:, j])
        cost_matrix[:, j] -= col_min
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Find covered rows and columns
        covered_rows = set()
        covered_cols = set()
        
        # Find initial zero in each row
        zero_positions = []
        for i in range(rows):
            zero_cols = np.where(matrix[i] == 0)[0]
            if len(zero_cols) > 0:
                zero_positions.append((i, zero_cols[0]))
        
        # Greedy covering algorithm
        while zero_positions:
            row, col = zero_positions.pop(0)
            
            # If row or column already covered, skip
            if row in covered_rows or col in covered_cols:
                continue
            
            # Cover the row and column
            covered_rows.add(row)
            covered_cols.add(col)
            
            # Remove zeros from covered row
            zero_positions = [(r, c) for (r, c) in zero_positions 
                              if r != row and c != col]
        
        return len(covered_rows) + len(covered_cols)
    
    # Step 4: Find optimal assignment
    def find_assignment(matrix):
        assignments = []
        used_rows = set()
        used_cols = set()
        
        for row in range(rows):
            zero_cols = np.where(matrix[row] == 0)[0]
            for col in zero_cols:
                if col not in used_cols and row not in used_rows:
                    assignments.append((row, col))
                    used_rows.add(row)
                    used_cols.add(col)
                    break
        
        return assignments
    
    # Try to find optimal assignments
    assignments = find_assignment(cost_matrix)
    
    # If not all assigned, adjust matrix
    while len(assignments) < min(rows, cols):
        # Find minimum uncovered element
        min_val = float('inf')
        for i in range(rows):
            for j in range(cols):
                # Skip covered elements
                if i in [a[0] for a in assignments] or j in [a[1] for a in assignments]:
                    continue
                min_val = min(min_val, cost_matrix[i, j])
        
        # Adjust matrix
        for i in range(rows):
            for j in range(cols):
                # Subtract min from uncovered, add to intersections
                if (i not in [a[0] for a in assignments] and 
                    j not in [a[1] for a in assignments]):
                    cost_matrix[i, j] -= min_val
        
        # Retry assignment
        assignments = find_assignment(cost_matrix)
    
    return assignments