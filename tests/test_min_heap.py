import unittest
from datastructures.min_heap import MinHeap

class TestMinHeap(unittest.TestCase):

    def test_empty_heap(self):
        heap = MinHeap()
        self.assertEqual(heap.heap, [])
        with self.assertRaises(IndexError):
            heap.peak()
        with self.assertRaises(IndexError):
            heap.pop()

    def test_push(self):
        heap = MinHeap()
        heap.push(5)
        heap.push(2)
        heap.push(8)
        self.assertEqual(heap.peak(), 2)
        heap.push(1)
        self.assertEqual(heap.peak(), 1)

    def test_pop(self):
        heap = MinHeap([5, 2, 8, 1])
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 8)
        with self.assertRaises(IndexError):
            print(heap.pop())

    def test_heapify_with_constructor(self):
        heap = MinHeap([5, 3, 9, 1, 7])
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 7)
        self.assertEqual(heap.pop(), 9)

    def test_push_and_pop(self):
        heap = MinHeap()
        heap.push(5)
        heap.push(3)
        heap.push(9)
        heap.push(1)
        self.assertEqual(heap.pop(), 1)
        heap.push(7)
        self.assertEqual(heap.pop(), 3)
        self.assertEqual(heap.pop(), 5)

if __name__ == '__main__':
    unittest.main()
