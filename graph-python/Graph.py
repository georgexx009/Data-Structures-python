class Graph:
	def __init__(self, graphDict={}):
		self.graphDict = graphDict

	def __getitem__(self, key):
		return self.graphDict[key]

	def getVertices(self):
		return list(self.graphDict.keys())

	def getEdges(self):
		edges = []
		for vertex in self.graphDict:
			for nextVertex in self.graphDict[vertex]:
				if {vertex, nextVertex} not in edges:
					edges.append({vertex, nextVertex})
		return edges

	def addVertex(self, newVertex):
		if newVertex not in self.graphDict:
			self.graphDict[newVertex] = []

	def addEdge(self, edge):
		edge = set(edge)
		(vertex1, vertex2) = tuple(edge)
		if vertex1 in self.graphDict:
			self.graphDict[vertex1].append(vertex2)
		else:
			self.graphDict[vertex1] = [vertex2]

	def hasKey(self, key):
		return key in self.graphDict