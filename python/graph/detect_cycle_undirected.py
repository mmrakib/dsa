class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Graph:
    def __init__(self, vertices):
        self.edges = []
        self.num_vertices = vertices

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def detect_cycle(self):
        pass