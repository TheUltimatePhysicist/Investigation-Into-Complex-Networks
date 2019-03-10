import networkx as nx
import matplotlib.pyplot as plt

# Number Of Nodes = 4047

G = nx.read_edgelist('NetworkRepository_Data/socfb-Howard90.txt')

print (len(G))
print (nx.number_of_edges(G))
print (nx.average_clustering(G))

plt.axis('off')

nx.draw_networkx(G, with_labels = False, node_size = 35)
plt.show()
