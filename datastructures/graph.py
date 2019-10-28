import json
from collections import defaultdict, deque

class Graph:
	def __init__(self, edges):
		self.graph = defaultdict(list)
		for first, second in edges:
			self.graph[first].append(second)


	def __str__(self):
		return 'Graph: ' + str(self.graph)


	def topological_sort(self):
		''' Topologically sorted list of graph nodes
		Args: None

		Returns:
			A list of integer nodes sorted 
			topologically (every node precedes 
			its neighbors)

			An empty list if there exists a cycle
		'''

		visited = defaultdict(lambda: 0)
		order = []
	
		# Define dfs traversal
		def dfs(node):
			if visited[node] == -1:
				return False
			elif visited[node] == 1:
				return True
			else:
				visited[node] = -1
				for adj in self.graph[node][::-1]:
					if not dfs(adj):
						return False
				visited[node] = 1
				order.append(node)
			return True

		# Traverse from each node
		for node in self.graph.keys():
			if not dfs(node):
				return []
		return order[::-1]

	def dfs(self, start):
		''' Breadth first search ordering of graph nodes
		Args: None

		Returns:
			A list of integer nodes sorted 
			by breadth first ordering from start node

			Raises exception if start does not exist
		'''

		stack = [start]
		visited = defaultdict(bool)
		ordering = []

		while len(stack) > 0:
			node = stack.pop()
			if not visited[node]:
				visited[node] = True
				ordering.append(node)
				for neighbor in self.graph[node][::-1]:
					if not visited[neighbor]:
						stack.append(neighbor)

		return ordering


	def bfs(self, start):
		''' Breadth first search ordering of graph nodes
		Args: None

		Returns:
			A list of integer nodes sorted 
			by breadth first ordering from start node

			Raises exception if start does not exist
		'''

		queue = deque([start])
		visited = defaultdict(bool)
		ordering = []

		while len(queue) > 0:
			node = queue.popleft()
			if not visited[node]:
				visited[node] = True
				ordering.append(node)
				for neighbor in self.graph[node]:
					if not visited[neighbor]:
						queue.append(neighbor)

		return ordering


	def contains_cycle(self):
		''' Detects and returns a cycle if it exists
		Args: None

		Returns:
			A boolean value, which is true if there 
			exists a cycle and false otherwise

			A path, which contains the nodes in the 
			cycle in order if a cycle exists and is 
			None otherwise.
		'''
		visited = defaultdict(lambda: 0)

		# Define dfs traversal
		def dfs(node, path):
			if visited[node] == -1: # Node is currently beign visited
				return True, path[path.index(node):] + [node]
			elif visited[node] == 1: # Node has already been visited
				return False, None
			else:
				visited[node] = -1
				for adj in self.graph[node][::-1]:
					has_cycle, cycle_path = dfs(adj, path + [node])
					if has_cycle:
						return has_cycle, cycle_path
				visited[node] = 1
			return False, None

		# Traverse from each node
		for node in self.graph.keys():
			has_cycle, cycle_path = dfs(node, [])
			if has_cycle:
				return has_cycle, cycle_path
		return False, None

