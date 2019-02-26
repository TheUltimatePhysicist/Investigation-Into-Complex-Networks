import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('facebook_combined.txt')

plt.figure()
nx.draw(G, with_labels = True, font_weight = 'bold')
plt.show()

