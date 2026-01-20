#!/usr/bin/env python3
"""
Lab 02: Selection Sort - Interactive Tutorial
==============================================

Welcome to Python! This file helps you test your selection sort implementation.

🎯 GOAL: Implement find_smallest() and selection_sort() in sort.py

📚 PYTHON BASICS FOR C++/JAVA DEVELOPERS:
------------------------------------------
1. No semicolons needed at end of lines
2. Indentation matters! (use 4 spaces, not tabs)
3. No curly braces {} - Python uses indentation for blocks
4. Lists are like arrays: my_list = [1, 2, 3]
5. len(my_list) gives the length (like .size() or .length)
6. for i in range(5): loops 0,1,2,3,4 (like for(int i=0; i<5; i++))

HOW TO RUN THIS FILE:
---------------------
In your terminal, type:
    python main.py

Or in VS Code:
    Click the ▶️ Run button in the top right

After implementing your functions, run the tests:
    python -m pytest tests/ -v
"""

# =============================================================================
# IMPORTS - In Python, we import modules at the top of the file
# Similar to #include in C++ or import in Java
# =============================================================================
from sort import find_smallest, selection_sort


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def demo_find_smallest() -> None:
    """
    Demonstrate the find_smallest function.
    
    In C++/Java, you might write:
        int findSmallest(int arr[], int start) { ... }
    
    In Python:
        def find_smallest(arr, start=0): ...
    
    Notice: Python uses snake_case for function names (not camelCase)
    """
    print_header("PART 1: find_smallest()")
    
    # In Python, we create lists with square brackets (like arrays)
    test_array = [5, 3, 6, 2, 10]
    
    print(f"Test array: {test_array}")
    print()
    
    # Test 1: Find smallest in entire array
    print("Test 1: Find smallest in entire array")
    print(f"  find_smallest({test_array})")
    
    try:
        result = find_smallest(test_array)
        if result is not None:
            print(f"  ✅ Returned index: {result}")
            print(f"     Value at index {result}: {test_array[result]}")
            if result == 3:  # Index of 2
                print("     🎉 Correct! The smallest value is 2 at index 3")
            else:
                print(f"     ❌ Expected index 3 (value 2), got index {result}")
        else:
            print("  ❌ Function returned None - did you forget to return?")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    
    print()
    
    # Test 2: Find smallest starting from index 2
    print("Test 2: Find smallest starting from index 2")
    print(f"  find_smallest({test_array}, start=2)")
    print(f"  (Only looking at: {test_array[2:]})")
    
    try:
        result = find_smallest(test_array, start=2)
        if result is not None:
            print(f"  ✅ Returned index: {result}")
            print(f"     Value at index {result}: {test_array[result]}")
            if result == 3:
                print("     🎉 Correct! Starting from index 2, smallest is still 2 at index 3")
            else:
                print(f"     ❌ Expected index 3, got {result}")
        else:
            print("  ❌ Function returned None")
    except Exception as e:
        print(f"  ❌ Error: {e}")


def demo_selection_sort() -> None:
    """
    Demonstrate the selection_sort function.
    
    ALGORITHM (from the book):
    1. Find the smallest element
    2. Add it to a new array
    3. Repeat until original array is empty
    
    Time Complexity: O(n²) - you check n elements, then n-1, then n-2...
    """
    print_header("PART 2: selection_sort()")
    
    test_cases = [
        [5, 3, 6, 2, 10],
        [1],                    # Edge case: single element
        [3, 2, 1],              # Reverse sorted
        [1, 2, 3],              # Already sorted
        [],                     # Edge case: empty list
    ]
    
    for i, test_array in enumerate(test_cases, 1):
        print(f"\nTest {i}: selection_sort({test_array})")
        
        try:
            result = selection_sort(test_array)
            expected = sorted(test_array)  # Python's built-in sort for comparison
            
            if result is not None:
                print(f"  Your result:   {result}")
                print(f"  Expected:      {expected}")
                
                if result == expected:
                    print("  ✅ Correct!")
                else:
                    print("  ❌ Not quite right")
            else:
                print("  ❌ Function returned None - did you forget to return?")
        except Exception as e:
            print(f"  ❌ Error: {e}")


def python_tips() -> None:
    """Show some Python tips for C++/Java developers."""
    print_header("PYTHON TIPS FOR C++/JAVA DEVELOPERS")
    
    print("""
    📝 COMMON PATTERNS:
    
    C++/Java                          Python
    ---------                         ------
    arr.length or arr.size()    →     len(arr)
    arr[arr.length - 1]         →     arr[-1]  (negative indexing!)
    for(int i=0; i<n; i++)      →     for i in range(n):
    arr.push_back(x)            →     arr.append(x)
    arr.erase(arr.begin()+i)    →     arr.pop(i)  or  del arr[i]
    null                        →     None
    true/false                  →     True/False (capitalized!)
    
    🔥 PYTHON SHORTCUTS:
    
    # Swap two variables (no temp needed!)
    a, b = b, a
    
    # Get min value and its index
    min_val = min(arr)
    min_idx = arr.index(min_val)
    
    # List slicing (super powerful!)
    arr[1:4]    # Elements from index 1 to 3
    arr[2:]     # Elements from index 2 to end
    arr[:-1]    # All except last element
    arr[:]      # Copy of entire list
    
    # List comprehension (like a compact for loop)
    squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    """)


def main():
    """
    Main function - the entry point of our program.
    
    In Python, we use this pattern:
        if __name__ == "__main__":
            main()
    
    This means: "Only run main() if this file is run directly"
    (not when imported as a module)
    """
    print("\n" + "🐍" * 30)
    print("   LAB 02: SELECTION SORT")
    print("   Welcome to Python!")
    print("🐍" * 30)
    
    print("""
    📋 YOUR TASKS:
    1. Open sort.py
    2. Implement find_smallest()
    3. Implement selection_sort()
    4. Run this file to test: python main.py
    5. Run pytest when ready: python -m pytest tests/ -v
    """)
    
    # Run demonstrations
    demo_find_smallest()
    demo_selection_sort()
    python_tips()
    
    print_header("NEXT STEPS")
    print("""
    1. If tests fail, check your implementation in sort.py
    2. Use print() statements to debug (like cout or System.out.println)
    3. When all tests pass here, run: python -m pytest tests/ -v
    4. Complete the Lab Report section in README.md
    
    💡 DEBUGGING TIP:
    Add print statements in your functions to see what's happening:
        print(f"Current smallest_index: {smallest_index}")
        print(f"Comparing {arr[i]} with {arr[smallest_index]}")
    """)


# =============================================================================
# This is the Python entry point pattern
# In C++, you have: int main() { ... }
# In Java, you have: public static void main(String[] args) { ... }
# In Python, we use this:
# =============================================================================
if __name__ == "__main__":
    main()
