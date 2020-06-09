testGraph = {"A": ["B", "D"], "B": ["C"], "C": ["A", "E"], "D": ["E"], "E": []}

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

def find_all_paths(graph, start, end, path=[]):
	path.append(start)
	#path = path + [start]

	if start == end:
		return [path]
	
	paths = []

	for adjVertex in graph[start]:
		if adjVertex not in path:
			new_paths = find_all_paths(graph, adjVertex, end, path)
			for new_path in new_paths:
				paths.append(new_path)
	return paths


def find_shortest_path(graph, start, end, path=[]):
	path = path + [start]

	if start == end:
		return path
	
	shortest_path = []
	
	for adjVertex in graph[start]:
		if adjVertex not in path:
			new_path = find_shortest_path(graph, adjVertex, end, path)

			if new_path:
				if len(shortest_path) == 0 or len(shortest_path) > len(new_path):
					shortest_path = new_path
	return shortest_path	

result = find_shortest_path(testGraph, 'A', 'E')
print(result)