graph = {
    0: [1],
    1: [2],
    2: [0]
}

def DFS_Util(node, visited, recStack, path):
    visited.add(node)
    path.append(node)
    recStack.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:

            result = DFS_Util(
                neighbour,
                visited,
                recStack, 
                path
            )

            if result is not None:
                return result
        elif neighbour in recStack:
            cycle_start = path.index(neighbour)
            cycle = path[cycle_start:] + [neighbour]

            return cycle
    recStack.remove(node)
    path.pop()

    return None

def find_cycle():

    visited = set()
    recStack = set()

    for node in graph:
        if node not in visited:

            path = []

        cycle = DFS_Util(
            node,
            visited,
            recStack,
            path
        )

        if cycle is not None:
            return cycle
    
    return None

cycle = find_cycle()

if cycle is not None:

    print("Cycle detected!")

    print("Nodes in the cycle:", cycle)

else:

    print("No cycle detected.")