import scipy
import math as m
import numpy as np

from SupportingFunctions import Network_Analysis_Functions


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


def StraightLine(xArray, gradient, intercept):
    
    returnedArray = np.zeros_like(xArray)

    for i in range(len(returnedArray)):
        if (np.isfinite(xArray[i])  == False):
            xArray[i] = 0
        
        returnedArray[i] = (gradient * xArray[i]) + intercept

    return returnedArray


def ExponentialTail(degreeArray, gammaValue):

    return degreeArray**(gammaValue)


def LogCurve(xArray, coefficient):
    return coefficient*(np.log(xArray))


def DiracDeltaFunction():

    
