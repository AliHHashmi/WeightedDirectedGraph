import networkx as nx
import matplotlib.pyplot as plt
from WeightedDirectedGraph import Graph
from VisualizeGraph import visualize_graph
from VisualizeDjikstra import visualize_shortest_path

# create a new graph
g = Graph()

# add some vertices and edges to the graph
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('C', 'E', 10)
g.add_edge('D', 'E', 2)

start_vertex = 'A'

# visualize the graph
visualize_graph(g)


# find the shortest path from vertex 'A' to all other vertices in the graph
shortest_paths = g.dijkstra('A')
print(shortest_paths)

# visualize the shortest path from vertex 'A' to all other vertices in the graph
visualize_shortest_path(g, 'A')

# find the shortest paths from the starting vertex to all other vertices using Bellman-Ford algorithm
start_vertex = 'A'
distances = g.bellman_ford(start_vertex)

# print the distances from the starting vertex to all other vertices
for vertex in distances:
    print(f"Distance from {start_vertex} to {vertex}: {distances[vertex]}")