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


def ExpectedScaleFreeClusteringCurve(xArray):
    return xArray**(-0.75)


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed probability value and varying node number, to determine how the
# clustering coefficient changes over a range of N.
#--------------------------------------------------------------------------------------------------
#
# Initialise the probability and N array.
probability = 0.50
N_Array = np.arange(50, 3050, 50)

#proportionOfAverageDegree = 20/50
               
# Compute the clustering coefficient values.
clusteringCoefficientArray = np.zeros(N_Array.shape[0])



for i in range(0, N_Array.shape[0]):

    sum = 0
    numberOfRepeats = 10

    for j in range(numberOfRepeats):
        scaleFrees_G = nx.from_numpy_matrix(  nx.to_numpy_matrix(  nx.scale_free_graph(int(N_Array[i]))  )   )
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
plt.plot(N_Array, clusteringCoefficientArray)

curveArray = np.linspace(N_Array[0], N_Array[len(N_Array)-1], 1000)
plt.plot(curveArray, ExpectedScaleFreeClusteringCurve(curveArray))

plt.ylim(0, 1)
plt.xlabel("Number Of Nodes")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Scale-Free Networks (Varying N)")
plt.grid()
plt.savefig('NetworkTypes/ScaleFree_Network/Average Clustering Coefficients Of Scale-Free Networks(Varying N)')


