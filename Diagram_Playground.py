import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from NetworkTypes.Regular_Network import Regular_Network
from NetworkTypes.Random_Network import Random_Network
from NetworkTypes.SmallWorld_Network import SmallWorld_Network
from NetworkTypes.ScaleFree_Network import ScaleFree_Network

#import Network_Analysis_Functions


# Define the number of nodes.
'''
adjacencyMatrix = Random_Network.GenerateAdjacencyMatrix(20, 0.25)

G = nx.from_numpy_matrix(adjacencyMatrix)

#
plt.figure()

#nx.draw(G)# with_labels = True, font_weight = 'bold')
print(nx.number_of_edges(G))
d = nx.degree(G)
d = [(d[node]+1) * 20 for node in G.nodes()]
nx.draw(G, node_size=d, alpha=0.5)


plt.show()
'''


G = nx.watts_strogatz_graph(50, 5, 0.2)
print(nx.number_of_edges(G))

plt.figure()

d = nx.degree(G)
d = [(d[node]+1) * 20 for node in G.nodes()]

nx.draw_spring(G, node_size=d, alpha=0.5)
plt.show()


'''
G = nx.barabasi_albert_graph(50, 1)
print(nx.number_of_edges(G))

plt.figure()

d = nx.degree(G)
d = [(d[node]+1) * 20 for node in G.nodes()]

nx.draw(G, node_size=d, alpha=0.5)
plt.show()
'''
