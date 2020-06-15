class AdjNode:
	def __init__(self, data):
		self.vertex = data
		self.next = None

class Graph:
	def __init__(self, vertices_num):
		self.vertices_num = vertices_num
		self.graph = [None] * self.vertices_num
	
	def add_edge(self, src, dest):
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		#node = AdjNode(src)
		#node.next = self.graph[dest]
		#self.graph[dest] = node

	def print_graph(self):
		for i in range(self.vertices_num):
			print("Vertex {}".format(i))
			temp = self.graph[i]
			while temp:
				print("--> {}".format(temp.vertex))
				temp = temp.next
			print("\n")

#graph = Graph(4)
#graph.add_edge(0, 1)
#graph.add_edge(0, 2)
#print(graph.print_graph())
