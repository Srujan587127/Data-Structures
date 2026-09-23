graph1 = {
    0: [1,2],
    1: [0],
    2: [0]
}

graph2= {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

def DFS_Util(node, visited, graph):
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            DFS_Util(neighbour, visited, graph)

def count_components(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:

            DFS_Util(node, visited, graph)

            count +=1

    return count

def isCyclic_Util(node, visited, parent, graph):
    visited.add(node)

    for neighbour in graph[node]:

        if neighbour not in visited:
            if isCyclic_Util(neighbour, visited, node, graph):
                return True
            
        elif neighbour != parent:
            return True
        
    return False

def isCyclic(graph):

    visited = set()

    for node in graph:

        if node not in visited:

            if isCyclic_Util(node, visited, -1, graph):
                return True
            
    return False 

def isTree(graph):

    components = count_components(graph)

    if components > 1:
        return False
    
    if isCyclic(graph):
        return False
    
    return True

print("Graph 1: ", isTree(graph1))
print("Graph 2: ", isTree(graph2))

