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
		node = self.head
		vals = []
		while node:
			vals += [node.val]
			node = node.nxt
		return vals

	def append(self, node):
		if not self.head:
			self.head = node
		else:
			curr = self.head
			while curr.nxt:
				curr = curr.nxt
			curr.nxt = node

	def appendleft(self, node):
		node.nxt = self.head
		self.head = node

	def sort(self):
		sorted_head = Node(-1)
		sorted_curr = sorted_head

		for val in sorted(self.vals()):
			sorted_curr.nxt = Node(val)
			sorted_curr = sorted_curr.nxt

		self.head = sorted_head.nxt

	def reverse(self):
		curr = self.head
		last = None
		while curr:
			nxt = curr.nxt
			curr.nxt = last
			last = curr
			curr = nxt

		self.head = last


if __name__ == '__main__':
	link = LinkedList()
	for i in range(10, 0, -1):
		link.append(Node(i))
	print(link)
	link.sort()
	print(link)
	link.reverse()
	print(link)


