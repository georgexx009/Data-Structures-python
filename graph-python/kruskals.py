from collections import defaultdict


class Graph:
	def __init__(self, numVertices):
		self.numVertices = numVertices
		self.graph = []  # the index will be the node/vertex

	def addEdge(self, start, end, weight):
		self.graph.append([start, end, weight])
	
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	def union(self, parent, rank, x, y):
		#xroot = self.find(parent, x)
		#yroot = self.find(parent, y)
		xroot = x
		yroot = y

		#attach smaller rank tree under root of
		#high rank tree
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	def kruskal(self):
		result = []
		i = 0 #index for sorted edges
		e = 0 #index for result

		#order the edges from shorter to largest
		self.graph = sorted(self.graph, key=lambda item: item[2])		

		parent = [] #disjoint-set
		rank = []

		for node in range(self.numVertices):
			parent.append(node)
			rank.append(0)
		
		while e < self.numVertices - 1:
			u, v, w = self.graph[i]
			i = i + 1

			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				e = e + 1
				result.append([u,v,w])
				self.union(parent, rank, x, y)
		
		print(result)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.kruskal()


class Graph2:
	def __init__(self, numVertices):
		self.numVertices = numVertices
		self.graph = []

	def addEdge(self, u,v,w):
		self.graph.append([u,v,w])

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent[i])

	def union(self, parent, rank, x, y):
		xroot = self.find(x)
		yroot = self.find(y)

		if rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		elif rank[yroot] > rank[xroot]:
			parent[xroot] = yroot
		else:
			parent[xroot] = yroot

	
	def kruskal(self):
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		rank = []

		for i in range(self.numVertices):
			parent.append(i)
			rank.append(0)

		result = []
		e = 0
		i = 0

		while e < self.numVertices - 1:
			u, v, w = self.graph[i]
			i += 1

			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				result.append([u,v,w])
				e += 1
				self.union(parent, rank, x, y)


