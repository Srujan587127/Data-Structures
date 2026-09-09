# Count neighbours

graph = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4]}

def count_neighbours(graph, node):
    if node not in graph:
        return 0

    neighbours = graph[node]
    count = len(neighbours)
    return count

result = count_neighbours(graph, 2)
print("Number of neighbours of Node 2: ", result)