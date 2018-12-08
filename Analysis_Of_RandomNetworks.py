import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy

import Random_Network
import Network_Analysis


# Define the number of nodes and probability.
numberOfNodes = 30
probability = 0.15

# Define the adjacency matrix.
adjacencyMatrix_RandomNetwork = Random_Network.GenerateAdjacencyMatrix(numberOfNodes, probability)
# Create a networkx graph.
G_RandomNetwork = nx.from_numpy_matrix(adjacencyMatrix_RandomNetwork)

# PLot the random networkx graph.
plt.figure("Random Network")
nx.draw(G_RandomNetwork, with_labels = True, font_weight = 'bold')
plt.show()


# Determine whether the random networks follow a Poisson distribution.
#
# Note: For random complex networks, the degree distribution is a Poisson
# distribution. Therefore we need to plot number of nodes vs the degree.

degreeArray = np.zeros((2, adjacencyMatrix_RandomNetwork.shape[0]))
     
for i in range(0, adjacencyMatrix_RandomNetwork.shape[0]):

    degreeArray[0, i] = i
    degreeOfNode = Network_Analysis.DegreeOfNode(adjacencyMatrix_RandomNetwork, i)
    degreeArray[1, degreeOfNode] += 1


# Fit a Poisson curve to the data set.
#
# http://www-f1.ijs.si/~rudi/sola/Random_Networks.pdf
# https://en.wikipedia.org/wiki/Poisson_distribution

def PoissonDistribution(degreeArray, lambdaMeanValue):
    """
    array = np.zeros(degreeArray.shape[0])

    for i in range(0, degreeArray.shape[0]):
        numerator = np.exp(-lambdaMeanValue) * (lambdaMeanValue**degreeArray[i])
        denominator = m.factorial(np.int(degreeArray[i]))

        array[i] = numerator / denominator

    return array
    """
    return np.exp((degreeArray * np.log(lambdaMeanValue)) - lambdaMeanValue - scipy.special.gammaln(degreeArray + 1))

averageValue = Network_Analysis.AverageDegree(adjacencyMatrix_RandomNetwork)
popt, pcov = curve_fit(PoissonDistribution, degreeArray[0, :], degreeArray[1, :], averageValue)


# Plot the degree distribution and Poisson fit.

plt.figure("Random Network Degree Distribution")
plt.plot(degreeArray[0, :], degreeArray[1, :])

newDegreeArray = np.linspace(0, numberOfNodes, 1000)
poissonArray = PoissonDistribution(newDegreeArray, popt[0]) * numberOfNodes
plt.plot(newDegreeArray, poissonArray)

print ("---------------------")
print (np.sum(poissonArray))
print (popt[0])
print ("std of poisson fit = ", np.std(degreeArray[1,:]))
print ("root mean of fit = ", np.sqrt(popt[0]))

plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Degree Distribution of Random Network N = " + str(numberOfNodes) + ", p = " + str(probability))
plt.show()

