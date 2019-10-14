import sys
sys.path.insert(0, '..')

from datastructures import binarytree
import unittest

class TestSomething(unittest.TestCase):
	def test_something(self):
		pass

def error_str(result, solution):
	return 'Got ' + str(result) + ', Expected ' + str(solution)

if __name__ == '__main__':
	unittest.main()