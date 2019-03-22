import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from NetworkTypes import Random_Network
from SupportingFunctions import Network_Analysis_Functions 
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


#------------------------------------------------------------------------------------------
# Determine how the average shortest path length varies for random networks (varying N).
#------------------------------------------------------------------------------------------

# Initialise the probability and N array.
probability = 0.5
N_Array = np.arange(50, 1050, 50)


# Create the adjacency matrices for varying N.
random_G = [None] * len(N_Array)

for i in range(0, N_Array.shape[0]):

    adjacencyMatrix = Random_Network.GenerateAdjacencyMatrix(N_Array[i], probability)

    random_G[i] = nx.from_numpy_matrix(adjacencyMatrix)
    
    print('N = ' + str(N_Array[i]) + ' Generated')

                                        
meanShortestPathArray = np.zeros(N_Array.shape[0])

for i in range(0, N_Array.shape[0]):
    meanShortestPathArray[i] = nx.average_shortest_path_length(random_G[i])

    print('N = ' + str(N_Array[i]) + ' Length Found')

print (meanShortestPathArray)


plt.figure()
plt.grid()
plt.plot(N_Array, meanShortestPathArray, label = 'Data')
'''
# Fit a log-e curve to the data.
popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.LogCurve,
                        N_Array, meanShortestPathArray,
                        (0.4))

xArray = np.linspace(N_Array[0], N_Array[len(N_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.LogCurve(xArray, popt[0]), label = 'Curve Of Best Fit')
'''
plt.legend(loc='best')
plt.xlabel("Number Of Nodes")
plt.ylabel("Mean Shortest Path Length")
plt.title("Mean Shortest Path Length Of Random Networks (Varying N)")
plt.savefig("Mean Shortest Path Length Of Random Networks (Varying N)")
plt.close()
'''
print('')
print('----------------------------------------------')

pvar = np.diag(pcov)

print('Coefficient = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
print('----------------------------------------------')
print('')
'''

