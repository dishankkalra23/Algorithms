import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

def add(g, i, j, w):
    g.add_edge(i, j, weight=w)

add(g, 1, 2, 2)
add(g, 2, 3, 1)
add(g, 1, 4, 1)
add(g, 1, 5, 1)
add(g, 5, 4, 1)
add(g, 4, 3, 1)
add(g, 4, 7, 2)
add(g, 4, 6, 1)
add(g, 3, 6, 2)
add(g, 6, 7, 1)
add(g, 4, 2, 1)
add(g, 4, 8, 1)
add(g, 8, 7, 1)

print(nx.average_shortest_path_length(g))