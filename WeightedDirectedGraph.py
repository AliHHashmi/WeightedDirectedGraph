import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.add_vertex(start)
        if end not in self.graph:
            self.add_vertex(end)
        self.graph[start][end] = weight

    def get_neighbors(self, vertex):
        return self.graph[vertex].keys()

    def dijkstra(self, start):
        # initialize distances to all vertices as infinity except start vertex which is 0
        dist = {v: float('inf') for v in self.graph}
        dist[start] = 0
        # create a set of unvisited vertices
        unvisited = set(self.graph.keys())
        while unvisited:
            # find the vertex with the smallest distance from start
            current = min(unvisited, key=lambda v: dist[v])
            unvisited.remove(current)
            # check if the path to this vertex is shorter through the current vertex
            for neighbor in self.get_neighbors(current):
                new_dist = dist[current] + self.graph[current][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
        return dist

    def bellman_ford(self, start):
        # initialize distances to all vertices as infinity, except for start vertex
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0

        # relax all edges v-1 times
        for i in range(len(self.graph) - 1):
            for u in self.graph:
                for v in self.graph[u]:
                    if distances[u] + self.graph[u][v] < distances[v]:
                        distances[v] = distances[u] + self.graph[u][v]

        # check for negative weight cycles
        for u in self.graph:
            for v in self.graph[u]:
                if distances[u] + self.graph[u][v] < distances[v]:
                    raise ValueError('Graph contains a negative weight cycle')

        return distances