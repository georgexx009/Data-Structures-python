from queue import PriorityQueue
from graphAdjList import Graph
#put(num, value)
#get()

g = Graph(5)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 5)
g.add_edge(1, 3, 1)
g.add_edge(3, 4, 3)


def dijkstra(g, n, s):
  visited = [False] * n
  dist = [float('inf')] * n
  dist[s] = 0
  pq = PriorityQueue()  
  pq.put((0, s))  
  
  while not pq.empty():
    minValue, index = pq.get()
    visited[index] = True

    adjNode = g.graph[index]
    while adjNode:
      if visited[adjNode.vertex]:
        continue

      newDist = dist[index] + adjNode.weight
      if newDist < dist[adjNode.vertex]:
        dist[adjNode.vertex] = newDist
        pq.put((newDist, adjNode.vertex))
      adjNode = adjNode.next
  return dist
    


  


result = dijkstra(g, 5, 0)
print(result)