class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def addEdge(self, vertex, weight = 0):
        self.edges[vertex] = weight

    def getEdges(self):
        return list(self.edges)
