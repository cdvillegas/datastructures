import unittest
from datastructures.sort import Sort

class TestSort(unittest.TestCase):
    
    def test_heap_sort(self):
        self.assertEqual(Sort.heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.heap_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(Sort.heap_sort([]), [])
        self.assertEqual(Sort.heap_sort([1]), [1])
        self.assertEqual(Sort.heap_sort([9, 8, 10, 7, 6, 5]), [5, 6, 7, 8, 9, 10])

    def test_merge_sort(self):
        self.assertEqual(Sort.merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.merge_sort([3, 3, 2, 1, 4]), [1, 2, 3, 3, 4])
        self.assertEqual(Sort.merge_sort([]), [])
        self.assertEqual(Sort.merge_sort([1]), [1])
        self.assertEqual(Sort.merge_sort([9, 1, 8, 2, 7]), [1, 2, 7, 8, 9])

    def test_quick_sort(self):
        self.assertEqual(Sort.quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.quick_sort([1, 5, 4, 2, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.quick_sort([]), [])
        self.assertEqual(Sort.quick_sort([1]), [1])
        self.assertEqual(Sort.quick_sort([3, 1, 4, 1, 2, 5]), [1, 1, 2, 3, 4, 5])

    def test_bubble_sort(self):
        self.assertEqual(Sort.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.bubble_sort([4, 2, 4, 1, 5, 3]), [1, 2, 3, 4, 4, 5])
        self.assertEqual(Sort.bubble_sort([]), [])
        self.assertEqual(Sort.bubble_sort([1]), [1])
        self.assertEqual(Sort.bubble_sort([9, 7, 8, 5, 6]), [5, 6, 7, 8, 9])

    def test_insertion_sort(self):
        self.assertEqual(Sort.insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.insertion_sort([5, 3, 4, 1, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.insertion_sort([]), [])
        self.assertEqual(Sort.insertion_sort([1]), [1])
        self.assertEqual(Sort.insertion_sort([10, 20, 10, 30, 20]), [10, 10, 20, 20, 30])

    def test_selection_sort(self):
        self.assertEqual(Sort.selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(Sort.selection_sort([5, 5, 5, 1, 1]), [1, 1, 5, 5, 5])
        self.assertEqual(Sort.selection_sort([]), [])
        self.assertEqual(Sort.selection_sort([1]), [1])
        self.assertEqual(Sort.selection_sort([3, 3, 2, 2, 1]), [1, 2, 2, 3, 3])

if __name__ == '__main__':
    unittest.main()
