import collections

# check the visited and unvisited nodes
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    # print(start)

    # is like use .difference(), create one set with elements of graph that are not in visited
    for nextVertex in graph[start] - visited:
        dfs(graph, nextVertex, visited)

    return visited


def bft(graph, start):
    # track the visited and unvisited nodes using queues
    seen, queue = set([start]), collections.deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


def findPath(graph, start, end, path=[]):
    # check if node is in the graph
    if not graph.hasKey(start):
        return None

    # add it first to graph, to be include in path answer
    # path = path + [start]
    path.append(start)

    # FOUND THE PATH!!
    if start == end:
        return path

    for node in graph[start]:
        # for avoid cycles
        if node not in path:
            newpath = findPath(graph, node, end, path)
            # when the path is found, it will return all the recursions
            # until first recursion call
            if newpath:
                return newpath

    # if in some step returns None, it will return until here,
    # to return None in the main call function
    return None


def findAllPaths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]
    if not graph.hasKey(start):
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            newpaths = findAllPaths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths




testGraph = {
	'A': ['B', 'D'],
	'B': ['C'],
	'C': ['A', 'E'],
	'D': ['E'],
	'E': []
}


def find_path(graph, start, end, path=[]):
	path.append(start)
	print(path)

	if start == end:
		return path

	for adjVertex in graph[start]:
		if adjVertex not in path:
			new_path = find_path(graph, adjVertex, end, path)

			if new_path:
				return new_path
	return None



