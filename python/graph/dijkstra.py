import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list:
            self.adj_list[u] = []

        if v not in self.adj_list:
            self.adj_list[v] = []

        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start, end):
        pq = [(0, start)]
        dists = {node: float('inf') for node in self.adj_list}
        prev_nodes = {node: None for node in self.adj_list}

        dists[start] = 0

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)

            for neighbor, weight in self.adj_list[curr_node]:
                new_dist = curr_dist + weight

                if new_dist < dists[neighbor]:
                    dists[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

                    prev_nodes[neighbor] = curr_node

        path = []
        curr_node = end
        while curr_node != None:
            path.append(curr_node)
            curr_node = prev_nodes[curr_node]
        path.reverse()

        return path if path[0] == start else []
        
graph = Graph()
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 1)
graph.add_edge("C", "B", 2)
graph.add_edge("B", "D", 1)
graph.add_edge("C", "D", 5)

start_node = "A"
end_node = "D"

shortest_path = graph.dijkstra(start_node, end_node)

print("shortest path: ", shortest_path)