# Graph
# Adjacency List
# Directed
# Acyclic
# Weighted

class AdjNode:
  def __init__(self, destination, weight):
    self.vertex = destination
    self.weight = weight
    self.next = None

  def __iter__(self):
    current = self.vertex
    while current:
      yield current
      current = self.next
    

class Graph:
  def __init__(self, n):
    self.vertices_num = n
    self.graph = [None] * self.vertices_num    

  def add_edge(self, src, dest, weight):
    node = AdjNode(dest, weight)
    node.next = self.graph[src]
    self.graph[src] = node

  def __getItem__(self, index):
    return self.graph[index]
 
  def print_graph(self):
    for i in range(self.vertices_num):
      print("Vertex {}".format(i))
      temp = self.graph[i]
      while temp:
        print("--> {}, {}".format(temp.vertex, temp.weight))
        temp = temp.next
      print("\n")

#graph = Graph(4)
#graph.add_edge(0, 1)
#graph.add_edge(0, 2)