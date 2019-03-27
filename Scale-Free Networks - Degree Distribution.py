import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from NetworkTypes.ScaleFree_Network import ScaleFree_Network
from SupportingFunctions import Network_Analysis_Functions 
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


#------------------------------------------------------------------------------------------
# This section demonstrates the power-law tail of the degree distribution for a scale-free
# network of a given size.
#------------------------------------------------------------------------------------------

N = 250

adjacencyMatrix = nx.to_numpy_matrix((nx.barabasi_albert_graph(N, 1))) #ScaleFree_Network.GenerateAdjacencyMatrix(N)
degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

plt.figure("Scale-Free Networks - Degree Distribution")
plt.plot(degreeDistribution[0, :], degreeDistribution[1, :], label='Data')



array1, array2 = IO.CleanArraysOfZeroValues(degreeDistribution[0, :], degreeDistribution[1, :])
array1 = np.log(array1)
array2 = np.log(array2)

endPoint = Distribution_Analysis_Functions.FirstIndexContainingGivenValue(array2, 0)
debug = array2[:endPoint]
estimatedGammaValue = -3
estimatedIntercept = 3.3
popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        array1[:endPoint],
                        array2[:endPoint],
                        (estimatedGammaValue, estimatedIntercept))

newDegreeArray = np.linspace(0, N, 1000)


#plt.plot(newDegreeArray, N*Distribution_Analysis_Functions.ExponentialTail(newDegreeArray, popt[0]), label='Best Fit')

print(popt[0])
print(popt[1])
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.legend(loc='best')
plt.title('Degree Distribution Of Scale-Free Networks, N = ' + str(N))
plt.savefig("NetworkTypes/ScaleFree_Network/Scale-Free Networks - Degree Distribution.png")


plt.figure("Scale-Free Networks - LogLog Degree Distribution")
plt.plot(array1[:endPoint], array2[:endPoint], 'o', label='Data')
plt.plot(array1[endPoint:], array2[endPoint:], 'o', c='grey', label='Reject', )

newArray = np.linspace(array1[0], array1[-1], 1000)
plt.plot(newArray, Distribution_Analysis_Functions.StraightLine(newArray, popt[0], popt[1]), label='Best Fit')

plt.legend(loc='best')
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.legend(loc='best')
plt.title('Log-Log Degree Distribution Of Scale-Free Networks, N = ' + str(N))
plt.savefig("NetworkTypes/ScaleFree_Network/Scale-Free Networks - LogLog Degree Distribution.png")



#------------------------------------------------------------------------------------------
# This section fits an exponential to the power-tails of various scale-free networks.
#------------------------------------------------------------------------------------------

N_Array = np.arange(1000, 4050, 50)

gammaArray = np.zeros(len(N_Array))
gammaErrorsArray = np.zeros(len(N_Array))
interceptArray = np.zeros(len(N_Array))
interceptErrorsArray = np.zeros(len(N_Array))

for i in range(len(N_Array)):

    numberOfRepeats = 3

    sumGamma = 0
    sumGammaError = 0
    sumIntercept = 0
    sumInterceptError = 0

    for j in range(numberOfRepeats):

        adjacencyMatrix = nx.to_numpy_matrix(nx.barabasi_albert_graph(N_Array[i], 1))
        degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

        array1, array2 = IO.CleanArraysOfZeroValues(degreeDistribution[0, :], degreeDistribution[1, :])
        array1 = np.log(array1)
        array2 = np.log(array2)

        endPoint = Distribution_Analysis_Functions.FirstIndexContainingGivenValue(array2, 0)

        if(endPoint < 3):
            numberOfRepeats -= 1
            continue

        estimatedGammaValue = -3
        estimatedIntercept = 3.3
        popt, pcov = curve_fit(
                            Distribution_Analysis_Functions.StraightLine,
                            array1[:endPoint],
                            array2[:endPoint],
                            (estimatedGammaValue, estimatedIntercept))
        pvar = np.diag(pcov)

        sumGamma += popt[0]
        sumGammaError += np.sqrt(pvar[0])
        sumIntercept += popt[1]
        sumInterceptError += np.sqrt(pvar[1])

    gammaArray[i] = sumGamma / numberOfRepeats
    gammaErrorsArray[i] = sumGammaError / numberOfRepeats
    interceptArray[i] = sumIntercept / numberOfRepeats
    interceptErrorsArray[i] = sumInterceptError / numberOfRepeats

    print(str(N_Array[i]) + ' DONE')


fileDestination = 'NetworkTypes/ScaleFree_Network/Gamma Values For Scale-Free Networks (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', N_Array, 'Gamma', gammaArray)
#N_Array, gammaArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkTypes/ScaleFree_Network/Gamma Errors For Scale-Free Networks (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', N_Array, 'Gamma Errors', gammaErrorsArray)
#N_Array, gammaErrorsArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkTypes/ScaleFree_Network/Intercept Values For Scale-Free Networks (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', N_Array, 'Gamma', interceptArray)
#N_Array, interceptArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkTypes/ScaleFree_Network/Intercept Error Values For Scale-Free Networks (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', N_Array, 'Gamma', interceptErrorsArray)
#N_Array, interceptErrorsArray = IO.ReadPlottingDataFromTxtFile(fileDestination)


#
plt.figure()
#plt.plot(N_Array, gammaArray, 'o')
plt.errorbar(N_Array, gammaArray, yerr = gammaErrorsArray/2, fmt = 'o')

plt.grid()
plt.ylim(-3, -2)
plt.xlabel('Number Of Nodes')
plt.ylabel('Gamma Value')
plt.title('Gamma Exponent Constant Of Scale-Free Networks (Varying N)')
plt.savefig("NetworkTypes/ScaleFree_Network/Gamma Exponent Constant Of Scale-Free Networks (Varying N).png")

'''
#
plt.figure()
plt.plot(N_Array, gammaErrorsArray, 'o')

plt.grid()
plt.xlabel('Number Of Nodes')
plt.ylabel('Gamma Value Error')
plt.title('Gamma Exponent Error Of Scale-Free Networks (Varying N)')
plt.savefig("NetworkTypes/ScaleFree_Network/Gamma Exponent Error Of Scale-Free Networks (Varying N).png")
'''

#
plt.figure()
plt.grid()
plt.xlabel('Number Of Nodes')
plt.ylabel('Intercept Value')

plt.errorbar(N_Array, interceptArray, yerr = interceptErrorsArray/2, fmt = 'o')
plt.plot(N_Array, np.log(N_Array), label='lnN Curve')

plt.title('Intercept Of LogLog Degree Distribution For Scale-Free Networks (Varying N)')
plt.savefig("NetworkTypes/ScaleFree_Network/Intercept Of LogLog Degree Distribution For Scale-Free Networks (Varying N).png")



