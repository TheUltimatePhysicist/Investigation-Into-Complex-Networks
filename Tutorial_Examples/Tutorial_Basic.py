import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# Graph is a collection of nodes (vertices) along with
# indentified pairs of nodes (called edges, links, etc).

G = nx.Graph()


# Add a node at a time.

G.add_node(1)


# Add a list of nodes.

G.add_nodes_from([2, 3])


# Pass in nodes with node attributes.

H = nx.path_graph(10)
G.add_nodes_from(H)

G.add_node(H)


# Adding edges at a time.

G.add_edge(1, 2)
e = (2, 3)

G.add_edge(*e)  # unpack edge tuple *.


# Add a list of edges.

G.add_edges_from([(1, 2), (1, 3)])


# Pass in edges with edge attributes.

#G.add_edges_from(H.edges)


# Clear all existing nodes/edges.

G.clear()


# Following nodes/edges included while all previous ignored.

G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")  # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')


# Plot the generated graph

plt.figure()
nx.draw(G, with_labels = True, font_weight = 'bold')


