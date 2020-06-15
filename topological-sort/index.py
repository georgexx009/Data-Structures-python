from AdjList import Graph

DAG = {
  'A': ['D'],
  'C': ['A', 'B'],
  'E': ['A', 'D', 'F'],
  'B': ['D'],
  'D': ['H', 'G'],
  'F': ['K', 'J'],
  'H': ['J', 'I'],
  'G': ['I'],
  'K': ['J'],
  'J': ['M', 'L'],
  'I': ['L'],
  'L': [],
  'M': []
}

def dfs(at, visited, visitedNodes, graph):
  if at not in visited:  
    visited.add(at)  
  edges = graph[at]
  for edge in edges:
    if edge not in visited:
      dfs(edge, visited, visitedNodes, graph)
  visitedNodes.append(at)

def dfs2(i, at, visited, ordering, graph):
  if at not in visited:
    visited.add(at)
  edges = graph[at]
  for edge in edges:
    if edge not in visited:
      i = dfs2(i, edge, visited, ordering, graph)
  ordering[i] = at
  return i - 1



def topSort(graph, numOfVertices):
  visited = set()
  ordering = [0 for i in range(numOfVertices)]
  i = numOfVertices - 1  #index for ordering array
  
  for at in graph:
    if at not in visited:
      visitedNodes = []
      dfs(at, visited, visitedNodes, graph)
      for nodeId in visitedNodes:
        ordering[i] = nodeId
        i = i - 1
  return ordering



result = topSort(DAG, 13)
print(result)
