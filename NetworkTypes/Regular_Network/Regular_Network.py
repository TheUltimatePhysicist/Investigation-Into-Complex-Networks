import numpy as np


# Create an adjacency matrix which corresponds to a regular network.

def GenerateAdjacencyMatrix(numberOfNodes):
    
    # Setting all values to 1 in the matrix implies every node is linked to
    # another node, hence the degree is equal to the number of nodes also.
    
    adjacencyMatrix = np.ones((numberOfNodes, numberOfNodes))
    
    for i in range(0, numberOfNodes):
        adjacencyMatrix[i, i] = 0
    
    return adjacencyMatrix

