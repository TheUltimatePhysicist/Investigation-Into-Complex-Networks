import scipy
import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from NetworkTypes.SmallWorld_Network import SmallWorld_Network
from SupportingFunctions import Network_Analysis_Functions 
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


def Gaussian(xArray, height, centre, sigma):
    return height * np.exp(((xArray - centre)**2)/(-2*(sigma**2)))


#------------------------------------------------------------------------------------------
# This section demonstrates the degree distribution for a small-world network of a given
# size.
#------------------------------------------------------------------------------------------
'''
N = 2500
averageDegree = 10
probability = 0.5

adjacencyMatrix =  nx.to_numpy_matrix(  nx.watts_strogatz_graph(N, averageDegree, probability)  )
degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (N = ' + str(N) + ', P0 = ' + str(averageDegree) + ', p = ' + str(probability) + ').txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'Degree', degreeDistribution[0,:], 'Number Of Nodes', degreeDistribution[1,:])

plt.figure("Small-World Networks - Degree Distribution")
plt.plot(degreeDistribution[0, :], degreeDistribution[1, :], 'o', label='Data')


popt, pcov = curve_fit(
                        Gaussian,
                        degreeDistribution[0, :],
                        degreeDistribution[1, :],
                        (N, averageDegree, averageDegree))

print('')
print('----------------------------------------------')

pvar = np.diag(pcov)

print('Height = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
print('Centre = ' + str(popt[1]) + ' +/- ' + str(np.sqrt(pvar[1])))
print('STD = ' + str(popt[2]) + ' +/- ' + str(np.sqrt(pvar[2])))
print('----------------------------------------------')
print('')


jArray = np.linspace(degreeDistribution[0,0], degreeDistribution[0, -1], 1000)
plt.plot(jArray, Gaussian(jArray, popt[0], popt[1], popt[2]), label='Curve Of Best Fit')


plt.xlim(0, 200)
plt.grid()
plt.legend(loc='best')
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.title('Degree Distribution Of Small-World Networks, N = ' + str(N))
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution.png")

plt.figure()

array1_1, array2_1 = IO.CleanArraysOfZeroValues(degreeDistribution[0, :], degreeDistribution[1, :])
array1 = np.log(array1_1)
array2 = np.log(array2_1)

kArray = np.linspace(array1_1[0], array1_1[-1], 1000)
arrayC, arrayD = IO.CleanArraysOfZeroValues(kArray, Gaussian(kArray, popt[0], popt[1], popt[2]))
arrayC = np.log(arrayC)
arrayD = np.log(arrayD)

plt.plot(array1, array2, 'o', label='Data')
plt.plot(arrayC, arrayD, label='Curve Of Best Fit')

plt.legend(loc='best')
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.title('Log-Log Degree Distribution Of Small-World Networks, N = ' + str(N))
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - LogLog Degree Distribution.png")
plt.show()
'''
#------------------------------------------------------------------------------------------
# This section produces a fit for various small-world networks (changing N).
#------------------------------------------------------------------------------------------

averageDegree = 10
probability = 0.5

N_Array = np.arange(1000, 4050, 50)

heightArray = np.zeros(len(N_Array))
heightArrayErrors = np.zeros(len(N_Array))
centreArray = np.zeros(len(N_Array))
centreArrayErrors = np.zeros(len(N_Array))
STD_Array = np.zeros(len(N_Array))
STD_ArrayErrors = np.zeros(len(N_Array))

for i in range(len(N_Array)):

    adjacencyMatrix =  nx.to_numpy_matrix(  nx.watts_strogatz_graph(N_Array[i], averageDegree, probability)  )
    degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

    popt, pcov = curve_fit(
                        Gaussian,
                        degreeDistribution[0, :],
                        degreeDistribution[1, :],
                        (N_Array[i], averageDegree, averageDegree))

    pvar = np.diag(pcov)

    heightArray[i] = popt[0]
    heightArrayErrors[i] = np.sqrt(pvar[0])
    centreArray[i] = popt[1]
    centreArrayErrors[i] = np.sqrt(pvar[1])
    STD_Array[i] = popt[2]
    STD_ArrayErrors[i] = np.sqrt(pvar[2])
    print (N_Array[i])


fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying N) - Height.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'N', N_Array, 'Height Of Peak', heightArray)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying N) - Height Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'N', N_Array, 'Height Of Peak Errors', heightArrayErrors)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying N) - Centre.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'N', N_Array, 'Centre Of Peak', centreArray)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying N) - Centre Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'N', N_Array, 'Centre Of Peak Errors', centreArrayErrors)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying N) - STD.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'N', N_Array, 'STD Of Peak', STD_Array)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying N) - STD Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'N', N_Array, 'STD Of Peak Errors', STD_ArrayErrors)


plt.figure("Small-World Networks - Degree Distribution (Varying N - Height)")
#plt.plot(N_Array, heightArray, 'o', label='Data')
plt.errorbar(N_Array, heightArray, yerr = heightArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Number Of Nodes')
plt.ylabel('Height Of Peak')
plt.title('Degree Distribution Gaussian Fitting Of Small-World Networks (Varying N - Height Of Peak)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying N - Height).png")
plt.show()

plt.figure("Small-World Networks - Degree Distribution (Varying N - Centre)")
#plt.plot(N_Array, centreArray, 'o', label='Data')
plt.errorbar(N_Array, centreArray, yerr = centreArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Number Of Nodes')
plt.ylabel('Centre Of Peak')
plt.title('Degree Distribution Gaussian Fitting Of Small-World Networks (Varying N - Centre Of Peak)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying N - Centre).png")
plt.show()

plt.figure("Small-World Networks - Degree Distribution (Varying N - STD)")
#plt.plot(N_Array, centreArray, 'o', label='Data')
plt.errorbar(N_Array, STD_Array, yerr = STD_ArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Number Of Nodes')
plt.ylabel('Centre Of Peak')
plt.title('Degree Distribution Gaussian Fitting Of Small-World Networks (Varying N - STD)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying N - STD).png")
plt.show()



