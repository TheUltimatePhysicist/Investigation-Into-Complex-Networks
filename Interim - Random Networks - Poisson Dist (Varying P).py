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
# This section looks at a fixed number of nodes and a changing probability, to determine how the
# degree distribution changes with probability.
#--------------------------------------------------------------------------------------------------
#
# Initialise the N and probability array.
N = 250
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
        label = "P = " + "{0:.2f}".format(P_Array[i]))

plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Poisson Distribution Of Varying Probability (N = " + str(N) + ")")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Poisson Distribution Of Varying Probability (N = " + str(N) + ").png")
plt.show()


# Output the extracted mean values of the Poisson fitting.
outputFile = open("Poisson Distribution - Extracted Mean Values - Varying P.txt", 'w')
WritePlottingDataToTxtFile(outputFile, "P", P_Array, "Poisson Mean Value", extractedLambdaValues)
outputFile.close()


#--------------------------------------------------------------------------------------------------
# This section looks at how the poisson fitting diverges from the data as probability changes.
#--------------------------------------------------------------------------------------------------
#
# 
differencesArray = np.zeros_like(P_Array)

for i in range(0, P_Array.shape[0]):

    delta = degreeDistributions[i][1, :] - Distribution_Analysis_Functions.PoissonDistribution(degreeDistributions[i][0, :], extractedLambdaValues[i])
    differencesArray[i] = np.sqrt(np.sum(delta))


# Fit a straight line to the data.
estimateGradient = differencesArray[len(differencesArray) - 1] / P_Array[len(P_Array) - 1]
estimateIntercept = 0
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.StraightLine,
                    P_Array, differencesArray,
                    (estimateGradient, estimateIntercept))


# Plot the data.
plt.figure("Differences Of Poisson Fit Against Varying Probability Data (N = " + str(N) + ")")
plt.plot(P_Array, differencesArray, label = 'Original Data')
"""
xArray = np.linspace(P_Array[0], P_Array[len(P_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')
"""
plt.xlabel("Probability")
plt.ylabel("Root Of Sum Of Differences")
plt.title("Differences Of Poisson Fit Against Varying Probability Data (N = " + str(N) + ")")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Differences Of Poisson Fit Against Varying Probability Data (N = " + str(N) + ").png")


# Output data to text file.
outputFile = open("Poisson Distribution - Divergance - Varying P.txt", 'w')
WritePlottingDataToTxtFile(outputFile, "N", P_Array, "Difference", differencesArray)

outputFile.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt[0]) + "\n Intercept = " + str(popt[1]))
outputFile.close()


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


# Fit a straight line to the standard deviation data.
estimateGradient = stdOfDegreeArray[len(stdOfDegreeArray) - 1] / P_Array[len(P_Array) - 1]
estimateIntercept = 0
popt_std, pcov_std = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        P_Array, stdOfDegreeArray,
                        (estimateGradient, estimateIntercept))


# Fit a straight line to the root mean data.
estimateGradient = rootMeanOfPoisson[len(rootMeanOfPoisson) - 1] / P_Array[len(P_Array) - 1]
estimateIntercept = 0
popt_rootmean, pcov_rootmean = curve_fit(
                                        Distribution_Analysis_Functions.StraightLine,
                                        P_Array, rootMeanOfPoisson,
                                        (estimateGradient, estimateIntercept))


# Plot the data.
plt.figure("Comparison Of Root-Mean and STD of Poisson data - Varying P")
plt.plot(P_Array, stdOfDegreeArray, label = "Standard Deviation Of Data")
plt.plot(P_Array, rootMeanOfPoisson, label = "Root-Mean Of Poisson")


xArray = np.linspace(P_Array[0], P_Array[len(P_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt_std[0], popt_std[1]), label = 'STD Best Fit')
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt_rootmean[0], popt_rootmean[1]), label = 'Root-Mean Best Fit')

plt.xlabel("Probability")
plt.ylabel("Error")
plt.title("Comparison Of Root-Mean and STD of Poisson data - Varying P")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Comparison Of Root-Mean and STD of Poisson data - Varying P.png")


# Output data to text file.
outputFile_std = open("Poisson Distribution - STD Of Data - Varying P.txt", 'w')
outputFile_rtMean = open("Poisson Distribution - Root Mean Of Fits - Varying P.txt", 'w')

WritePlottingDataToTxtFile(outputFile_std, "N", P_Array, "STD", stdOfDegreeArray)
WritePlottingDataToTxtFile(outputFile_rtMean, "N", P_Array, "Root-Mean", rootMeanOfPoisson)

outputFile_std.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt_std[0]) + "\n Intercept = " + str(popt_std[1]))
outputFile_rtMean.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt_rootmean[0]) + "\n Intercept = " + str(popt_rootmean[1]))

outputFile_std.close()
outputFile_rtMean.close()

