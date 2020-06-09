from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # number of vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    def isCyclic(self):
        # allocate memory for creating V subsets and
        # initialize all subsets as single element sets
        parent = [-1] * (self.V)

        # iterate through all the edges of the graph,
        # find subset of both vertices of every edge,
        # if both subsets are the same, then there is a cycle in the graph
        for i in self.graph:  # iterate keys (vertices)
            for j in self.graph[i]:  # iterate values (values)
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
# g.addEdge(3, 4)
g.addEdge(1, 4)

result = g.isCyclic()
print(result)
