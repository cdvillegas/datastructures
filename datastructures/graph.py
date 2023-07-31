import json
from collections import defaultdict, deque

class Graph:
	"""
	A graph in is a data structure that consists of vertices 
	(or nodes) and edges connecting these vertices. An 
	efficient way to store graphs is to create an adjacency 
	dictionary, where dictionary[N] returns all nodes that N
	is connected to.
	"""
	def __init__(self, edges):
		self.graph = defaultdict(list)
		for first, second in edges:
			self.graph[first].append(second)


	def __str__(self):
		return 'Graph: ' + str(self.graph)


	def topological_sort(self):
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
				for adj in self.graph[node]:
					if not dfs(adj):
						return False
				visited[node] = 1
				order.append(node)
			return True

		# Traverse from each node
		for node in list(self.graph.keys()):
			if not dfs(node):
				return []
		return order[::-1]

	def dfs(self, start):
		stack = [start]
		visited = defaultdict(bool)
		ordering = []

		while len(stack) > 0:
			node = stack.pop()
			if not visited[node]:
				visited[node] = True
				ordering.append(node)
				for neighbor in self.graph[node]:
					if not visited[neighbor]:
						stack.append(neighbor)

		return ordering

	def bfs(self, start):
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
	    visited = defaultdict(lambda: 0)

	    # Define dfs traversal
	    def dfs(node, path):
	        if visited[node] == -1: # Node is currently being visited
	            return True, path[path.index(node):] + [node]
	        elif visited[node] == 1: # Node has already been visited
	            return False, None
	        else:
	            visited[node] = -1
	            for adj in self.graph[node]:
	                has_cycle, cycle_path = dfs(adj, path + [node])
	                if has_cycle:
	                    return has_cycle, cycle_path
	            visited[node] = 1
	        return False, None

	    # Traverse from each node
	    for node in list(self.graph.keys()):
	        has_cycle, cycle_path = dfs(node, [])
	        if has_cycle:
	            return has_cycle, cycle_path
	    return False, None


