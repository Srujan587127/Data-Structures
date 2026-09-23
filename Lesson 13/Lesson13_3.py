graph = {
    0:[1, 2],
    1:[0, 2],
    2:[1, 0]
}

def DFS_Util(node, visited, parent):

    visited.add(node)

    for neighbour in graph[node]:

        if neighbour not in visited:
              
            if DFS_Util(neighbour, visited, node):
                return True
        
        elif neighbour != parent:
            return True
        
    return False

def isCyclic():

    visited = set()
    for node in graph:

        if node not in visited:

            if DFS_Util(node, visited, -1):
                return True
            
    return False

if isCyclic():
    print("Cyclic detected!")
else:
    print("No cycle detected.")

             
        

