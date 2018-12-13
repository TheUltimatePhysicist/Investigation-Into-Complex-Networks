import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import Regular_Network
import Random_Network
import SmallWorld_Network
#import ScaleFree_Network

import Network_Analysis_Functions


# Define the number of nodes.

adjacencyMatrix = np.array([[0, 1, 1, 1],
                            [1, 0, 0, 0],
                            [1, 0, 0, 0],
                            [1, 0, 0, 0]])


G = nx.from_numpy_matrix(adjacencyMatrix)


plt.figure()
nx.draw(G, with_labels = True, font_weight = 'bold')
plt.show()





