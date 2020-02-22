import networkx as nx

# using networkx
# : for creation of graphs and manipulation of networks

g = nx.Graph()

# g: empty graph

def add(g, i, j, w):
    """
    :param g: empty graph
    :param i: node i
    :param j: node j
    :param w: weight b/w node i and j
    :return: graph formed with added edges
    """
    g.add_edge(i, j, weight=w)


# Evaluating sum of the average degree of nodes with below provided data
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
# networkx.average_shortest_path_length(graph_name): Returns the average shortest path length
