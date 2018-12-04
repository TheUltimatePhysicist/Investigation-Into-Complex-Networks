import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import Regular_Network
import Random_Network
#import SmallWorld_Network
#import ScaleFree_Network

import Network_Analysis


# Define the number of nodes.

numberOfNodes = 100


# Define the adjacency matrix.

adjacencyMatrix_RegularNetwork = Regular_Network.GenerateAdjacencyMatrix(numberOfNodes)
adjacencyMatrix_RandomNetwork = Random_Network.GenerateAdjacencyMatrix(numberOfNodes, 0.50)


# Create a networkx graph.

G_RegularNetwork = nx.from_numpy_matrix(adjacencyMatrix_RegularNetwork)
G_RandomNetwork = nx.from_numpy_matrix(adjacencyMatrix_RandomNetwork)


# Plot the regular networkx graph.

plt.figure("Regular Network")
nx.draw(G_RegularNetwork, with_labels = True, font_weight = 'bold')


# PLot the random networkx graph.

plt.figure("Random Network")
nx.draw(G_RandomNetwork, with_labels = True, font_weight = 'bold')


# Determine whether the random networks follow a Poisson distribution.
#
# Note: For random complex networks, the degree distribution is a poisson
# distribution. Therefore we need to plot number of nodes vs the degree.

degreeArray = np.zeros((2, adjacencyMatrix_RandomNetwork.shape[0]))

for i in range(0, adjacencyMatrix_RandomNetwork.shape[0]):

    #     
    degreeArray[0, i] = i
    
    
for i in range(0, adjacencyMatrix_RandomNetwork.shape[0]):
    
    degreeOfNode = Network_Analysis.DegreeOfNode(adjacencyMatrix_RandomNetwork, i)
    degreeArray[1, degreeOfNode] += 1    
    
    """
    # 
    summation = 0
    for j in range(0, adjacencyMatrix_RandomNetwork.shape[0]):
        
        if()
        summation += 
    """

plt.figure("Random Network Degree Distribution")
plt.plot(degreeArray[0, :], degreeArray[1, :])
plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Degree Distribution of Random Network (N = 100, p = 0.5)")
