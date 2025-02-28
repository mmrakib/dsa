class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, start, end):
        dists = [float('inf')] * self.num_vertices
        dists[start] = 0

        for _ in range(self.num_vertices - 1):
            for u, v, weight in self.edges:
                if dists[u] != float('inf') and dists[u] + weight < dists[v]:
                    dists[v] = dists[u] + weight

        for u, v, weight in self.edges:
            if dists[u] != float('inf') and dists[u] + weight < dists[v]:
                return None
            
        return dists[end]
    
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

src = 0
dest = 3
result = g.bellman_ford(src, dest)

print(result)