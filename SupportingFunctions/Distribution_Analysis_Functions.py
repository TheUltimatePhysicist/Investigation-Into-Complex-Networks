import scipy.misc
import scipy.special
import math as m
import numpy as np
import decimal

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


def DiracDeltaFunction(degreeArray, k, p):

    # j = degree array
    # k = number of neighbouring nodes.
    # n = summation index
    # p = probability



    returnArray = np.zeros(len(degreeArray))

    for j in range(len(degreeArray)):

        if j < k: 
            returnArray[j] = 0
        else:

            #
            summation = 0
            summationLimit = np.min((j - k, k))

            for n in range(int(summationLimit)):

                binomialCoefficient = scipy.misc.comb(k, n)

                decimal.getcontext().prec = 100


                numerator = (( decimal.Decimal(p*k)  )**(  decimal.Decimal(j - k - n)  ))
                denominator = decimal.Decimal(m.factorial(int(j - k - n)))

                fraction = decimal.Decimal(numerator) / decimal.Decimal(denominator)

                summation += decimal.Decimal(  binomialCoefficient * ((1 - p)**n) * (p**(k - n))   ) * fraction *    decimal.Decimal(  np.exp(-1*p*k)  )
    
            returnArray[j] = summation

    return returnArray


