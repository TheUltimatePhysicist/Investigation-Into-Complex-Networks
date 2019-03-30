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


def ExpectedScaleFreeClusteringCurve(xArray, constant, scalingFactor):
    return scalingFactor*(xArray**(-1*constant))


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed probability value and varying node number, to determine how the
# clustering coefficient changes over a range of N.
#--------------------------------------------------------------------------------------------------
#
# Initialise the probability and N array.
N_Array = np.arange(1000, 4050, 50)

#proportionOfAverageDegree = 20/50
               
# Compute the clustering coefficient values.
clusteringCoefficientArray = np.zeros(N_Array.shape[0])



for i in range(0, N_Array.shape[0]):

    sum = 0
    numberOfRepeats = 10

    for j in range(numberOfRepeats):
        scaleFrees_G = nx.barabasi_albert_graph(N_Array[i], 5)
        sum += nx.average_clustering(scaleFrees_G)
    
    clusteringCoefficientArray[i] = sum / numberOfRepeats

    print ("N = " + str(N_Array[i]) + ", Coefficient = " + str(clusteringCoefficientArray[i]))



# Output the data to a .txt file.
fileDestination = 'NetworkTypes/ScaleFree_Network/AverageClusteringCoefficients (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "N", N_Array, "Difference", clusteringCoefficientArray)


fileDestination = 'NetworkTypes/ScaleFree_Network/AverageClusteringCoefficients (Varying N).txt'
N_Array, clusteringCoefficientArray = IO.ReadPlottingDataFromTxtFile(fileDestination)


# Plot the resulting data.
plt.figure()
plt.plot(N_Array, clusteringCoefficientArray, 'o', label='Data')


popt, pcov = curve_fit(
                        ExpectedScaleFreeClusteringCurve,
                        N_Array,
                        clusteringCoefficientArray,
                        (0.75, 1))


curveArray = np.linspace(N_Array[0], N_Array[len(N_Array)-1], 1000)
plt.plot(curveArray, ExpectedScaleFreeClusteringCurve(curveArray, popt[0], popt[1]), label='Curve Of Best Fit')
print (popt[0])
print (popt[1])

#plt.ylim(0, 0.5)
plt.legend(loc='best')
plt.xlabel("Number Of Nodes")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Scale-Free Networks (Varying N)")
plt.grid()
plt.savefig('NetworkTypes/ScaleFree_Network/Average Clustering Coefficients Of Scale-Free Networks(Varying N)')


