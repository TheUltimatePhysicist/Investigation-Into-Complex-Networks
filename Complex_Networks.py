import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import Regular_Network
import Random_Network
#import SmallWorld_Network

import Network_Analysis


# Define the number of nodes.

numberOfNodes = 20


# Define the adjacency matrix.

adjacencyMatrix_RegularNetwork = Regular_Network.GenerateAdjacencyMatrix(numberOfNodes)
adjacencyMatrix_RandomNetwork = Random_Network.GenerateAdjacencyMatrix(numberOfNodes, 0.5)


# Create a networkx graph.

G_RegularNetwork = nx.from_numpy_matrix(adjacencyMatrix_RegularNetwork)
G_RandomNetwork = nx.from_numpy_matrix(adjacencyMatrix_RandomNetwork)


# Plot the regular networkx graph.

plt.figure("Regular Network")
nx.draw(G_RegularNetwork, with_labels = True, font_weight = 'bold')


# PLot the random networkx graph.

plt.figure("Random Network")
nx.draw(G_RandomNetwork, with_labels = True, font_weight = 'bold')
