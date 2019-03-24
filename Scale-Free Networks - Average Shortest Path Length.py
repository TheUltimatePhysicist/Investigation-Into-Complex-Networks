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


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed probability value and varying node number, to determine how the
# average shortest path length changes over a range of N.
#--------------------------------------------------------------------------------------------------
#
# Initialise the probability and N array.
N_Array = np.arange(50, 1050, 50)

# Create the adjacency matrices for varying N.
scaleFrees_G = [None] * len(N_Array)


for i in range(0, N_Array.shape[0]):

    scaleFrees_G[i] = nx.scale_free_graph(int(N_Array[i]))
    
    print('N = ' + str(N_Array[i]) + ' Generated')

               
# Compute the clustering coefficient values.
averageShortestPathLengths = np.zeros(N_Array.shape[0])

for i in range(0, N_Array.shape[0]):
    
    averageShortestPathLengths[i] = nx.average_shortest_path_length(scaleFrees_G[i])
    print ("N = " + str(N_Array[i]) + ", Coefficient = " + str(averageShortestPathLengths[i]))

# Output the data to a .txt file.
fileDestination = 'NetworkTypes/ScaleFree_Network/AverageShortestPathLengths (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "N", N_Array, "Difference", averageShortestPathLengths)


fileDestination = 'NetworkTypes/ScaleFree_Network/AverageShortestPathLengths (Varying N).txt'
N_Array, averageShortestPathLengths = IO.ReadPlottingDataFromTxtFile(fileDestination)

# Plot the resulting data.
plt.figure()
plt.plot(N_Array, averageShortestPathLengths)

plt.ylim(0, 1)
plt.xlabel("Number Of Nodes")
plt.ylabel("Average Shortest Path Length")
plt.title("Average Shortest Path Lengths Of Scale-Free Networks (Varying N)")
plt.grid()
plt.savefig('NetworkTypes/ScaleFree_Network/Average Shortest Path Lengths Of Scale-Free Networks(Varying N)')

