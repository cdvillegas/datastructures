import sys
sys.path.insert(0, '..')

from util import testutil
import unittest

class TestGraph(unittest.TestCase):
	def test_topological_sort(self):
		for graph_type in ['simple', 'cycles']:
			cases = testutil.parse_cases('graph', graph_type)
			solutions = testutil.parse_solutions('topological', 'graph', graph_type)

			for case, solution in zip(cases, solutions):
				result = case.topological_sort()
				self.assertEqual(result, solution, testutil.error_str(result, solution, 'graph', str(case)))

if __name__ == '__main__':
	unittest.main()