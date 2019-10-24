import sys
sys.path.insert(0, '..')

from util import testutil
import unittest

class TestDisjointSets(unittest.TestCase):
	def test_build(self):
		for case_type in ['one set', 'two sets']:
			cases = testutil.parse_cases('disjointsets', case_type)
			solutions = testutil.parse_solutions('build', 'disjointsets', case_type)
			solutions = [[set(solution_set) for solution_set in solution] for solution in solutions ]
			for case, solution in zip(cases, solutions):
				self.assertEqual(case.sets(), solution, testutil.error_str(case, solution, 'disjointsets', 'build'))

if __name__ == '__main__':
	unittest.main()