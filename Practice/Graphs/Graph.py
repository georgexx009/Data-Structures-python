class Graph:
    def __init__(self, directed = False):
        self.directed = directed
        self.graphDict = {}

    def addVertex(self, vertex):
        self.graphDict[vertex.value] = vertex

    def addEdge(self, fromVertex, toVertex, weight = 0):
        self.graphDict[fromVertex.value].addEdge(toVertex.value, weight)

    def findPath(self, startVertex, endVertex):
        start = [startVertex.value]
        seen = {}

        while len(start):
            currentVertex = start.pop(0)
            seen[currentVertex] = True

            if currentVertex == endVertex.value:
                return True
            else:
                verticesToVisit = self.graphDict[currentVertex].getEdges()
                start += [vertex for vertex in verticesToVisit if vertex not in seen]
        return False

    def findPath2(self, startVertex, endVertex):
        start = [startVertex.value]
        seen = set()

        while len(start):
            currentVertex = start.pop(0)
            seen.add(currentVertex)

            if currentVertex == endVertex.value:
                return True
            else:
                verticesToVisit = self.graphDict[currentVertex].getEdges()
                start += [vertex for vertex in verticesToVisit if vertex not in seen]
        return False
