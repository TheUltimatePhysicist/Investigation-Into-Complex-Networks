import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from SupportingFunctions import Network_Analysis_Functions 
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


#------------------------------------------------------------------------------------------
# Important Arrays.
#------------------------------------------------------------------------------------------

datasetDesignation = np.array(["socfb-Caltech36",
                               "socfb-Reed98",
                               "socfb-Haverford76",
                               "socfb-Simmons81",
                               "socfb-Swarthmore42",
                               "socfb-Amherst41",
                               "socfb-Bowdoin47",
                               "socfb-Hamilton46",
                               "socfb-Trinity100",
                               "socfb-USFCA72",
                               "socfb-Williams40",
                               "socfb-Oberlin44",
                               "socfb-Smith60",
                               "socfb-Wellesley22",
                               "socfb-Vassar85",
                               "socfb-Middlebury45",
                               "socfb-Pepperdine86",
                               "socfb-Colgate88",
                               "socfb-Santa74",
                               "socfb-Wesleyan43",
                               "socfb-Mich67",
                               "socfb-Bucknell39",
                               "socfb-Brandeis99",
                               "socfb-Howard90",
                               "socfb-Rice31"])

numberOfDatasets = len(datasetDesignation)

numberOfNodesArray = np.array([769,
                               962,
                               1446,
                               1518,
                               1659,
                               2235,
                               2252,
                               2314,
                               2613,
                               2682,
                               2790,
                               2920,
                               2970,
                               2970,
                               3068,
                               3075,
                               3445,
                               3482,
                               3578,
                               3593,
                               3748,
                               3826,
                               3898,
                               4047,
                               4047])


#
meanShortestPathLengths = [None] * numberOfDatasets

for i in range(numberOfDatasets):
    dataset_G = nx.read_edgelist('NetworkRepository_Data/' + datasetDesignation[1] + '/' + datasetDesignation[1] + '.txt')
    meanShortestPathLengths[i] = nx.average_shortest_path_length(dataset_G)

fileDestination = 'NetworkRepository_Data/' + 'AverageShortestPathLength.txt'
IO.WritePlottingDataToTxtFile(fileDestination, "Number Of Nodes", numberOfNodesArray, "Average Shortest Path Length", meanShortestPathLengths)
'''

#
fileDestination = 'NetworkRepository_Data/' + 'AverageShortestPathLength.txt'
numberArray, meanShortestPathLengths = IO.ReadPlottingDataFromTxtFile(fileDestination)
'''
plt.figure()
plt.grid()
plt.plot(numberOfNodesArray, meanShortestPathLengths, label='Data')

'''
# Fit a curve to the data.
estimateGradient = 0
estimateIntercept = 0.3

numberArray_temp, clusteringArray_temp = IO.CleanRepeatedValuesOfNetworkRepData(numberOfNodesArray, averageClusteringCoefficients)
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.StraightLine,
                    numberArray_temp, clusteringArray_temp,
                    (estimateGradient, estimateIntercept))
xArray = np.linspace(numberOfNodesArray[0],     numberOfNodesArray[len(numberOfNodesArray) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')
'''

#plt.ylim(0, 1)
plt.legend(loc='best')
plt.xlabel("Number Of Nodes")
plt.ylabel("Average Shortest Path Length")
plt.title("Average Shortest Path Length Of Social Media Networks (Varying N)")
plt.savefig("NetworkRepository_Data/Average Shortest Path Length Of Social Media Networks (Varying N)")
plt.close()

'''
print('')
print('----------------------------------------------')

pvar = np.diag(pcov)

print('Gradient = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
print('Intercept = ' + str(popt[1]) + ' +/- ' + str(np.sqrt(pvar[1])))
print('----------------------------------------------')
print('')
'''


