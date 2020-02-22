import networkx as nx
import matplotlib.pyplot as plt

# # using networkx
# : for creation of graphs and manipulation of networks

# using pyplot from matplotlib
# : to give visual representation of graphs generated

g = nx.Graph()


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
        
    leng = nx.average_shortest_path_length(g)  # average length between all the nodes
    # print(leng)
    efficiency = 1 / (s * leng)

    return efficiency


e = cal_s(g)
# print(e)
print("efficiency of whole sysytem: ", e)

em = []  # em: Efficiency E(G)
effc = []  # effc: Efficiency of system after deleting a node (EffC)

for i in range(1, 9):
    h = g.copy()    # g.copy: 'copy' returns an independent shallow copy of the graph
    h.remove_node(i)    # h.remove_node: 'remove_node' Removes the node n and all adjacent edges
    em.append(cal_s(h))
    effc.append((e - cal_s(h)) / e)

print("efficiency of system after removing each node(1-8): ", em)
print("EffC(k) of the system after removing each node(1-8)", effc)
# Effc(k): Change in efficiency after removal of each node
