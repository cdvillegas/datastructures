class Heap:
	def __init__(self, items=[]):
		self.heap = []
		for item in items:
			self.heap.push(item)

	def __str__(self): return str(self.heap)

	def __nonzero__(self): return len(self.heap) > 0

	def __len__(self): return len(self.heap)

	# Getter functions
	def has_parent(self, index): return (index - 1) // 2 >= 0

	def has_left_child(self, index): return (index * 2) + 1 < len(self.heap)

	def has_right_child(self, index): return (index * 2) + 2 < len(self.heap)

	def parent_index(self, index): return (index - 1) // 2

	def left_child_index(self, index): return (index * 2) + 1

	def right_child_index(self, index): return (index * 2) + 2


	def peak(self):
		''' Access top of heap
		Args:
			None

		Returns:
			Value at top of heap
			Raises IndexError if
			heap is empty
		'''

		if len(self.heap) > 0:
			return self.heap[0]
		else:
			raise IndexError


	def push(self, val):
		''' Push val onto heap
		Args:
			val: Comparable value

		Returns:
			None
		'''

		self.heap.append(val)
		self.heapify_up()


	def pop(self):
		''' Pop and return top of heap
		Args:
			None

		Returns:
			Value at top of heap;
			Raises IndexError if heap
			is empty
		'''

		top = self.peak()
		if len(self.heap) > 1:
			self.heap[0] = self.heap.pop()
		self.heapify_down()
		return top
			

	def heapify_up(self):
		''' Heapify from the bottom up
		Args:
			None

		Returns:
			None
		'''

		for index in range(len(self.heap) - 1, -1, -1):
			parent_index = self.parent_index(index)
			if self.has_parent(index) and self.heap[parent_index] > self.heap[index]:
				self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]


	def heapify_down(self):
		''' Heapify from the top down
		Args:
			None

		Returns:
			None
		'''

		for index in range(len(self.heap)):
			left_child_index = self.left_child_index(index) if self.has_left_child(index) else None
			right_child_index = self.right_child_index(index) if self.has_right_child(index) else None

			if left_child_index and right_child_index:
				min_index = min(left_child_index, right_child_index, key=lambda i: self.heap[i])
			else:
				min_index = left_child_index if left_child_index else right_child_index

			if min_index and self.heap[min_index] < self.heap[index]:
				self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]

			if self.has_right_child(index) and self.heap[right_child_index] < self.heap[index]:
				self.heap[index], self.heap[right_child_index] = self.heap[right_child_index], self.heap[index]

	@staticmethod
	def evaluate(actions):
		''' Execute list of actions
		Args:
			actions: List of strings
				representing actions, each
				beginning with the function
				name followed by function
				arguments

		Returns:
			List of results of evaluating
			each action
		'''

		heap = None
		res = []
		for action in actions:
			action = action.split(' ')
			if action[0] == 'init':
				heap = Heap()
				res.append(None)
			elif action[0] == 'push':
				res.append(heap.push(int(action[1])))
			elif action[0] == 'pop':
				res.append([heap.pop() for _ in range(int(action[1]))])
		return res
