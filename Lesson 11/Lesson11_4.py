
graph = {1: [2, 3], 2: [1, 4, 5], 3: [1, 6], 4: [2], 5: [2], 6:[3]}

def count_neighbours(graph, node):
    if node not in graph:
        return 0

    neighbours = graph[node]
    count = len(neighbours)
    return count

result = count_neighbours(graph, 3)
print("Number of neighbours of Node 3: ", result)