class Node:
	def __init__(self, val, nxt=None):
		self.val = val
		self.nxt = nxt


class LinkedList:
	def __init__(self, head=None):
		self.head = head


	def __str__(self):
		s = ''
		node = self.head
		while node.nxt:
			s += str(node.val) + ' - '
			node = node.nxt
		return s + str(node.val)


	def vals(self):
		''' List of values in linked list
		Args:
			None

		Returns:
			List of values in linked list
		'''

		node = self.head
		vals = []
		while node:
			vals += [node.val]
			node = node.nxt
		return vals

	def append(self, val):
		''' Append node to right of linked list
		Args:
			val: Value to append

		Returns:
			None
		'''

		if not self.head:
			self.head = Node(val)
		else:
			curr = self.head
			while curr.nxt:
				curr = curr.nxt
			curr.nxt = Node(val)


	def appendleft(self, node):
		''' Append node to left of linked list
		Args:
			val: Value to append

		Returns:
			None
		'''

		node.nxt = self.head
		self.head = node

	def sort(self):
		''' Sort linked list
		Args:
			None

		Returns:
			None
		'''

		sorted_head = Node(-1)
		sorted_curr = sorted_head

		for val in sorted(self.vals()):
			sorted_curr.nxt = Node(val)
			sorted_curr = sorted_curr.nxt

		self.head = sorted_head.nxt

	def reverse(self):
		''' Reverses linked list
		Args:
			None

		Returns:
			None
		'''

		curr = self.head
		last = None
		while curr:
			nxt = curr.nxt
			curr.nxt = last
			last = curr
			curr = nxt

		self.head = last
