import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the sleep sort algorithm.
    
    Sleep sort works by creating a separate thread for each number,
    where each thread sleeps for a duration proportional to the number's value.
    Threads then add their number to the result list when they wake up.
    
    Args:
        arr (List[int]): Input list of positive integers to be sorted.
    
    Returns:
        List[int]: Sorted list of input numbers.
    
    Raises:
        ValueError: If input contains negative numbers.
    """
    # Validate input
    if not arr:
        return []
    
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort only works with non-negative integers")
    
    # Create synchronization primitives
    result = []
    lock = threading.Lock()
    
    # Define thread function
    def sort_thread(num):
        time.sleep(num * 0.1)  # Sleep proportional to number value
        with lock:
            result.append(num)
    
    # Create and start threads
    threads = []
    for num in arr:
        thread = threading.Thread(target=sort_thread, args=(num,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result