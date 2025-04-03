class CustomStack:
    """
    A custom stack data structure with a fixed capacity of 10 elements.
    
    Supports pushing, popping, peeking, and checking if empty for any data type.
    Raises exceptions for stack overflow and underflow conditions.
    """
    
    def __init__(self, capacity=10):
        """
        Initialize the stack with a given capacity (default 10).
        
        :param capacity: Maximum number of elements the stack can hold
        :type capacity: int
        """
        self._capacity = capacity
        self._items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        :param item: Item to be added to the stack (can be of any type)
        :raises OverflowError: If the stack has reached its maximum capacity
        """
        if len(self._items) >= self._capacity:
            raise OverflowError("Stack is full. Cannot push more items.")
        
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        :return: The top item from the stack
        :raises IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        
        return self._items.pop()
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        :return: The top item from the stack
        :raises IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack.")
        
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        :return: True if the stack is empty, False otherwise
        :rtype: bool
        """
        return len(self._items) == 0
    
    def __len__(self):
        """
        Return the current number of items in the stack.
        
        :return: Number of items in the stack
        :rtype: int
        """
        return len(self._items)