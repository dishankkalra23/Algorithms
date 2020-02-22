import networkx as nx
import matplotlib.pyplot as plt

# using networkx
# : for creation of graphs and manipulation of networks

# using pyplot from matplotlib
# : to give visual representation of graphs generated

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


def cal_s(g: nx.Graph):
    """

    :param g: graphs generated
    :return: sum of the average degree of nodes
    """
    s = 0
    # s : initialising average degree of nodes
    for node in g.nodes:
        neigh = [n for n in g.neighbors(node)]  # neigh : Neighbours of the node in a graph
        # print(neigh)

        s_temp = 0
        for i in neigh:
            w = g.get_edge_data(node, i)['weight']
            # w: getting weights between node i and node j where node i varies while node j is fixed
            s_temp += 1 / w
            # s_temp : sum of the weights of between i and j

        s += s_temp * (1 / len(neigh))  # Finding average of s
    return s


s = cal_s(g)  # s: sum of average degree of nodes

print(s)
