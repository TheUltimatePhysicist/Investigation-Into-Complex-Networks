import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import Random_Network
import Network_Analysis_Functions
import Distribution_Analysis_Functions


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed number of nodes and a changing probability, to determine how the
# degree distribution changes with probability.
#--------------------------------------------------------------------------------------------------
#
# Initialise the N and probability array.
N = 100
P_Array = np.arange(0.05, 1.05, 0.05)


# Create the adjacency matrices for varying N.
adjacencyMatrices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, P_Array.shape[0]):
    adjacencyMatrices[i] = Random_Network.GenerateAdjacencyMatrix(N, P_Array[i])


# Extract the degree distribution data.
degreeDistributions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, P_Array.shape[0]):
    degreeDistributions[i] = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrices[i])


# Fit Poisson curves to the degree data.
extractedLambdaValues = np.zeros_like(P_Array)
extractedPCOV_Values = np.zeros_like(P_Array)

for i in range(0, P_Array.shape[0]):
    extractedLambdaValues[i], extractedPCOV_Values[i] = curve_fit(
                                                                Distribution_Analysis_Functions.PoissonDistribution,
                                                                degreeDistributions[i][0, :],
                                                                degreeDistributions[i][1, :],
                                                                Network_Analysis_Functions.AverageDegree(adjacencyMatrices[i]))


# Plot the Poisson distribution graph.
plt.figure("Poisson Distribution Of Varying Probability (N = " + str(N) + ")")

for i in range(0, P_Array.shape[0]):
    plt.plot(degreeDistributions[i][0, :], degreeDistributions[i][1, :])

    newDegreeArray = np.linspace(0, N, 1000)
    plt.plot(
        newDegreeArray,
        N * Distribution_Analysis_Functions.PoissonDistribution(newDegreeArray, extractedLambdaValues[i]),
        label = "P = " + "{0:.2f}".format(P_Array[i])) #str(P_Array[i]))

plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Poisson Distribution Of Varying Probability (N = " + str(N) + ")")
plt.legend(loc = "best")
plt.show()


#--------------------------------------------------------------------------------------------------
# This section looks at how the poisson fitting diverges from the data as probability changes.
#--------------------------------------------------------------------------------------------------
#
# 
differencesArray = np.zeros_like(P_Array)

for i in range(0, P_Array.shape[0]):

    delta = degreeDistributions[i][1, :] - Distribution_Analysis_Functions.PoissonDistribution(degreeDistributions[i][0, :], extractedLambdaValues[i])
    differencesArray[i] = np.sqrt(np.sum(delta))


#
plt.figure("Differences Of Poisson Fit Against Varying Probability Data (N = " + str(N) + ")")
plt.plot(P_Array, differencesArray)

plt.xlabel("Probability")
plt.ylabel("Root Of Sum Of Differences")
plt.title("Differences Of Poisson Fit Against Varying Probability Data (N = " + str(N) + ")")
plt.show()


#--------------------------------------------------------------------------------------------------
# This section looks at how the standard deviations of the Poisson fit compares with the standard
# deviation of the original data.
#--------------------------------------------------------------------------------------------------
# 
# 
stdOfDegreeArray = np.zeros_like(P_Array)
rootMeanOfPoisson = np.zeros_like(P_Array)

for i in range(0, P_Array.shape[0]):
    stdOfDegreeArray[i] = np.std(degreeDistributions[i][1, :])
    rootMeanOfPoisson[i] = np.sqrt(extractedLambdaValues[i])

plt.figure("Comparison Of Root-Mean and STD of Poisson data")
plt.plot(P_Array, stdOfDegreeArray, label = "Standard Deviation Of Data")
plt.plot(P_Array, rootMeanOfPoisson, label = "Root-Mean Of Poisson")

plt.xlabel("Probability")
plt.ylabel("Error")
plt.title("Comparison Of Root-Mean and STD of Poisson data")
plt.legend(loc = "best")
plt.show()

