import sys
sys.path.insert(0, '..')

from util import testutil
import unittest

class TestHeap(unittest.TestCase):
	def test_sort(self):
		cases = testutil.parse_cases('heap', 'sort')
		solutions = testutil.parse_solutions('sort', 'heap', 'sort')

		for result, solution in zip(cases, solutions):
			self.assertEqual(result, solution, testutil.error_str(result, solution, 'heap', 'sort'))

if __name__ == '__main__':
	unittest.main()