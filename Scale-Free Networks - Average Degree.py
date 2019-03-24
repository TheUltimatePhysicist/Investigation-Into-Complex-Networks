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
# This section looks at a varying node number, to determine how the average degree changes over
# a range of N.
#--------------------------------------------------------------------------------------------------
#
# Initialise the N array.
N_Array = np.arange(50, 1050, 50)


# Compute the clustering coefficient values.
averageDegreeArray = np.zeros(N_Array.shape[0])

for i in range(0, N_Array.shape[0]):
    
    sum = 0
    for j in range(10):
        adjacencyMatrix = ScaleFree_Network.GenerateAdjacencyMatrix(N_Array[i])
        sum += Network_Analysis_Functions.AverageDegree(adjacencyMatrix)

    averageDegreeArray[i] = sum / 10
    print ("N = " + str(N_Array[i]) + ", Average k = " + str(averageDegreeArray[i]))

# Output the data to a .txt file.
fileDestination = 'NetworkTypes/ScaleFree_Network/AverageDegree (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "N", N_Array, "Difference", averageDegreeArray)


fileDestination = 'NetworkTypes/ScaleFree_Network/AverageDegree (Varying N).txt'
N_Array, averageDegreeArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

# Plot the resulting data.
plt.figure()
plt.plot(N_Array, averageDegreeArray)

plt.ylim(1, 3)
plt.xlabel("Number Of Nodes")
plt.ylabel("Average Degree")
plt.title("Average Degree Of Scale-Free Networks (Varying N)")
plt.grid()
plt.savefig('NetworkTypes/ScaleFree_Network/Average Degree Of Scale-Free Networks(Varying N)')

