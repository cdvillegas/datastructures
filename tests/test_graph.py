import unittest
from datastructures.graph import Graph

class TestGraph(unittest.TestCase):

    def test_topological_sort(self):
        edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        g = Graph(edges)
        self.assertEqual(g.topological_sort(), ['A', 'B', 'C', 'D'])

        edges_with_cycle = [('A', 'B'), ('B', 'C'), ('C', 'A')]
        g = Graph(edges_with_cycle)
        self.assertEqual(g.topological_sort(), []) # Cycle exists, so no topological sort possible

    def test_dfs(self):
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
        g = Graph(edges)
        self.assertEqual(g.dfs('A'), ['A', 'C', 'D', 'B'])

    def test_bfs(self):
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
        g = Graph(edges)
        self.assertEqual(g.bfs('A'), ['A', 'B', 'C', 'D'])

    def test_contains_cycle(self):
        edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        g = Graph(edges)
        self.assertEqual(g.contains_cycle(), (False, None))

        edges_with_cycle = [('A', 'B'), ('B', 'C'), ('C', 'A')]
        g = Graph(edges_with_cycle)
        has_cycle, cycle_path = g.contains_cycle()
        self.assertTrue(has_cycle)
        self.assertTrue(set(cycle_path) == set(['A', 'B', 'C']))

if __name__ == '__main__':
    unittest.main()

