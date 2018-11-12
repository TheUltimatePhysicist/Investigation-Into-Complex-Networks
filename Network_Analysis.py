import numpy as np


#############################################################################
# Function to determine the number of nodes.

def NumberOfNodes(adjacencyMatrix):
    
    return adjacencyMatrix.shape[0]


#############################################################################
# Function to determine the number of links/vertices.

def NumberOfLinks(adjacencyMatrix, isDirected = 'false'):

    linksNumber = 0
    
    # Loop to count all occurences of a number greater than 0 (link) and
    # continually sum.
    
    for i in range(0, adjacencyMatrix.shape[0]):
        for j in range(0, adjacencyMatrix.shape[1]):
            
            if(adjacencyMatrix[i, j] > 0):
                linksNumber += 1
    
    # If the matrix is undirected then the total number of links must be
    # halved due to links being doubly recorded.
    
    if(isDirected == 'false'):
        return linksNumber / 2
    
    # Else return the summation value.
    
    return linksNumber


#############################################################################
# Function to determine the degree of a node within a network.

def DegreeOfNode(adjacencyMatrix, node):
    
    sum = 0
    
    for i in range(0, adjacencyMatrix.shape[0]):
        
        if(adjacencyMatrix[node, i] > 0):
            sum += 1
    
    return sum


#############################################################################
# Function to determine the average degree within a network.

def AverageDegree(adjacencyMatrix):
    
    degreeArray = np.zeros(adjacencyMatrix.shape[0])
    
    for i in range(0, adjacencyMatrix.shape[0]):
        degreeArray[i] = DegreeOfNode(adjacencyMatrix, i)

    return np.mean(degreeArray)


#############################################################################
# Function to determine the clustering coefficient of a node.

def ClusteringCoefficientOfNode(adjacencyMatrix, node):
    
    # Loop through the adjacency matrix for a node, recording the nodes which
    # are connected to the given node.
    
    clusteringArray = ([])
    for i in range(0, adjacencyMatrix.shape[0]):
        
        if(adjacencyMatrix[node, i] > 0):
            clusteringArray = np.append(clusteringArray, i)
    
    # Sum all the number of links between the neighbors of the selected node.
    
    overallSum = 0
    
    for i in range(0, clusteringArray.shape[0]):
        
        for j in range(0, adjacencyMatrix.shape[0]):
            
            for k in range(0, clusteringArray.shape[0]):
                
                if((adjacencyMatrix[np.int(clusteringArray[i]), j] > 0) & (j == clusteringArray[k])):
                    overallSum += 1
                    
    # Now divide the overall number of links (between neighbors) by the number
    # of neighbors (minus 1, due to original node being included).
    #
    # Then return this modified overallSum by the number of neighbors of the
    # original node.
                    
    overallSum = overallSum / (np.float(clusteringArray.shape[0]) - 1)
    
    return overallSum / np.float(clusteringArray.shape[0])



#############################################################################
# Function to determine the clustering coefficient of a network.

def AverageClusteringCoefficient(adjacencyMatrix):
    
    clusteringCoefficientArray = np.zeros(adjacencyMatrix.shape[0])
    
    for i in range(0, adjacencyMatrix.shape[0]):
        clusteringCoefficientArray[i] = ClusteringCoefficientOfNode(adjacencyMatrix, i)
    
    return np.mean(clusteringCoefficientArray)



