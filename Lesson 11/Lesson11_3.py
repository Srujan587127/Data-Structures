#Isolated Nodes

graph = {
    0 : [1],
    1 : [0, 2],
    2 : [1],
    3: [],
    4 : []
}

def find_isolated(graph):
    isolated = []
    for node in graph:
        if len(graph[node]) == 0:
            isolated.append(node)

    return isolated

result = find_isolated(graph)
print("Isolated Nodes: ", result)