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
    
    clusteringArray = np.zeros(0)
    for i in range(0, adjacencyMatrix.shape[0]):
        
        if(adjacencyMatrix[node, i] > 0):
            clusteringArray = np.append(clusteringArray, i)
    
    
    # If there is only one neighbor or none, then there cannot be a 
    # clustering coefficient.
    
    if(clusteringArray.shape[0] <= 1):
        return 0
    
    
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


#############################################################################
# Function to find the neighboring nodes of a node.

def NeighboringNodes(adjacencyMatrix, node):
    
    clusteringArray = np.zeros(0)
    for i in range(0, adjacencyMatrix.shape[0]):
        
        if(adjacencyMatrix[np.int(node), i] > 0):
            clusteringArray = np.append(clusteringArray, i)
    
    return clusteringArray


#############################################################################
# Function to determine if a value is present within an array.

def IsValuePresent(array, value):
    
    for i in range(0, array.shape[0]):
        
        if(array[i] == value):
            return 1
    
    return 0
    

#############################################################################
# Function to determine the shortest path length of 2 nodes in a network.

def ShortestPathLength(adjacencyMatrix, node1, node2, pathLength = 0, isDirected = 'false'):
    
    # 
    neighborArray = NeighboringNodes(adjacencyMatrix, node1)
    
    if(neighborArray.shape[0] == 0):
        return 0


    # ATTEMPT at recursive function.
    pathLength += 1
    
    if(IsValuePresent(neighborArray, node2) == 1):
        return pathLength
    
    for i in range(0, (neighborArray.shape[0])):
        
        ShortestPathLength(adjacencyMatrix, neighborArray[i], node2, pathLength)
        
    return pathLength

    
    """
    # 
    pathLength += 1
    for i in range(0, neighborArray.shape[0]):
        
        if(neighborArray[i] == node2):
            return pathLength
    
    
    pathLength += 1
    for i in range(0, neighborArray.shape[0]):
        
        neighborOfNeighborArray = NeighboringNodes(adjacencyMatrix, neighborArray[i])
        
        for i in range(0, neighborOfNeighborArray.shape[0]):
        
            if(neighborOfNeighborArray[i] == node2):
                return pathLength
    
    
    
    
    
    # 
    
    neighborArray_1 = np.copy(neighborArray)
    neighborArray_2 = np.zeros(0)
    
    for FAIL in range(0, (adjacencyMatrix.shape[0])**2):
        
        
        pathLength += 1
        
        if(IsValuePresent(neighborArray_1, node2)):
            return pathLength
        
        
        pathLength += 1
        
        for i in range(0, neighborArray.shape[0]):
        
            neighborArray_2 = NeighboringNodes(adjacencyMatrix, neighborArray[i])
            
            if(IsValuePresent(neighborArray_2, node2)):
                return pathLength
                
    return 0
    """
    
    
    
    







