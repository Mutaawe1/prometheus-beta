import pytest
from src.binary_tree_traversal import Node, in_order_traversal, pre_order_traversal, post_order_traversal

def test_empty_tree():
    """Test traversals on an empty tree (None)"""
    assert in_order_traversal(None) == []
    assert pre_order_traversal(None) == []
    assert post_order_traversal(None) == []

def test_single_node_tree():
    """Test traversals on a tree with a single node"""
    root = Node(5)
    assert in_order_traversal(root) == [5]
    assert pre_order_traversal(root) == [5]
    assert post_order_traversal(root) == [5]

def test_complete_binary_tree():
    """Test traversals on a complete binary tree"""
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Expected traversal results
    assert in_order_traversal(root) == [4, 2, 5, 1, 6, 3, 7]
    assert pre_order_traversal(root) == [1, 2, 4, 5, 3, 6, 7]
    assert post_order_traversal(root) == [4, 5, 2, 6, 7, 3, 1]

def test_unbalanced_tree():
    """Test traversals on an unbalanced tree"""
    #        1
    #       /
    #      2
    #     /
    #    3
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)

    # Expected traversal results
    assert in_order_traversal(root) == [3, 2, 1]
    assert pre_order_traversal(root) == [1, 2, 3]
    assert post_order_traversal(root) == [3, 2, 1]