import scipy
import math as m
import numpy as np

import Network_Analysis_Functions


#--------------------------------------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------------------------------------

def DegreeDistributionData(adjacencyMatrix):
    
    array = np.zeros((2, adjacencyMatrix.shape[0]))
     
    for i in range(0, adjacencyMatrix.shape[0]):

        array[0, i] = i
        degreeOfNode = Network_Analysis_Functions.DegreeOfNode(adjacencyMatrix, i)
        array[1, degreeOfNode] += 1
    
    return array


def PoissonDistribution(degreeArray, lambdaMeanValue):

    return np.exp((degreeArray * np.log(lambdaMeanValue)) - lambdaMeanValue - scipy.special.gammaln(degreeArray + 1))
