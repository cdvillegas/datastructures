import json
from collections import defaultdict

class Graph:
	def __init__(self, nodes, edges, undirected=False, weighted=False):
		self.nodes = nodes
		self.graph = defaultdict(list)
		self.undirected = undirected
		self.weighted = weighted
		for first, second in edges:
			self.graph[first].append(second)
			if self.undirected:
				self.graph[second].append(first)


	def __str__(self):
		return 'Nodes: ' + str(self.nodes) + '\n' + 'Graph: ' + str(self.graph) + '\n'

	def topological_sort(self):
		''' Topologically sorted list of graph nodes
		Args:
			nodes: An integer representing
				max node index

			graph: A graph representing an
				adjacency matrix

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
