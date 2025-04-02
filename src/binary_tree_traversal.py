class Node:
    """
    Represents a node in a binary tree.
    
    Attributes:
        value: The value stored in the node
        left: Reference to the left child node (None if no left child)
        right: Reference to the right child node (None if no right child)
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(root):
    """
    Perform an in-order depth-first traversal of the binary tree.
    
    Args:
        root (Node): The root node of the binary tree
    
    Returns:
        list: A list of node values in in-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    # Traverse left subtree
    result.extend(in_order_traversal(root.left))
    
    # Add current node's value
    result.append(root.value)
    
    # Traverse right subtree
    result.extend(in_order_traversal(root.right))
    
    return result

def pre_order_traversal(root):
    """
    Perform a pre-order depth-first traversal of the binary tree.
    
    Args:
        root (Node): The root node of the binary tree
    
    Returns:
        list: A list of node values in pre-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    # Add current node's value first
    result.append(root.value)
    
    # Traverse left subtree
    result.extend(pre_order_traversal(root.left))
    
    # Traverse right subtree
    result.extend(pre_order_traversal(root.right))
    
    return result

def post_order_traversal(root):
    """
    Perform a post-order depth-first traversal of the binary tree.
    
    Args:
        root (Node): The root node of the binary tree
    
    Returns:
        list: A list of node values in post-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    # Traverse left subtree
    result.extend(post_order_traversal(root.left))
    
    # Traverse right subtree
    result.extend(post_order_traversal(root.right))
    
    # Add current node's value last
    result.append(root.value)
    
    return result