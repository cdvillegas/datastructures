class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class BinaryTree:
	def __init__(self, tree_list=None):
		if not tree_list:
			self.root = None
			self.size = 0
		else:
			size = [0]
			def traverse(index, size):
				if index < len(tree_list) and tree_list[index] is not None:
					size[0] += 1
					node = Node(tree_list[index])
					node.left = traverse((index * 2) + 1, size)
					node.right = traverse((index * 2) + 2, size)
					return node
			self.root = traverse(0, size)
			self.size = size[0]


	def __str__(self): 
		return str(self.list())


	def height(self):
		''' Maximum height of the tree
		Args: None

		Returns:
			The height of the tree
			Returns 0 if no tree exists
		'''

		def traverse(node):
			if node:
				return 1 + max(traverse(node.left), traverse(node.right))
			else:
				return 0
		return traverse(self.root)


	def list(self):
		''' A list representation of the tree
		Args: None

		Returns:
			A list of node values where 
			the parent index of node at 
			index i is (i - 1) // 2
		'''
		vals = [None] * self.size
		def traverse(node, index, vals):
			if node:
				if index >= len(vals):
					vals.extend([None] * (index - len(vals) + 1))
				vals[index] = node.val
				traverse(node.left, (index * 2) + 1, vals)
				traverse(node.right, (index * 2) + 2, vals)
		traverse(self.root, 0, vals)
		return vals


	def insert(self, val):
		''' Inserts a value into the tree
		Args:
			val: An integer representing a 
				node value

		Returns: None
		'''
		def traverse(node):
			if not node:
				return Node(val)
			else:
				if val < node.val:
					node.left = traverse(node.left)
				elif val > node.val:
					node.right = traverse(node.right)
				return node
		self.root = traverse(self.root)
		self.size += 1


	def search(self, val):
		''' Searches the tree for a value
		Args:
			val: An integer representing a 
				node value

		Returns:
			True if a node with value val
			exists in the tree, False
			otherwise
		'''
		def traverse(node):
			if not node:
				return False
			else:
				if val < node.val:
					return traverse(node.left)
				elif val > node.val:
					return traverse(node.right)
				else:
					return True
		return traverse(self.root)


	def inorder_traversal(self):
		''' Searches the tree for a value
		Args: None

		Returns:
			A list of sorted node values
		'''
		def traverse(node):
			if not node:
				return []
			return traverse(node.left) + [node.val] + traverse(node.right)

		return traverse(self.root)


	def balance(self):
		''' Optimally balance the tree
		Args: None

		Returns: None
		'''
		def traverse(traversal, lo, hi):
			if lo <= hi:
				mid = (hi + lo) // 2
				node = Node(traversal[mid])
				node.left = traverse(traversal, lo, mid - 1)
				node.right = traverse(traversal, mid + 1, hi)
				return node
		traversal = self.inorder_traversal()
		self.root = traverse(traversal, 0, len(traversal) - 1)
