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

## Your Tasks

### Task 1: Implement `find_smallest()`
Complete the `find_smallest()` function in `sort.py`:
- Start from the given `start` index
- Track the index of the smallest element found
- Use the `key` function to extract comparison values
- Return the index (not the value!)

### Task 2: Implement `selection_sort()`
Complete the `selection_sort()` function in `sort.py`:
- Create a new list for the sorted result
- Repeatedly find and remove the smallest element
- Add it to the result list
- Return the sorted list (don't modify the original)

## Example

```python
>>> selection_sort([5, 3, 6, 2, 10])
[2, 3, 5, 6, 10]

# Step by step:
# [5, 3, 6, 2, 10] → find smallest (2) → result: [2]
# [5, 3, 6, 10]    → find smallest (3) → result: [2, 3]
# [5, 6, 10]       → find smallest (5) → result: [2, 3, 5]
# [6, 10]          → find smallest (6) → result: [2, 3, 5, 6]
# [10]             → find smallest (10) → result: [2, 3, 5, 6, 10]
```

## Testing
Run the tests to verify your implementation:
```bash
python -m pytest tests/ -v
```

## Hints
- The `key` parameter allows sorting by a specific attribute (like sorting people by age)
- Make a copy of the input list to avoid modifying the original
- Use `list.pop(index)` to remove and return an element at a specific index

## Submission
Commit and push your completed `sort.py` file.
