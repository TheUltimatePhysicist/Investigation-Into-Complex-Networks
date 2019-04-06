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



gammaArray = np.zeros(numberOfDatasets)
gammaErrorsArray = np.zeros(numberOfDatasets)
interceptArray = np.zeros(numberOfDatasets)
interceptErrorsArray = np.zeros(numberOfDatasets)

# 
for i in range(0, 1):#numberOfDatasets):
    print ('started ' + str(i) + ' out of 24')

    fileDestination = 'NetworkRepository_Data/' + datasetDesignation[i] + '/' + datasetDesignation[i] + '_DegreeDistribution.txt'
    degreeArray, numberArray = IO.ReadPlottingDataFromTxtFile(fileDestination)


    array1_tt, array2_tt = IO.CleanArraysOfZeroValues(degreeArray, numberArray)
    array1 = np.log(array1_tt)
    array2 = np.log(array2_tt)

    endPoint = len(array1) - 1 #Distribution_Analysis_Functions.FirstIndexContainingGivenValue(array2, 0)
    '''
    # 
    estimatedVal_1 = 5
    estimatedVal_2 = 0.5
    popt, pcov = curve_fit(
                            Distribution_Analysis_Functions.DiracDeltaFunction,
                            degreeArray,
                            numberArray,
                            (estimatedVal_1, estimatedVal_2))
    
    #
    pvar = np.diag(pcov)

    gammaArray[i] = popt[0]
    gammaErrorsArray[i] = np.sqrt(pvar[0])
    interceptArray[i] = popt[1]
    interceptErrorsArray[i] = np.sqrt(pvar[1])
    '''

    # Create a raw plot of the degree distribution.
    plt.figure()
    plt.grid()
    plt.plot(degreeArray, numberArray)

    #newArray = np.linspace(0, numberOfNodesArray[i], 1000)
    #plt.plot(newArray, numberOfNodesArray[i] * Distribution_Analysis_Functions.DiracDeltaFunction(newArray, popt[0], popt[1]))

    plt.xlabel("Degree")
    plt.ylabel("Number Of Nodes")
    plt.title("Degree Distribution Of " + datasetDesignation[i] +  " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.savefig("NetworkRepository_Data/" + datasetDesignation[i] + "/Degree Distribution Of " + datasetDesignation[i] + " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.close()

    # 
    plt.figure()
    plt.grid()
    plt.ylim(0, 5)
    plt.xlim(0, 6)
    plt.plot(array1, array2, 'o')

    #plt.plot(array1, (-2)*array1 + np.log(array2_tt))

    #arrayfit1, arrayfit2 = IO.CleanArraysOfZeroValues(newArray, numberOfNodesArray[i] * Distribution_Analysis_Functions.DiracDeltaFunction(newArray, popt[0], popt[1]))
    #arrayfit1 = np.log(arrayfit1)
    #arrayfit2 = np.log(arrayfit2)
    #plt.plot(arrayfit1, arrayfit2)
    #secondDegreeArray = np.linspace(array1[0], array1[-1], 1000)
    #plt.plot(secondDegreeArray, np.log(Distribution_Analysis_Functions.DiracDeltaFunction(secondDegreeArray, popt[0], popt[1])))


    plt.xlabel("Degree")
    plt.ylabel("Number Of Nodes")
    plt.title("Log-Log Degree Distribution Of " + datasetDesignation[i] +  " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.savefig("NetworkRepository_Data/" + datasetDesignation[i] + "/Log-Log Degree Distribution Of " + datasetDesignation[i] + " (N = " + str(numberOfNodesArray[i]) + ")")
    plt.close()


#
fileDestination = 'NetworkRepository_Data/Gamma Values For Scale-Free Model (Varying N).txt'
#IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', numberOfNodesArray, 'Gamma', gammaArray)
#N_Array, gammaArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkRepository_Data/Gamma Error Values For Scale-Free Model (Varying N).txt'
#IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', numberOfNodesArray, 'Gamma Errors', gammaErrorsArray)
#N_Array, gammaErrorsArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkRepository_Data/Intercept Values For Scale-Free Model (Varying N).txt'
#IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', numberOfNodesArray, 'Gamma', interceptArray)
#N_Array, interceptArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkRepository_Data/Intercept Error Values For Scale-Free Model (Varying N).txt'
#IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', numberOfNodesArray, 'Gamma', interceptErrorsArray)
#N_Array, interceptErrorsArray = IO.ReadPlottingDataFromTxtFile(fileDestination)


