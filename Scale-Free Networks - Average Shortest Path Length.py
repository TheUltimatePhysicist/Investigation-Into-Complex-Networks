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


def ExpectedPathLengthCurve(array, verticalTranslation, scalingFactor):
    return (((np.log(array)) / (np.log(np.log(array)))) + verticalTranslation)*scalingFactor


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed probability value and varying node number, to determine how the
# average shortest path length changes over a range of N.
#--------------------------------------------------------------------------------------------------
#
# Initialise the probability and N array.
N_Array = np.arange(1000, 4050, 50)

'''
# Compute the clustering coefficient values.
averageShortestPathLengths = np.zeros(N_Array.shape[0])

for i in range(0, N_Array.shape[0]):

    summation = 0
    numberOfRepeats = 3

    for j in range(numberOfRepeats):
        scaleFrees_G = nx.barabasi_albert_graph(N_Array[i], 5)

        summation += nx.average_shortest_path_length(scaleFrees_G)
    averageShortestPathLengths[i] = summation / numberOfRepeats
    #print(ExpectedPathLengthCurve(N_Array[i]))
    print (averageShortestPathLengths[i])
    print ('---')



# Output the data to a .txt file.
fileDestination = 'NetworkTypes/ScaleFree_Network/AverageShortestPathLengths (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "N", N_Array, "Difference", averageShortestPathLengths)
'''
fileDestination = 'NetworkTypes/ScaleFree_Network/AverageShortestPathLengths (Varying N).txt'
N_Array, averageShortestPathLengths = IO.ReadPlottingDataFromTxtFile(fileDestination)


# Plot the resulting data.
plt.figure()
plt.plot(N_Array, averageShortestPathLengths, 'o', label='Data')


popt, pcov = curve_fit(
                   ExpectedPathLengthCurve,
                   N_Array, averageShortestPathLengths,
                   (1, 1))

xArray = np.linspace(N_Array[0], N_Array[-1], 1000)
plt.plot(xArray, ExpectedPathLengthCurve(xArray, popt[0], popt[1]), label='Curve Of Best Fit')
print (popt[0])
#plt.ylim(0, 1)
plt.legend(loc='best')
plt.xlabel("Number Of Nodes")
plt.ylabel("Average Shortest Path Length")
plt.title("Average Shortest Path Lengths Of Scale-Free Networks (Varying N)")
plt.grid()
plt.savefig('NetworkTypes/ScaleFree_Network/Average Shortest Path Lengths Of Scale-Free Networks(Varying N)')

