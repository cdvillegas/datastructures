class MinHeap:
	"""
	A heap is a special tree-based data structure that satisfies the heap 
	property. It's an important structure because it's efficient for 
	priority queue operations, such as insertion, maximum extraction, 
	and sorting.

	In a min heap, for any given node I, the value of I is less than or 
	equal to the values of its children. This property must be 
	recursively true for all nodes in the binary tree.
	"""
	def __init__(self, items=[]):
		self.heap = []
		for item in items:
			self.push(item)

	def __len__(self):
		return len(self.heap)

	def peak(self):
		if len(self.heap) > 0:
			return self.heap[0]
		else:
			raise IndexError

	def push(self, val):
		self.heap.append(val)
		self.heapify_up()

	def pop(self):
		if len(self.heap) == 0:
		    raise IndexError
		elif len(self.heap) == 1:
		    return self.heap.pop()
		else:
		    top = self.peak()
		    self.heap[0] = self.heap.pop()
		    self.heapify_down()
		    return top
			
	def heapify_up(self):
		# Start at the bottom of the heap
		for index in range(len(self.heap) - 1, -1, -1):
			parent_index = self.parent_index(index)
			# If a node is smaller than its parent, swap them
			if self.has_parent(index) and self.heap[parent_index] > self.heap[index]:
				self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

	def heapify_down(self):
		for index in range(len(self.heap)):
			left_index = self.left_index(index) if self.has_left(index) else None
			right_index = self.right_index(index) if self.has_right(index) else None

			# Set min_index equal to the index of the node with the smaller value
			# If there are no children, min_index will be None
			if left_index and right_index:
				min_child_index = min(left_index, right_index, key=lambda i: self.heap[i])
			else:
				min_child_index = left_index if left_index else right_index

			# If the smallest index is smaller than the parent, swap the nodes
			# This is not necessary for the other child; we've already validated that it's greater
			if min_child_index and self.heap[min_child_index] < self.heap[index]:
				self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]

	# Getter functions
	def has_parent(self, index): return (index - 1) // 2 >= 0

	def has_left(self, index): return (index * 2) + 1 < len(self.heap)

	def has_right(self, index): return (index * 2) + 2 < len(self.heap)

	def parent_index(self, index): return (index - 1) // 2

	def left_index(self, index): return (index * 2) + 1

	def right_index(self, index): return (index * 2) + 2
