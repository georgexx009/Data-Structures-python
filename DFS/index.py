def DFS(graph, start_node, path=[]):
  path.append(start_node)
  adj_nodes = graph[start_node]
  for adj_node in adj_nodes:
    if adj_node not in path:
      path = DFS(graph, adj_node, path)      
  return path

graph = {
  "A": ["B", "D", "E"],
  "B": ["C"],
  "C": [],
  "D": [],
  "E": ["F"],
  "F": ["G"],
  "G": []
}

graph2 = {
  "A": ["B", "C"],
  "B": ["C", "D"],
  "C": ["F", "G"],
  "F": ["A"],
  "D": [],
  "G": []
}

result = DFS(graph2, "A")
print(result)

