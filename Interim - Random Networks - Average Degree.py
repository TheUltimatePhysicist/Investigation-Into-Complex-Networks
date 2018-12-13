import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import Random_Network
import Network_Analysis_Functions
import Distribution_Analysis_Functions
from Input_Output_Support_Functions import *


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed probability value and varying node number, to determine how the
# average degree changes over a range of N.
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
averageDegreeArray = np.zeros(N_Array.shape[0])

for i in range(0, N_Array.shape[0]):
    degreeValue = Network_Analysis_Functions.AverageDegree(adjacencyMatrices[i])
    averageDegreeArray[i] = degreeValue


# Fit a straight line to the data.
estimateGradient = N_Array[len(N_Array) - 1] * probability
estimateIntercept = 0
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.StraightLine,
                    N_Array, averageDegreeArray,
                    (estimateGradient, estimateIntercept))


# Plot the resulting data.
plt.figure("Average Degree Of Random Networks (Probability = " + str(probability) + ")")
plt.plot(N_Array, averageDegreeArray, label = 'Original Data')

xArray = np.linspace(N_Array[0], N_Array[len(N_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')

plt.xlabel("Number Of Nodes")
plt.ylabel("Average Degree")
plt.title("Average Degree Of Random Networks (Probability = " + str(probability) + ")")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Average Degree Of Random Networks (Probability = " + str(probability) + ").png")


# Output data to text file.
outputFile = open("Random Networks - Average Degree - Varying N.txt", 'w')
WritePlottingDataToTxtFile(outputFile, "N", N_Array, "Avg. Degree", averageDegreeArray)

outputFile.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt[0]) + "\n Intercept = " + str(popt[1]))
outputFile.close()


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed node number and varying probability, to determine how the average
# degree changes over a range of probabilities.
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
averageDegreeArray = np.zeros_like(P_Array)

for i in range(0, P_Array.shape[0]):
    degreeValue = Network_Analysis_Functions.AverageDegree(adjacencyMatrices[i])
    averageDegreeArray[i] = degreeValue


# Fit a straight line to the data.
estimateGradient = averageDegreeArray[len(averageDegreeArray) - 1] / P_Array[len(P_Array) - 1]
estimateIntercept = 0
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.StraightLine,
                    P_Array, averageDegreeArray,
                    (estimateGradient, estimateIntercept))


# Plot the resulting data.
plt.figure("Average Degree Of Random Networks (N = " + str(N) + ")")
plt.plot(P_Array, averageDegreeArray, label = 'Original Data')

xArray = np.linspace(P_Array[0], P_Array[len(P_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')

plt.xlabel("Probability")
plt.ylabel("Average Degree")
plt.title("Average Degree Of Random Networks (N = " + str(N) + ")")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Average Degree Of Random Networks (N = " + str(N) + ")")


# Output data to text file.
outputFile = open("Random Networks - Average Degree - Varying P.txt", 'w')
WritePlottingDataToTxtFile(outputFile, "P", P_Array, "Avg. Degree", averageDegreeArray)

outputFile.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt[0]) + "\n Intercept = " + str(popt[1]))
outputFile.close()


