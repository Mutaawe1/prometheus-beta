from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle using Depth-First Search.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
            where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the input graph is None or not a valid dictionary.
    """
    # Validate input
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    if not isinstance(graph, dict):
        raise ValueError("Graph must be a dictionary")
    
    def dfs(node: int, visited: Set[int], rec_stack: Set[int]) -> bool:
        """
        Depth-first search to detect cycle in the graph.
        
        Args:
            node (int): Current node being explored
            visited (Set[int]): Set of nodes already visited
            rec_stack (Set[int]): Recursion stack to track current path
        
        Returns:
            bool: True if cycle detected, False otherwise
        """
        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)
        
        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor not visited, recursively check
            if neighbor not in visited:
                if dfs(neighbor, visited, rec_stack):
                    return True
            
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True
        
        # Remove node from recursion stack after exploration
        rec_stack.remove(node)
        return False
    
    # Check for cycle in each unvisited node
    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, visited, set()):
                return True
    
    return False