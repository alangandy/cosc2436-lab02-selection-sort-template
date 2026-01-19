"""Lab 02: Test Cases for Selection Sort"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sort import find_smallest, selection_sort


class TestFindSmallest:
    def test_find_smallest_basic(self):
        assert find_smallest([5, 3, 6, 2, 10]) == 3
    
    def test_find_smallest_first(self):
        assert find_smallest([1, 3, 6, 2, 10]) == 0
    
    def test_find_smallest_last(self):
        assert find_smallest([5, 3, 6, 2, 1]) == 4
    
    def test_find_smallest_with_start(self):
        assert find_smallest([1, 5, 3, 6, 2], start=1) == 4
    
    def test_find_smallest_single(self):
        assert find_smallest([42]) == 0


class TestSelectionSort:
    def test_sort_basic(self):
        assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    
    def test_sort_already_sorted(self):
        assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    def test_sort_reverse(self):
        assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    def test_sort_empty(self):
        assert selection_sort([]) == []
    
    def test_sort_single(self):
        assert selection_sort([42]) == [42]
    
    def test_sort_duplicates(self):
        assert selection_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    
    def test_sort_with_key(self):
        cities = [{"name": "Dallas", "pop": 1304379}, {"name": "Austin", "pop": 978908}]
        result = selection_sort(cities, key=lambda x: x["pop"])
        assert result[0]["name"] == "Austin"
    
    def test_does_not_modify_original(self):
        original = [5, 3, 6, 2, 10]
        copy = original.copy()
        selection_sort(original)
        assert original == copy


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
