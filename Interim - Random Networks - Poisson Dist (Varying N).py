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
# degree distribution changes over a range of N. Note this is expected to follow the Poisson
# distribution.
#--------------------------------------------------------------------------------------------------
#
# Initialise the probability and N array.
probability = 0.050
N_Array = np.arange(50, 1050, 50)


# Create the adjacency matrices for varying N.
adjacencyMatrices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, N_Array.shape[0]):
    adjacencyMatrices[i] = Random_Network.GenerateAdjacencyMatrix(N_Array[i], probability)


# Extract the degree distribution data.
degreeDistributions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, N_Array.shape[0]):
    degreeDistributions[i] = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrices[i])


# Fit Poisson curves to the degree data.
extractedLambdaValues = np.zeros_like(N_Array)
extractedPCOV_Values = np.zeros_like(N_Array)

for i in range(0, N_Array.shape[0]):
    extractedLambdaValues[i], extractedPCOV_Values[i] = curve_fit(
                                                                Distribution_Analysis_Functions.PoissonDistribution,
                                                                degreeDistributions[i][0, :],
                                                                degreeDistributions[i][1, :],
                                                                Network_Analysis_Functions.AverageDegree(adjacencyMatrices[i]))


# Plot the Poisson distribution graph.
plt.figure("Poisson Distribution Of Varying N (P = " + str(probability) + ")")

for i in range(0, N_Array.shape[0]):
    plt.plot(degreeDistributions[i][0, :], degreeDistributions[i][1, :])

    newDegreeArray = np.linspace(0, N_Array[i], 1000)
    plt.plot(
        newDegreeArray,
        N_Array[i] * Distribution_Analysis_Functions.PoissonDistribution(newDegreeArray, extractedLambdaValues[i]),
        label = "N = " + str(N_Array[i]))

plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Various Poisson Distributions for Different N nodes (P = " + str(probability) + ")")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Various Poisson Distributions for Different N nodes (P = " + str(probability) + ").png")
plt.show()


# Output the extracted mean values of the Poisson fitting.
outputFile = open("Poisson Distribution - Extracted Mean Values - Varying N.txt", 'w')
WritePlottingDataToTxtFile(outputFile, "N", N_Array, "Poisson Mean Value", extractedLambdaValues)
outputFile.close()


#--------------------------------------------------------------------------------------------------
# This section looks at how the Poisson fitting diverges from the data as N changes.
#--------------------------------------------------------------------------------------------------
#
# 
differencesArray = np.zeros_like(N_Array)

for i in range(0, N_Array.shape[0]):

    delta = degreeDistributions[i][1, :] - Distribution_Analysis_Functions.PoissonDistribution(degreeDistributions[i][0, :], extractedLambdaValues[i])
    differencesArray[i] = np.sqrt(np.sum(delta))


# Fit a straight line to the data.
estimateGradient = differencesArray[len(differencesArray) - 1] / N_Array[len(N_Array) - 1]
estimateIntercept = 0
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.StraightLine,
                    N_Array, differencesArray,
                    (estimateGradient, estimateIntercept))


# Plot the data.
plt.figure("Differences Of Poisson Fit Against Varying N Data (P = " + str(probability) + ")")
plt.plot(N_Array, differencesArray, label = 'Original Data')

xArray = np.linspace(N_Array[0], N_Array[len(N_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')

plt.xlabel("Number Of Nodes")
plt.ylabel("Root Of Sum Of Differences")
plt.title("Differences Of Poisson Fit Against Varying N Data (P = " + str(probability) + ")")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Differences Of Poisson Fit Against Varying N Data (P = " + str(probability) + ").png")


# Output data to text file.
outputFile = open("Poisson Distribution - Divergance - Varying N.txt", 'w')
WritePlottingDataToTxtFile(outputFile, "N", N_Array, "Difference", differencesArray)

outputFile.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt[0]) + "\n Intercept = " + str(popt[1]))
outputFile.close()


#--------------------------------------------------------------------------------------------------
# This section looks at how the standard deviations of the Poisson fit compares with the standard
# deviation of the original data.
#--------------------------------------------------------------------------------------------------
# 
# 
stdOfDegreeArray = np.zeros_like(N_Array)
rootMeanOfPoisson = np.zeros_like(N_Array)

for i in range(0, N_Array.shape[0]):
    stdOfDegreeArray[i] = np.std(degreeDistributions[i][1, :])
    rootMeanOfPoisson[i] = np.sqrt(extractedLambdaValues[i])


# Fit a straight line to the standard deviation data.
estimateGradient = stdOfDegreeArray[len(stdOfDegreeArray) - 1] / N_Array[len(N_Array) - 1]
estimateIntercept = 0
popt_std, pcov_std = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        N_Array, stdOfDegreeArray,
                        (estimateGradient, estimateIntercept))


# Fit a straight line to the root mean data.
estimateGradient = rootMeanOfPoisson[len(rootMeanOfPoisson) - 1] / N_Array[len(N_Array) - 1]
estimateIntercept = 0
popt_rootmean, pcov_rootmean = curve_fit(
                                        Distribution_Analysis_Functions.StraightLine,
                                        N_Array, rootMeanOfPoisson,
                                        (estimateGradient, estimateIntercept))


# Plot the data.
plt.figure("Comparison Of Root-Mean and STD of Poisson data - Varying N")
plt.plot(N_Array, stdOfDegreeArray, label = "Standard Deviation Of Data")
plt.plot(N_Array, rootMeanOfPoisson, label = "Root-Mean Of Poisson")

xArray = np.linspace(N_Array[0], N_Array[len(N_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt_std[0], popt_std[1]), label = 'STD Best Fit')
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt_rootmean[0], popt_rootmean[1]), label = 'Root-Mean Best Fit')

plt.xlabel("Number Of Nodes")
plt.ylabel("Error")
plt.title("Comparison Of Root-Mean and STD of Poisson data - Varying N")
plt.legend(loc = "best")
plt.grid()
plt.savefig("Comparison Of Root-Mean and STD of Poisson data - Varying N.png")


# Output data to text file.
outputFile_std = open("Poisson Distribution - STD Of Data - Varying N.txt", 'w')
outputFile_rtMean = open("Poisson Distribution - Root Mean Of Fits - Varying N.txt", 'w')

WritePlottingDataToTxtFile(outputFile_std, "N", N_Array, "STD", stdOfDegreeArray)
WritePlottingDataToTxtFile(outputFile_rtMean, "N", N_Array, "Root-Mean", rootMeanOfPoisson)

outputFile_std.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt_std[0]) + "\n Intercept = " + str(popt_std[1]))
outputFile_rtMean.write("\n" + "Best fit line:" + "\n Gradient = " + str(popt_rootmean[0]) + "\n Intercept = " + str(popt_rootmean[1]))

outputFile_std.close()
outputFile_rtMean.close()
