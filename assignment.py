import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        self.graph.setdefault(u, []).append((v, weight))
        self.graph.setdefault(v, []).append((u, weight))

    def dijkstra(self, start):
        queue = [(0, start)]
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        previous = {vertex: None for vertex in self.graph}

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

        return distances, previous

    def final_path(self, previous, start, end):
        path, current = [], end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path

def main():
    graph = Graph()
    num_edges = int(input("Enter the number of bus routes (edges): "))
    
    for _ in range(num_edges):
        u, v, weight = input("Enter bus route (start stop, end stop, distance): ").split()
        graph.add_edge(u, v, int(weight))

    start = input("Enter the starting bus stop: ")

    distances, previous = graph.dijkstra(start)

    for vertex in graph.graph:
        if distances[vertex] == float('infinity'):
            print(f"No path exists from {start} to {vertex}.")
        else:
            path = graph.final_path(previous, start, vertex)
            print(f"The shortest path from {start} to {vertex} is: {' -> '.join(path)} with a distance of {distances[vertex]}.")

if __name__ == "__main__":
    main()
