class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in range(n)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, node, visited):
        visited[node] = True
        for neighbour in self.adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited)

    def count_components(self):
        visited = [False] * self.n
        count = 0

        for i in range(self.n):
            if not visited[i]:
                count += 1
                self.dfs(i, visited)

        return count


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(2, 3)
print(g.count_components())