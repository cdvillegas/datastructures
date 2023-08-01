import unittest
from datastructures.disjoint_sets import DisjointSets

class TestDisjointSets(unittest.TestCase):
    def test_find_new_node(self):
        ds = DisjointSets()
        node = 5
        self.assertEqual(ds.find(node), node)

    def test_find_after_union(self):
        ds = DisjointSets([(1, 2), (3, 4)])
        self.assertEqual(ds.find(1), ds.find(2))
        self.assertNotEqual(ds.find(1), ds.find(3))
        self.assertEqual(ds.find(3), ds.find(4))

    def test_add_pairs(self):
        ds = DisjointSets()
        ds.add([(1, 2), (3, 4)])
        self.assertEqual(ds.find(1), ds.find(2))
        self.assertNotEqual(ds.find(1), ds.find(3))
        self.assertEqual(ds.find(3), ds.find(4))

    def test_union(self):
        ds = DisjointSets()
        ds.union(1, 2)
        ds.union(2, 3)
        ds.union(4, 5)
        self.assertEqual(ds.find(1), ds.find(3))
        self.assertNotEqual(ds.find(1), ds.find(4))
        self.assertEqual(ds.find(4), ds.find(5))

    def test_multiple_union_operations(self):
        ds = DisjointSets()
        ds.union(1, 2)
        ds.union(2, 3)
        ds.union(3, 4)
        self.assertEqual(ds.find(1), ds.find(4))
        self.assertNotEqual(ds.find(1), ds.find(5))

    def test_no_nodes(self):
        ds = DisjointSets()
        self.assertEqual(ds.find(1), 1)
        self.assertEqual(ds.find(2), 2)

    def test_initialization_with_pairs(self):
        ds = DisjointSets([(1, 2), (2, 3), (4, 5)])
        self.assertEqual(ds.find(1), ds.find(3))
        self.assertNotEqual(ds.find(1), ds.find(4))
        self.assertEqual(ds.find(4), ds.find(5))

    def test_add_and_union_combination(self):
        ds = DisjointSets([(1, 2)])
        ds.add([(2, 3)])
        ds.union(3, 4)
        self.assertEqual(ds.find(1), ds.find(4))
        self.assertNotEqual(ds.find(1), ds.find(5))


if __name__ == '__main__':
    unittest.main()