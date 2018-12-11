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
# This section looks at a fixed probability value and varying node number, to determine how the
# clustering coefficient changes over a range of N.
#--------------------------------------------------------------------------------------------------
#
# Initialise the probability and N array.
probability = 0.50
N_Array = np.arange(50, 1050, 50)


# Create the adjacency matrices for varying N.
adjacencyMatrices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, N_Array.shape[0]):
    adjacencyMatrices[i] = Random_Network.GenerateAdjacencyMatrix(N_Array[i], probability)


# Compute the clustering coefficient values.
clusteringCoefficientArray = np.zeros(N_Array.shape[0])

for i in range(0, N_Array.shape[0]):
    clusteringValue = Network_Analysis_Functions.AverageClusteringCoefficient(adjacencyMatrices[i])
    clusteringCoefficientArray[i] = clusteringValue
    print ("N = " + str(N_Array[i]) + ", Coefficient = " + str(clusteringValue))


# Plot the resulting data.
plt.figure("Clustering Coefficients Of Random Networks (Probability = " + str(probability) + ")")
plt.plot(N_Array, clusteringCoefficientArray)

plt.xlabel("Number Of Nodes")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Random Networks (Probability = " + str(probability) + ")")
plt.grid()
plt.savefig("Clustering Coefficients Of Random Networks (Probability = " + str(probability) + ").png")


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed node number and varying probability, to determine how the
# clustering coefficient changes over a range of probabilities.
#--------------------------------------------------------------------------------------------------
#
# Initialise N and the probability array.
N = 250
P_Array = np.arange(0.05, 1.05, 0.05)


# Create the adjacency matrices for varying N.
adjacencyMatrices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, P_Array.shape[0]):
    adjacencyMatrices[i] = Random_Network.GenerateAdjacencyMatrix(N, P_Array[i])


# Compute the clustering coefficient values.
clusteringCoefficientArray = np.zeros(P_Array.shape[0])

for i in range(0, P_Array.shape[0]):
    clusteringValue = Network_Analysis_Functions.AverageClusteringCoefficient(adjacencyMatrices[i])
    clusteringCoefficientArray[i] = clusteringValue
    print ("P = " + str(P_Array[i]) + ", Coefficient = " + str(clusteringValue))


# Plot the resulting data.
plt.figure("Clustering Coefficients Of Random Networks (N = " + str(N) + ")")
plt.plot(P_Array, clusteringCoefficientArray)

plt.xlabel("Probability")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Random Networks (N = " + str(N) + ")")
plt.grid()
plt.savefig("Clustering Coefficients Of Random Networks (N = " + str(N) + ").png")

