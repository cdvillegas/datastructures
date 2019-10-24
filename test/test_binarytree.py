import sys
sys.path.insert(0, '..')

from util import testutil
import unittest

class TestBinaryTree(unittest.TestCase):
	def test_height(self):
		for tree_type in ['balanced', 'unbalanced']:
			cases = testutil.parse_cases('binarytree', tree_type)
			solutions = testutil.parse_solutions('height', 'binarytree', tree_type)

			for tree, solution in zip(cases, solutions):
				result = tree.height()
				self.assertEqual(result, solution, testutil.error_str(result, solution, 'tree', str(tree)))


if __name__ == '__main__':
	unittest.main()