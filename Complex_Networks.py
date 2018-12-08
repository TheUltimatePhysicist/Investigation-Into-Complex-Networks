import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import Regular_Network
import Random_Network
import SmallWorld_Network
#import ScaleFree_Network

import Network_Analysis

# Define the number of nodes.

numberOfNodes = 100


# Define the adjacency matrix.

adjacencyMatrix_RegularNetwork = Regular_Network.GenerateAdjacencyMatrix(numberOfNodes)
adjacencyMatrix_RandomNetwork = Random_Network.GenerateAdjacencyMatrix(numberOfNodes, 0.5)
adjacencyMatrix_SmallWorldNetwork = SmallWorld_Network.GenerateAdjacencyMatrix(numberOfNodes, 10, 0.5)


# Create a networkx graph.

G_RegularNetwork = nx.from_numpy_matrix(adjacencyMatrix_RegularNetwork)
G_RandomNetwork = nx.from_numpy_matrix(adjacencyMatrix_RandomNetwork)
G_SmallWorldNetwork = nx.from_numpy_matrix(adjacencyMatrix_SmallWorldNetwork)


# Plot the regular networkx graph.

plt.figure("Regular Network")
nx.draw(G_RegularNetwork, with_labels = True, font_weight = 'bold')
plt.show()

# PLot the random networkx graph.

plt.figure("Random Network")
nx.draw(G_RandomNetwork, with_labels = True, font_weight = 'bold')
plt.show()

# PLot the small world networkx graph.

plt.figure("Small-World Network")
nx.draw(G_SmallWorldNetwork, with_labels = True, font_weight = 'bold')
plt.show()

# Determine whether the random networks follow a Poisson distribution.
#
# Note: For random complex networks, the degree distribution is a poisson
# distribution. Therefore we need to plot number of nodes vs the degree.

degreeArray = np.zeros((2, adjacencyMatrix_RandomNetwork.shape[0]))
     
for i in range(0, adjacencyMatrix_RandomNetwork.shape[0]):

    degreeArray[0, i] = i
    degreeOfNode = Network_Analysis.DegreeOfNode(adjacencyMatrix_RandomNetwork, i)
    degreeArray[1, degreeOfNode] += 1
    
plt.figure("Random Network Degree Distribution")
plt.plot(degreeArray[0, :], degreeArray[1, :])
plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Degree Distribution of Random Network (N = 100, p = 0.5)")
plt.show()


#node1 = 2
#node2 = 6
#pathLength = Network_Analysis.ShortestPathLength(adjacencyMatrix_SmallWorldNetwork, node1, node2)

#print ("Shortest path length between node ", node1, " and node ", node2, " = ", pathLength)



# Print the average degrees of the networks.
#averageDegreeOfRegularNetwork = Network_Analysis.AverageDegree(adjacencyMatrix_RegularNetwork)
#averageDegreeOfRandomNetwork = Network_Analysis.AverageDegree(adjacencyMatrix_RandomNetwork)
#averageDegreeOfSmallWorldNetwork = Network_Analysis.AverageDegree(adjacencyMatrix_SmallWorldNetwork)

#print (" ")
#print ("-----------------------------------------------------------------------")
#print ("Average degree of regular network = ", averageDegreeOfRegularNetwork)
#print ("Average degree of random network = ", averageDegreeOfRandomNetwork)
#print ("Average degree of small-world network = ", averageDegreeOfSmallWorldNetwork)


# Print the clustering coefficients of the networks.
#clusteringCoefficientOfRegularNetwork = Network_Analysis.AverageClusteringCoefficient(adjacencyMatrix_RegularNetwork)
#clusteringCoefficientOfRandomNetwork = Network_Analysis.AverageClusteringCoefficient(adjacencyMatrix_RandomNetwork)
#clusteringCoefficientOfSmallWorldNetwork = Network_Analysis.AverageClusteringCoefficient(adjacencyMatrix_SmallWorldNetwork)

#print (" ")
#print ("Average clustering coefficient of regular network = ", clusteringCoefficientOfRegularNetwork)
#print ("Average clustering coefficient of random network = ", clusteringCoefficientOfRandomNetwork)
#print ("Average clustering coefficient of small-world network = ", clusteringCoefficientOfSmallWorldNetwork)



