# Lab 02: Selection Sort

## Overview
In this lab, you will implement **Selection Sort**, a simple O(n²) sorting algorithm covered in Chapter 2 of "Grokking Algorithms."

## Learning Objectives
- Understand how selection sort works
- Implement the `find_smallest()` helper function
- Implement the complete `selection_sort()` algorithm
- Understand O(n²) time complexity

## Background

### How Selection Sort Works
Selection sort builds a sorted list by repeatedly finding the smallest element:

1. Find the smallest element in the unsorted portion
2. Swap it to the front (or add to a new sorted list)
3. Repeat for the remaining unsorted elements

### Time Complexity
- **O(n²)** - For each of n elements, we scan through up to n elements
- Not efficient for large datasets, but simple to understand and implement

---

## Complete Solutions

### Task 1: `find_smallest()` - Complete Implementation

```python
def find_smallest(arr: List[Any], start: int = 0, key: Callable = lambda x: x) -> int:
    """
    Find the index of the smallest element starting from 'start' position.
    
    Args:
        arr: List to search
        start: Starting index (default 0)
        key: Function to extract comparison value (default identity)
    
    Returns:
        Index of smallest element
    """
    smallest_index = start
    smallest_value = key(arr[start])
    
    for i in range(start + 1, len(arr)):
        current_value = key(arr[i])
        if current_value < smallest_value:
            smallest_value = current_value
            smallest_index = i
    
    return smallest_index
```

**How it works:**
1. Initialize `smallest_index` to the `start` position
2. Store the value at that position (using the `key` function to extract it)
3. Loop through all elements from `start + 1` to the end
4. For each element, extract its value using `key`
5. If this value is smaller than our current smallest, update both `smallest_index` and `smallest_value`
6. Return the index of the smallest element found

---

### Task 2: `selection_sort()` - Complete Implementation

```python
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
    """
    # Create a copy to avoid modifying the original
    arr_copy = list(arr)
    result = []
    
    while arr_copy:
        # Find the smallest element in the remaining list
        smallest_idx = find_smallest(arr_copy, start=0, key=key)
        # Remove it from the copy and add to result
        smallest_element = arr_copy.pop(smallest_idx)
        result.append(smallest_element)
    
    return result
```

**How it works:**
1. Create a copy of the input array (so we don't modify the original)
2. Create an empty result list
3. While there are still elements in the copy:
   - Find the index of the smallest element using `find_smallest()`
   - Remove that element from the copy using `pop(index)`
   - Append it to the result list
4. Return the sorted result

---

## Example Usage

```python
# Basic sorting
>>> selection_sort([5, 3, 6, 2, 10])
[2, 3, 5, 6, 10]

# Step-by-step visualization:
# arr_copy = [5, 3, 6, 2, 10], result = []
# smallest_idx = 3 (value 2), pop it → arr_copy = [5, 3, 6, 10], result = [2]
# smallest_idx = 1 (value 3), pop it → arr_copy = [5, 6, 10], result = [2, 3]
# smallest_idx = 0 (value 5), pop it → arr_copy = [6, 10], result = [2, 3, 5]
# smallest_idx = 0 (value 6), pop it → arr_copy = [10], result = [2, 3, 5, 6]
# smallest_idx = 0 (value 10), pop it → arr_copy = [], result = [2, 3, 5, 6, 10]

# Sorting with a key function (sort by age)
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_people = selection_sort(people, key=lambda p: p["age"])
# Result: [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}, {"name": "Charlie", "age": 35}]

# Using find_smallest directly
>>> find_smallest([5, 3, 6, 2, 10])
3  # Index of value 2

>>> find_smallest([5, 3, 6, 2, 10], start=2)
3  # Starting from index 2, smallest is still at index 3
```

---

## Testing
Run the tests to verify your implementation:
```bash
python -m pytest tests/ -v
```

## Submission
Commit and push your completed `sort.py` file.
