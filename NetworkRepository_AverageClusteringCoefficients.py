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
'''
averageClusteringCoefficients = [None] * numberOfDatasets

for i in range(numberOfDatasets):
    dataset_G = nx.read_edgelist('NetworkRepository_Data/' + datasetDesignation[i] + '/' + datasetDesignation[i] + '.txt')
    averageClusteringCoefficients[i] = nx.average_clustering(dataset_G)

fileDestination = 'NetworkRepository_Data/' + 'AverageClusteringCoefficients.txt'
IO.WritePlottingDataToTxtFile(fileDestination, "Number Of Nodes", numberOfNodesArray, "Average Clustering Coefficient", averageClusteringCoefficients)
'''

#
fileDestination = 'NetworkRepository_Data/' + 'AverageClusteringCoefficients.txt'
numberArray, averageClusteringCoefficients = IO.ReadPlottingDataFromTxtFile(fileDestination)

plt.figure()
plt.grid()
plt.plot(numberOfNodesArray, averageClusteringCoefficients)

plt.ylim(0, 1)
plt.xlabel("Number Of Nodes")
plt.ylabel("Average Clustering Coefficient")
plt.title("Average Clustering Coefficients Of Social Media Networks (Varying N)")
plt.savefig("NetworkRepository_Data/Average Clustering Coefficients Of Social Media Networks (Varying N)")
plt.close()


