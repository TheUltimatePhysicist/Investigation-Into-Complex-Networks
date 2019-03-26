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

N = 2000

adjacencyMatrix = ScaleFree_Network.GenerateAdjacencyMatrix(N)
degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

plt.figure("Scale-Free Networks - Degree Distribution")
plt.plot(degreeDistribution[0, :], degreeDistribution[1, :])

'''
estimatedGammaValue = -3

popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.ExponentialTail,
                        degreeDistribution[0, :],
                        degreeDistribution[1, :],
                        estimatedGammaValue)

array1 = np.log(degreeDistribution[0, 1:])
array2 = np.log(degreeDistribution[1, 1:])
for i in range(len(degreeDistribution)):
    if (np.isfinite(array1[i]) == False):    array1[i] = 0
    if (np.isfinite(array2[i]) == False):    array2[i] = 0
'''


array1, array2 = IO.CleanArraysOfZeroValues(degreeDistribution[0, :], degreeDistribution[1, :])
array1 = np.log(array1)
array2 = np.log(array2)
estimatedGammaValue = -3
estimatedIntercept = 3.3
popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        array1,
                        array2,
                        (estimatedGammaValue, estimatedIntercept))

newDegreeArray = np.linspace(0, N, 1000)


plt.plot(newDegreeArray, N*Distribution_Analysis_Functions.ExponentialTail(newDegreeArray, popt[0]))

print(popt[0])
print(popt[1])
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.title('Degree Distribution Of Scale-Free Networks, N = ' + str(N))
plt.savefig("NetworkTypes/ScaleFree_Network/Scale-Free Networks - Degree Distribution.png")


plt.figure("Scale-Free Networks - LogLog Degree Distribution")
plt.plot(array1, array2, 'o', label='Data')

newArray = np.linspace(array1[0], array1[-1], 1000)
plt.plot(newArray, Distribution_Analysis_Functions.StraightLine(newArray, popt[0], popt[1]), label='Line Of Best Fit')

plt.legend(loc='best')
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.title('Log-Log Degree Distribution Of Scale-Free Networks, N = ' + str(N))
plt.savefig("NetworkTypes/ScaleFree_Network/Scale-Free Networks - LogLog Degree Distribution.png")


#------------------------------------------------------------------------------------------
# This section fits an exponential to the power-tails of various scale-free networks.
#------------------------------------------------------------------------------------------

N_Array = np.arange(50, 2050, 50)

gammaArray = np.zeros(len(N_Array))
gammaErrorsArray = np.zeros(len(N_Array))
interceptArray = np.zeros(len(N_Array))
interceptErrorsArray = np.zeros(len(N_Array))

for i in range(len(N_Array)):

    numberOfRepeats = 10

    sumGamma = 0
    sumGammaError = 0
    sumIntercept = 0
    sumInterceptError = 0

    for j in range(numberOfRepeats):

        adjacencyMatrix = nx.to_numpy_matrix(nx.barabasi_albert_graph(N_Array[i], 5))
        degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

        array1, array2 = IO.CleanArraysOfZeroValues(degreeDistribution[0, :], degreeDistribution[1, :])
        array1 = np.log(array1)
        array2 = np.log(array2)
        estimatedGammaValue = -3
        estimatedIntercept = 3.3
        popt, pcov = curve_fit(
                            Distribution_Analysis_Functions.StraightLine,
                            array1,
                            array2,
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

fileDestination = 'NetworkTypes/ScaleFree_Network/Gamma Values For Scale-Free Networks (Varying N)'
IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', N_Array, 'Gamma', gammaArray)

fileDestination = 'NetworkTypes/ScaleFree_Network/Gamma Errors For Scale-Free Networks (Varying N)'
IO.WritePlottingDataToTxtFile(fileDestination, 'Number Of Nodes', N_Array, 'Gamma Errors', gammaArray)

#
plt.figure()
plt.plot(N_Array, gammaArray, 'o')

plt.grid()
plt.ylim(-2.5, -1.2)
plt.xlabel('Number Of Nodes')
plt.ylabel('Gamma Value')
plt.title('Gamma Exponent Constant Of Scale-Free Networks (Varying N)')
plt.savefig("NetworkTypes/ScaleFree_Network/Gamma Exponent Constant Of Scale-Free Networks (Varying N).png")

#
plt.figure()
plt.plot(N_Array, gammaErrorsArray, 'o')

plt.grid()
plt.xlabel('Number Of Nodes')
plt.ylabel('Gamma Value Error')
plt.title('Gamma Exponent Error Of Scale-Free Networks (Varying N)')
plt.savefig("NetworkTypes/ScaleFree_Network/Gamma Exponent Error Of Scale-Free Networks (Varying N).png")

