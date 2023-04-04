import networkx as nx
import matplotlib.pyplot as plt
from WeightedDirectedGraph import Graph

def visualize_shortest_path(graph, start):
    # create a networkx graph object
    G = nx.DiGraph()
    for vertex in graph.graph:
        G.add_node(vertex)
        for neighbor in graph.get_neighbors(vertex):
            G.add_edge(vertex, neighbor, weight=graph.graph[vertex][neighbor])

    # find the shortest paths from the starting vertex to all other vertices
    shortest_paths = nx.multi_source_dijkstra(G, {start})
    # create a list of edges in the shortest paths
    shortest_path_edges = []
    for vertex in shortest_paths[1]:
        shortest_path_edges.extend([(v, vertex) for v in shortest_paths[1][vertex][:-1]])

    # set the colors of the edges
    edge_colors = ['red' if edge in shortest_path_edges else 'black' for edge in G.edges()]

    # draw the graph
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_labels(G, pos)
    plt.show()
