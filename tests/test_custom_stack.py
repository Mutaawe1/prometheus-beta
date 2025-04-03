import pytest
from src.custom_stack import CustomStack

def test_stack_initialization():
    """Test stack initialization."""
    stack = CustomStack()
    assert len(stack) == 0
    assert stack.is_empty() is True

def test_push_and_peek():
    """Test pushing items and peeking."""
    stack = CustomStack()
    stack.push(5)
    assert stack.peek() == 5
    assert len(stack) == 1
    
    stack.push("hello")
    assert stack.peek() == "hello"
    assert len(stack) == 2

def test_pop():
    """Test popping items."""
    stack = CustomStack()
    stack.push(1)
    stack.push(2)
    
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert len(stack) == 0
    assert stack.is_empty() is True

def test_mixed_type_stack():
    """Test stack with different data types."""
    stack = CustomStack()
    stack.push(42)
    stack.push("string")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})
    
    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]

def test_stack_overflow():
    """Test stack overflow condition."""
    stack = CustomStack(capacity=2)
    stack.push(1)
    stack.push(2)
    
    with pytest.raises(OverflowError):
        stack.push(3)

def test_pop_empty_stack():
    """Test popping from an empty stack."""
    stack = CustomStack()
    
    with pytest.raises(IndexError):
        stack.pop()

def test_peek_empty_stack():
    """Test peeking an empty stack."""
    stack = CustomStack()
    
    with pytest.raises(IndexError):
        stack.peek()