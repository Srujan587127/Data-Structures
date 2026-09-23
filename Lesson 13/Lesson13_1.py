graph ={
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3]
}

visited = set()

def DFS_Util(node, temp_list):
    visited.add(node)

    temp_list.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            DFS_Util(neighbour, temp_list)

largest_size = 0

for node in graph:

    if node not in visited:
        temp_list =[]
        DFS_Util(node, temp_list)

        if len(temp_list) > largest_size:
            largest_size = len(temp_list)

print("Largest Connected Component Size", largest_size)