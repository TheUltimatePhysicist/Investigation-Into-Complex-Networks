import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from NetworkTypes.Random_Network import Random_Network
from SupportingFunctions import Network_Analysis_Functions
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO

"""
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
"""

probability = 0.50
N_Array = np.arange(50, 500, 50)

clusteringCoefficientArray = np.zeros(N_Array.shape[0])
clusteringCoefficientArray[0] = 0.5016641334008043
clusteringCoefficientArray[1] = 0.5034136044311537
clusteringCoefficientArray[2] = 0.5015198304303254
clusteringCoefficientArray[3] = 0.5000306091831521
clusteringCoefficientArray[4] = 0.4982656062921174
clusteringCoefficientArray[5] = 0.49836488196273476
clusteringCoefficientArray[6] = 0.49893511787924977
clusteringCoefficientArray[7] = 0.5012285624948963
clusteringCoefficientArray[8] = 0.49998337580756125


# Fit a straight line to the data.
estimateGradient = clusteringCoefficientArray[len(clusteringCoefficientArray) - 1] / N_Array[len(N_Array) - 1]
estimateIntercept = 0.5
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.StraightLine,
                    N_Array, clusteringCoefficientArray,
                    (estimateGradient, estimateIntercept))


# Plot the resulting data.
plt.figure("Clustering Coefficients Of Random Networks (Probability = " + str(probability) + ")")
plt.plot(N_Array, clusteringCoefficientArray, 'o', label = 'Original Data')


xArray = np.linspace(N_Array[0], N_Array[len(N_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')


plt.ylim(0.45, 0.55)
plt.xlabel("Number Of Nodes")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Random Networks (Probability = " + str(probability) + ")")
plt.legend()
plt.grid()
plt.savefig("Clustering Coefficients Of Random Networks (Probability = " + str(probability) + ").png")


# Output the data to a .txt file.
outputFile = open("Random Networks - Clustering Coefficients - Varying N.txt", 'w')
#WritePlottingDataToTxtFile(outputFile, "N", N_Array, "Difference", clusteringCoefficientArray)

outputFile.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt[0]) + "\n Intercept = " + str(popt[1]))
outputFile.close()



#--------------------------------------------------------------------------------------------------
# This section looks at a fixed node number and varying probability, to determine how the
# clustering coefficient changes over a range of probabilities.
#--------------------------------------------------------------------------------------------------
#
# Initialise N and the probability array.
N = 100
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
    print ("P = " + "{0:.2f}".format(P_Array[i]) + ", Coefficient = " + str(clusteringValue))


# Fit a straight line to the data.
estimateGradient = clusteringCoefficientArray[len(clusteringCoefficientArray) - 1] / P_Array[len(P_Array) - 1]
estimateIntercept = 0
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.StraightLine,
                    P_Array, clusteringCoefficientArray,
                    (estimateGradient, estimateIntercept))


# Plot the resulting data.
plt.figure("Clustering Coefficients Of Random Networks (N = " + str(N) + ")")
plt.plot(P_Array, clusteringCoefficientArray, 'o', label = "Original Data")

xArray = np.linspace(P_Array[0], P_Array[len(P_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')


plt.xlabel("Probability")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Random Networks (N = " + str(N) + ")")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Clustering Coefficients Of Random Networks (N = " + str(N) + ").png")


# Output the data to a .txt file.
outputFile = open("Random Networks - Clustering Coefficients - Varying P.txt", 'w')
#WritePlottingDataToTxtFile(outputFile, "P", P_Array, "Difference", clusteringCoefficientArray)

outputFile.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt[0]) + "\n Intercept = " + str(popt[1]))
outputFile.close()


