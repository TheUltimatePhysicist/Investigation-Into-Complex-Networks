import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from NetworkTypes import SmallWorld_Network
from SupportingFunctions import Network_Analysis_Functions 
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


#------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------

# Initialise the probability and N array.
probability = 0.50
N_Array = np.arange(1000, 4050, 50)


# Create the adjacency matrices for varying N.
smallWorlds_G = [None] * len(N_Array)

for i in range(0, N_Array.shape[0]):

    averageDegree = 20#probability * N_Array[i]

    smallWorlds_G[i] = nx.watts_strogatz_graph(int(N_Array[i]),
                                               int(averageDegree),
                                               probability)
    
    print('N = ' + str(N_Array[i]) + ' Generated')

                                        
meanShortestPathArray = np.zeros(N_Array.shape[0])

for i in range(0, N_Array.shape[0]):
    meanShortestPathArray[i] = nx.average_shortest_path_length(smallWorlds_G[i])

    print('N = ' + str(N_Array[i]) + ' Length Found')

print (meanShortestPathArray)


plt.figure()
plt.grid()
plt.plot(N_Array, meanShortestPathArray, 'o', label = 'Data')

# Fit a log-e curve to the data.
popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.LogCurve,
                        N_Array, meanShortestPathArray,
                        (0.4))

xArray = np.linspace(N_Array[0], N_Array[len(N_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.LogCurve(xArray, popt[0]), label = 'Curve Of Best Fit')

plt.legend(loc='best')
plt.xlabel("Number Of Nodes")
plt.ylabel("Mean Shortest Path Length")
plt.title("Mean Shortest Path Length Of Small-World Networks (Varying N)")
plt.savefig("NetworkTypes/SmallWorld_Network/Mean Shortest Path Length Of Small-World Networks (Varying N)")
plt.close()

print('')
print('----------------------------------------------')

pvar = np.diag(pcov)

print('Coefficient = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
print('----------------------------------------------')
print('')

