import sys
sys.path.insert(0, '..')

from util import testutil
import unittest

class TestGraph(unittest.TestCase):
	def test_topological_sort(self):
		for graph_type in ['simple', 'cycles']:
			cases = testutil.parse_cases('graph', graph_type)
			solutions = testutil.parse_solutions('topological_sort', 'graph', graph_type)

			for case, solution in zip(cases, solutions):
				result = case.topological_sort()
				self.assertEqual(result, solution, testutil.error_str(result, solution, 'graph', graph_type))


	def test_contains_cycle(self):
		for graph_type in ['simple', 'cycles']:
			cases = testutil.parse_cases('graph', graph_type)
			solutions = testutil.parse_solutions('contains_cycle', 'graph', graph_type)

			for case, solution in zip(cases, solutions):
				has_cycle_result, cycle_result = case.contains_cycle()
				has_cycle_solution, cycle_solution = solution
				self.assertEqual(has_cycle_result, has_cycle_solution, testutil.error_str(has_cycle_result, has_cycle_solution, 'graph', graph_type))
				self.assertEqual(cycle_result, cycle_solution, testutil.error_str(cycle_result, cycle_solution, 'graph', graph_type))


	def test_dfs(self):
		for graph_type in ['simple', 'cycles']:
			cases = testutil.parse_cases('graph', graph_type)
			solutions = testutil.parse_solutions('dfs', 'graph', graph_type)

			for case, solution in zip(cases, solutions):
				result = case.dfs(0)
				self.assertEqual(result, solution, testutil.error_str(result, solution, 'graph', graph_type))


	def test_bfs(self):
		for graph_type in ['simple', 'cycles']:
			cases = testutil.parse_cases('graph', graph_type)
			solutions = testutil.parse_solutions('bfs', 'graph', graph_type)

			for case, solution in zip(cases, solutions):
				result = case.bfs(0)
				self.assertEqual(result, solution, testutil.error_str(result, solution, 'graph', graph_type))
				

if __name__ == '__main__':
	unittest.main()