class Node:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next


class LinkedList:
	def __init__(self, list_items=[]):
		dummy = Node(-1)
		tail = dummy

		for item in list_items:
			tail.next = Node(item)
			tail = tail.next

		self.head = dummy.next

	def vals(self):
		node = self.head
		vals = []
		while node:
			vals += [node.val]
			node = node.next
		return vals

	def append(self, val):
		if not self.head:
			self.head = Node(val)
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(val)

	def appendleft(self, val):
		node = Node(val, next=self.head)
		self.head = node

	def sort(self):
		sorted_head = Node(-1)
		sorted_tail = sorted_head

		for val in sorted(self.vals()):
			sorted_tail.next = Node(val)
			sorted_tail = sorted_tail.next

		self.head = sorted_head.next

	def reverse(self):
		curr = self.head
		last = None
		while curr:
			next = curr.next
			curr.next = last
			last = curr
			curr = next

		self.head = last
