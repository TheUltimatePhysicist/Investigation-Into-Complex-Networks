import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from NetworkTypes import ScaleFree_Network
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

array1 = np.log(degreeDistribution[0,1:])
array2 = np.log(degreeDistribution[1, 1:])
for i in range(len(degreeDistribution)):
    if (np.isfinite(array1[i]) == False):    array1[i] = 0
    if (np.isfinite(array2[i]) == False):    array2[i] = 0
'''
array1 = np.nan_to_num(np.log(degreeDistribution[0, :]))
array2 = np.nan_to_num(np.log(degreeDistribution[1, :]))
estimatedGammaValue = -3
estimatedIntercept = 0
popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        array1,
                        array2,
                        estimatedGammaValue,
                        estimatedIntercept)

newDegreeArray = np.linspace(0, N, 1000)
#popt[0] = estimatedGammaValue

plt.plot(newDegreeArray, N*Distribution_Analysis_Functions.ExponentialTail(newDegreeArray, popt[0]))

print(popt[0])
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.title('Degree Distribution Of Scale-Free Networks, N = ' + str(N))
plt.savefig("Scale-Free Networks - Degree Distribution.png")




plt.figure("Scale-Free Networks - LogLog Degree Distribution")
plt.loglog(degreeDistribution[0, :], degreeDistribution[1, :], 'o')

newDegreeArray(0, np.log(N), 1000)
plt.plot(newDegreeArray, N *Distribution_Analysis_Functions.StraightLine(newDegreeArray, popt[0], popt[1]))

plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.title('Log-Log Degree Distribution Of Scale-Free Networks, N = ' + str(N))
plt.savefig("Scale-Free Networks - LogLog Degree Distribution.png")


#------------------------------------------------------------------------------------------
# This section fits an exponential to the power-tails of various scale-free networks.
#------------------------------------------------------------------------------------------




