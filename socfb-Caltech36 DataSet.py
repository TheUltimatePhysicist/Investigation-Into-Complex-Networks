import networkx as nx
import matplotlib.pyplot as plt
from scipy.io import mmread

#rawData = mmread("socfb-Caltech36.mtx")

G = nx.read_edgelist('NetworkRepository_Data/socfb-Caltech36.txt')

print (len(G))
print (nx.number_of_edges(G))
print (nx.average_clustering(G))

#print (rawData)

plt.axis('off')

nx.draw_networkx(G, with_labels = False, node_size = 35)
plt.show()

