import numpy as np
import random


# Create an adjacency matrix which corresponds to a random network.

def GenerateAdjacencyMatrix(numberOfNodes, probability):
    
    # Initialise an empty maxtrix.
    
    adjacencyMatrix = np.zeros((numberOfNodes, numberOfNodes))
    
    
    # Go through each lower diagonal element of the square matrix (do not want
    # to go through the same link twice).
    
    for i in range (0, numberOfNodes):
        for j in range (0, numberOfNodes):
            
            # Generate a random value between 0 to 1.
            
            randomValue = random.uniform(0, 1)
            
            # If in the lower diagonal, compare the probability and the given
            # threshold to determine if a link between the two nodes should be
            # made or not.
            
            if i > j:
                if randomValue >= probability:
                    adjacencyMatrix[i, j] = 1
                    adjacencyMatrix[j, i] = 1

    return adjacencyMatrix

