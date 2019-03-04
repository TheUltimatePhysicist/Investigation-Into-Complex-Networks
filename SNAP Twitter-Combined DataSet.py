import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('twitter_combined.txt')

#SP = nx.spring_layout(G)

#plt.axis('off')

nx.draw_networkx(G, with_labels = False)
plt.show()


