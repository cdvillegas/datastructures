import sys
sys.path.insert(0, '..')

from datastructures.hashtable import HashTable
from util import testutil
import unittest

class TestHashTable(unittest.TestCase):
	def test_get(self):
		cases = testutil.parse_cases('hashtable', 'get')
		solutions = testutil.parse_solutions('get', 'hashtable', 'get')

		for result, solution in zip(cases, solutions):
			self.assertEqual(result, solution, testutil.error_str(result, solution, 'hashtable', 'get'))

if __name__ == '__main__':
	unittest.main()
	