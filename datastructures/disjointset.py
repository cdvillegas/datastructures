class disjointset:
	def __init__(self, pairs=None, vals=None):
		self.nodes = self.build(pairs, vals)

	def __str__(self):
		return ''.join([str(list(unique_set)) + ' ' for unique_set in self.sets()])

	def sets(self):
		sets = dict()
		for child in self.nodes.keys():
			children = set()
			while child != self.nodes[child]:
				children.add(child)
				child = self.nodes[child]
			sets[child] = sets.get(child, set()).union(children)
		roots = self.roots()
		return [sets[root].union(set([root])) for root in roots]


	def build(self, pairs, vals):
		roots = dict()
		if vals:
			for val in vals:
				roots[val] = val

		for root, child in pairs:
			child = roots.setdefault(child, child)
			while child != roots[child]:
				child = roots[child]
			roots[child] = root
		return roots

	def roots(self):
		return [key for key, val in self.nodes.items() if key == val]








