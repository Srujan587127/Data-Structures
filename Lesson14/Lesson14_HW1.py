class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_safe_util(self, v, visited, rec_stack, safe):
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.graph[v]:
            if rec_stack[neighbour]:
                return False
            if visited[neighbour] and not safe[neighbour]:
                return False
            if not visited[neighbour]:
                if not self.is_safe_util(neighbour, visited, rec_stack, safe):
                    return False

        rec_stack[v] = False
        safe[v] = True
        return True

    def safe_nodes(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        safe = [False] * self.V

        for v in range(self.V):
            if not visited[v]:
                self.is_safe_util(v, visited, rec_stack, safe)

        return [v for v in range(self.V) if safe[v]]


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(2, 3)
g.add_edge(3, 2)
print("Safe nodes:", g.safe_nodes())

g2 = Graph(5)
g2.add_edge(0, 1)
g2.add_edge(2, 3)
g2.add_edge(3, 2)
g2.add_edge(4, 2)
print("Safe nodes:", g2.safe_nodes())