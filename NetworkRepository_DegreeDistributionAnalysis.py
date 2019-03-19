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

numberOfDatasets = len(datasetDesignation) + 1

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

for i in range(0, numberOfDatasets - 1):
    fileDestination = 'NetworkRepository_Data/' + datasetDesignation[i] + '/' + datasetDesignation[i] + '_DegreeDistribution.txt'
    degreeArray, numberArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

    # 
    '''
    estimatedGammaValue = -1
    popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.ExponentialTail,
                        degreeArray,
                        numberArray,
                        estimatedGammaValue)
    '''
    estimatedGammaValue = -3
    estimatedIntercept = 0
    popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        np.log(degreeArray),
                        np.log(numberArray),
                        estimatedGammaValue,
                        estimatedIntercept)

    secondDegreeArray = np.linspace(0, numberOfNodesArray[i], numberOfNodesArray[i]*2)

    # Create a raw plot of the degree distribution.
    plt.figure()
    plt.grid()
    plt.plot(degreeArray, numberArray)
    plt.plot(secondDegreeArray, Distribution_Analysis_Functions.ExponentialTail(secondDegreeArray, popt[0]))

    plt.xlabel("Degree")
    plt.ylabel("Number Of Nodes")
    plt.title("Degree Distribution Of " + datasetDesignation[i] +  " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.savefig("NetworkRepository_Data/" + datasetDesignation[i] + "/Degree Distribution Of " + datasetDesignation[i] + " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.close()


    # 
    plt.figure()
    plt.grid()
    plt.loglog(degreeArray, numberArray, 'o')
    plt.plot(secondDegreeArray, Distribution_Analysis_Functions.StraightLine(secondDegreeArray, popt[0], popt[1]))

    plt.xlabel("Degree")
    plt.ylabel("Number Of Nodes")
    plt.title("Log-Log Degree Distribution Of " + datasetDesignation[i] +  " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.savefig("NetworkRepository_Data/" + datasetDesignation[i] + "/Log-Log Degree Distribution Of " + datasetDesignation[i] + " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.close()

