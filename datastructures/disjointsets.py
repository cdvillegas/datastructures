from collections import defaultdict

class DisjointSets:
    """
    Disjoint sets, also known as a "disjoint-set data structure" or 
    "union-find data structure," is a data structure that helps 
    maintain a collection of elements partitioned into multiple 
    disjoint subsets. Each element belongs to exactly one subset, 
    and no two subsets have any elements in common.
    """

    def __init__(self, pairs=[]):
        # Initialize with the given pairs of elements
        self.parents = defaultdict(lambda: -1)
        self.ranks = defaultdict(lambda: 0)
        self.add(pairs)

    def add(self, pairs):
        # Adding a connection between a pair of nodes is the same
        # as unioning the two sets
        for a, b in pairs:
            self.union(a, b)

    def find(self, node):
        # Find the parent of the given node, and apply path compression
        if self.parents[node] == -1:
            return node
        self.parents[node] = self.find(self.parents[node])  # Path compression
        return self.parents[node]

    def union(self, x, y):
        # Unite the sets containing x and y only if they are disjoint
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if parent_x == parent_y:
            return  # Already in the same set
        
        # Union by rank: Attach the smaller tree to the root of the larger tree
        if self.ranks[parent_x] < self.ranks[parent_y]:
            self.parents[parent_x] = parent_y
        elif self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = parent_x
        else:
            self.parents[parent_y] = parent_x
            self.ranks[parent_x] += 1
