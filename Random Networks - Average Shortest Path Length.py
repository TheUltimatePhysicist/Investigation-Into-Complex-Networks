import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from NetworkTypes.Random_Network import Random_Network
from SupportingFunctions import Network_Analysis_Functions 
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


#------------------------------------------------------------------------------------------
# Determine how the average shortest path length varies for random networks (varying N).
#------------------------------------------------------------------------------------------

# Initialise the probability and N array.
probability = 0.5
N_Array = np.arange(50, 1050, 50)

'''
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

fileDestination = 'NetworkTypes/Random_Network/AverageShortestPathLength (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "Number Of Nodes", N_Array, "Average Shortest Path Length", meanShortestPathArray)
'''
fileDestination = 'NetworkTypes/Random_Network/AverageShortestPathLength (Varying N).txt'
N_Array, meanShortestPathArray = IO.ReadPlottingDataFromTxtFile(fileDestination)


plt.figure()
plt.grid()
plt.plot(N_Array, meanShortestPathArray, label = 'Data')

# Fit a line to the data.
popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        N_Array, meanShortestPathArray,
                        (0, 1.5))

xArray = np.linspace(N_Array[0], N_Array[len(N_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')

plt.ylim(1,2)
plt.legend(loc='best')
plt.xlabel("Number Of Nodes")
plt.ylabel("Mean Shortest Path Length")
plt.title("Mean Shortest Path Length Of Random Networks (Varying N)")
plt.savefig("NetworkTypes/Random_Network/Mean Shortest Path Length Of Random Networks (Varying N)")
plt.close()

print('')
print('----------------------------------------------')

pvar = np.diag(pcov)

print('Gradient = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
print('Intercept = ' + str(popt[1]) + ' +/- ' + str(np.sqrt(pvar[1])))
print('----------------------------------------------')
print('')



#------------------------------------------------------------------------------------------
# Determine how the average shortest path length varies for random networks (varying P).
#------------------------------------------------------------------------------------------

# Initialise the N value and P array.
N = 500
P_Array = np.arange(0.05, 1.05, 0.05)

'''
# Create the adjacency matrices for varying P.
random_G = [None] * len(P_Array)

for i in range(0, P_Array.shape[0]):

    adjacencyMatrix = Random_Network.GenerateAdjacencyMatrix(N, P_Array[i])

    random_G[i] = nx.from_numpy_matrix(adjacencyMatrix)
    
    print('P = ' + str(P_Array[i]) + ' Generated')

	
for i in range(0, P_Array.shape[0]):
    meanShortestPathArray[i] = nx.average_shortest_path_length(random_G[i])

    print('P = ' + str(P_Array[i]) + ' Length Found')

fileDestination = 'NetworkTypes/Random_Network/AverageShortestPathLength (Varying P).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "Probability", P_Array, "Average Shortest Path Length", meanShortestPathArray)
'''

fileDestination = 'NetworkTypes/Random_Network/AverageShortestPathLength (Varying P).txt'
P_Array, meanShortestPathArray = IO.ReadPlottingDataFromTxtFile(fileDestination)


plt.figure()
plt.grid()
plt.plot(P_Array, meanShortestPathArray, label = 'Data')

#
popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.StraightLine,
                        P_Array, meanShortestPathArray,
                        (-1, 2))

xArray = np.linspace(P_Array[0], P_Array[len(P_Array) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.StraightLine(xArray, popt[0], popt[1]), label = 'Line Of Best Fit')


plt.legend(loc='best')
plt.xlabel("Probability")
plt.ylabel("Mean Shortest Path Length")
plt.title("Mean Shortest Path Length Of Random Networks (Varying P)")
plt.savefig("NetworkTypes/Random_Network/Mean Shortest Path Length Of Random Networks (Varying P)")
plt.close()


print('')
print('----------------------------------------------')

pvar = np.diag(pcov)

print('Gradient = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
print('Intercept = ' + str(popt[1]) + ' +/- ' + str(np.sqrt(pvar[1])))
print('----------------------------------------------')
print('')

