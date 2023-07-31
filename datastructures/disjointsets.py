from collections import defaultdict

class DisjointSets:
	"""
	This data structure keeps track of a set of elements partitioned
	into several disjoin subsets. Two sets are disjoint when they 
	have no elements in common.

	This data structure supports two key methods:

	find() : Determines which subset an element belongs to by 
				returning its parent node

	union() : Merges two different subsets into a single subset
	"""

	def __init__(self, pairs=[]):
		self.parents = defaultdict(lambda: -1)
		self.add(pairs)

	def add(self, pairs):
		for a, b in pairs:
			self.union(a, b)

	def find(self, node):
		if x != self.parents[node]: 
			self.parents[node] = find(self.parents[node])

		return self.parents[node]

	def union(self, x, y):
		self.parents[find(y)] = find(x)








