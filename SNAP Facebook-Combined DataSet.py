import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('SNAP_Data/facebook_combined.txt')

SP = nx.spring_layout(G)

plt.axis('off')

nx.draw_networkx(G, pos = SP, with_labels = False, node_size = 35)
plt.show()

