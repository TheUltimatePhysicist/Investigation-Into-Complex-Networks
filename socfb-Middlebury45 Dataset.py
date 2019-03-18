import networkx as nx
import matplotlib.pyplot as plt

# Number Of Nodes = 3075

G = nx.read_edgelist('NetworkRepository_Data/socfb-Middlebury45.txt')

print (len(G))
print (nx.number_of_edges(G))
print (nx.average_clustering(G))

plt.axis('off')

nx.draw_networkx(G, with_labels = False, node_size = 35)
plt.show()