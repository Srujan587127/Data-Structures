class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in range(n)]

    def createEdge(self, x, y):
        self.adj[x - 1].append(y - 1)
        self.adj[y - 1].append(x - 1)

    def isConnected(self, start, end):
        if start == end:
            return True
        visited = [False] * self.n
        queue = []
        queue.append(start)
        visited[start] = True

        while len(queue) > 0:
            s = queue.pop(0)

            for node in self.adj[s]:
                if node == end:
                    return True
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True

        return False


graph = Graph(5)
graph.createEdge(1, 2)
graph.createEdge(1, 3)
graph.createEdge(2, 4)
print(graph.isConnected(0, 3))
print(graph.isConnected(0, 4))