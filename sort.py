"""
Lab 02: Selection Sort
Implement selection sort from Chapter 2.

From Chapter 2: Selection sort works by:
1. Find the smallest element
2. Swap it to the front
3. Repeat for remaining elements
"""
from typing import List, Any, Callable


def find_smallest(arr: List[Any], start: int = 0, key: Callable = lambda x: x) -> int:
    """
    Find the index of the smallest element starting from 'start' position.
    
    Args:
        arr: List to search
        start: Starting index (default 0)
        key: Function to extract comparison value (default identity)
    
    Returns:
        Index of smallest element
    
    Example:
        >>> find_smallest([5, 3, 6, 2, 10])
        3
        >>> find_smallest([5, 3, 6, 2, 10], start=2)
        3
    """
    # TODO: Implement find_smallest
    # 1. Initialize smallest_index to start
    # 2. Loop from start+1 to end of array
    # 3. If current element < smallest, update smallest_index
    # 4. Return smallest_index
    
    pass  # Remove this and add your code


def selection_sort(arr: List[Any], key: Callable = lambda x: x) -> List[Any]:
    """
    Sort list using selection sort algorithm.
    
    Args:
        arr: List to sort
        key: Function to extract comparison value
    
    Returns:
        New sorted list (does not modify original)
    
    Time Complexity: O(n²)
    Space Complexity: O(n) - creates new list
    
    Example:
        >>> selection_sort([5, 3, 6, 2, 10])
        [2, 3, 5, 6, 10]
    """
    # TODO: Implement selection_sort
    # Method 1 (from book): Build new array
    # 1. Create empty result list
    # 2. Create copy of input array
    # 3. While copy is not empty:
    #    a. Find smallest element
    #    b. Remove it from copy and append to result
    # 4. Return result
    
    pass  # Remove this and add your code
