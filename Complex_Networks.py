import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import Regular_Network
#import Random_Network
#import SmallWorld_Network


# Define the number of nodes.

numberOfNodes = 20


# Define the adjacency matrix.

adjacencyMatrix_RegularNetwork = Regular_Network.GenerateAdjacencyMatrix(numberOfNodes)


# Create a networkx graph.

G_RegularNetwork = nx.from_numpy_matrix(adjacencyMatrix)


# Plot the networkx graph.

plt.figure()
nx.draw(G_RegularNetwork, with_labels = True, font_weight = 'bold')
