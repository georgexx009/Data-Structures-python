from Vertex import Vertex
from Graph import Graph

vertex1 = Vertex(1)
vertex2 = Vertex(2)
vertex3 = Vertex(3)

graph = Graph()

graph.addVertex(vertex1)
graph.addVertex(vertex2)
graph.addVertex(vertex3)

graph.addEdge(vertex1, vertex2)
graph.addEdge(vertex2, vertex3)
print(graph.findPath2(vertex1, vertex3))
