import unittest
from datastructures.binarytree import BinaryTree

class TestBinaryTree(unittest.TestCase):

    def test_insert_and_search(self):
        tree = BinaryTree()
        elements = [5, 3, 7, 2, 4, 6, 8]
        for elem in elements:
            tree.insert(elem)
            self.assertTrue(tree.search(elem))

        # Test searching for elements that don't exist
        self.assertFalse(tree.search(1))
        self.assertFalse(tree.search(9))

    def test_constructor(self):
        tree_list = [5, 3, 7, 2, 4, 6, 8]
        tree = BinaryTree(tree_list)
        self.assertEqual(tree.inorder_traversal(), [2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(tree.height(), 3)
        self.assertEqual(tree.list(), tree_list)

    def test_height(self):
        # Test an empty tree
        empty_tree = BinaryTree()
        self.assertEqual(empty_tree.height(), 0)

        # Test a balanced tree
        tree_balanced = BinaryTree([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(tree_balanced.height(), 3)

        # Test an unbalanced tree
        tree_unbalanced = BinaryTree([2, 1, 3, None, None, None, 4, None, None, None, None, None, None, None, 5])
        self.assertEqual(tree_unbalanced.height(), 4)

    def test_inorder_traversal(self):
        # Test an empty tree
        empty_tree = BinaryTree()
        self.assertEqual(empty_tree.inorder_traversal(), [])

        # Test a balanced tree
        tree_balanced = BinaryTree([5, 3, 7, 2, 4, 6, 8])
        self.assertEqual(tree_balanced.inorder_traversal(), [2, 3, 4, 5, 6, 7, 8])

    def test_balance(self):
        tree_unbalanced = BinaryTree([2, 1, 3, None, None, None, 4, None, None, None, None, None, None, None, 5])
        tree_unbalanced.balance()
        self.assertEqual(tree_unbalanced.height(), 3)
        self.assertEqual(tree_unbalanced.inorder_traversal(), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()