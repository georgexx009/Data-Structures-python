from constants import graphExample
from Graph import Graph
from utils import findAllPaths

g = Graph(graphExample)

result = findAllPaths(g, "a", "e")
print(result)