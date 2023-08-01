import unittest
from datastructures.linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_empty_list(self):
        ll = LinkedList()
        self.assertEqual(ll.vals(), [])

    def test_append(self):
        ll = LinkedList([1, 2, 3])
        ll.append(4)
        self.assertEqual(ll.vals(), [1, 2, 3, 4])

    def test_appendleft(self):
        ll = LinkedList([1, 2, 3])
        ll.appendleft(0)
        self.assertEqual(ll.vals(), [0, 1, 2, 3])

    def test_reverse(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        ll.reverse()
        self.assertEqual(ll.vals(), [5, 4, 3, 2, 1])

    def test_sort(self):
        ll = LinkedList([3, 1, 4, 1, 5, 9, 2, 6])
        ll.sort()
        self.assertEqual(ll.vals(), [1, 1, 2, 3, 4, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
