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
# This section concerns a single graph of a chosen N and p, note that the Poisson distribution
# function is defined within this section.
#--------------------------------------------------------------------------------------------------
#
# Define the number of nodes and probability.
numberOfNodes = 200
probability = 0.9

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

degreeArray = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix_RandomNetwork)

# Fit a Poisson curve to the data set.
#
# http://www-f1.ijs.si/~rudi/sola/Random_Networks.pdf
# https://en.wikipedia.org/wiki/Poisson_distribution

averageValue = Network_Analysis_Functions.AverageDegree(adjacencyMatrix_RandomNetwork)
popt, pcov = curve_fit(Distribution_Analysis_Functions.PoissonDistribution, degreeArray[0, :], degreeArray[1, :], averageValue)


# Plot the degree distribution and Poisson fit.

plt.figure("Random Network Degree Distribution")
plt.plot(degreeArray[0, :], degreeArray[1, :])

newDegreeArray = np.linspace(0, numberOfNodes, 1000)
poissonArray = Distribution_Analysis_Functions.PoissonDistribution(newDegreeArray, popt[0]) * numberOfNodes
plt.plot(newDegreeArray, poissonArray)

print ("---------------------")
print (np.sum(poissonArray))
print (popt[0])
print ("std of degree distribution = ", np.std(degreeArray[1,:]))
print ("root mean of fit = ", np.sqrt(popt[0]))

plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Degree Distribution of Random Network N = " + str(numberOfNodes) + ", p = " + str(probability))
plt.show()

