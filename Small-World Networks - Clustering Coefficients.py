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


def ExpectedClusteringValue(k, p):
    return ((3*(k - 1)) / (2*((2*k) - 1))) * ((1 - p)**3)


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed probability value and varying node number, to determine how the
# clustering coefficient changes over a range of N.
#--------------------------------------------------------------------------------------------------
#
# Initialise the probability and N array.
probability = 0.50
N_Array = np.arange(50, 1050, 50)

proportionOfAverageDegree = 20/50
averageDegree = 5

# Compute the clustering coefficient values.
clusteringCoefficientArray = np.zeros(N_Array.shape[0])


for i in range(0, N_Array.shape[0]):

    summation = 0

    numberOfRepeats = 10
    for j in range(numberOfRepeats):
        #averageDegree = int(proportionOfAverageDegree * N_Array[i])

        smallWorlds_G = nx.watts_strogatz_graph(int(N_Array[i]),
                                                int(averageDegree),
                                                probability)
        summation += nx.average_clustering(smallWorlds_G)
    
    clusteringCoefficientArray[i] = summation / numberOfRepeats


# Output the data to a .txt file.
fileDestination = 'NetworkTypes/SmallWorld_Network/AverageClusteringCoefficients (Varying N).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "N", N_Array, "Difference", clusteringCoefficientArray)


fileDestination = 'NetworkTypes/SmallWorld_Network/AverageClusteringCoefficients (Varying N).txt'
N_Array, clusteringCoefficientArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

# Plot the resulting data.
plt.figure()
plt.plot(N_Array, clusteringCoefficientArray, 'o')

#expectedClusteringValue = ((3*(averageDegree -1)) / (2*((2*averageDegree) - 1))) * ((1 - probability)**3)

plt.plot(N_Array, ExpectedClusteringValue(averageDegree, probability)*(N_Array**0))

plt.ylim(0, 1)
plt.xlabel("Number Of Nodes")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Small-World Networks (Varying N)")
plt.grid()
plt.savefig('NetworkTypes/SmallWorld_Network/Average Clustering Coefficients Of Small-World Networks(Varying N)')


#--------------------------------------------------------------------------------------------------
# This section looks at a fixed node number and varying probability, to determine how the
# clustering coefficient changes over a range of probabilities.
#--------------------------------------------------------------------------------------------------
#
# Initialise N and the probability array.
N = 1000
P_Array = np.arange(0.05, 1.05, 0.05)

averageDegree = 5


# Compute the clustering coefficient values.
clusteringCoefficientArray = np.zeros(P_Array.shape[0])

for i in range(0, P_Array.shape[0]):

    summation = 0
    numberOfRepeats = 5
    for j in range(numberOfRepeats):
        smallWorlds_G = nx.watts_strogatz_graph(N,
                                                int(averageDegree),
                                                P_Array[i])
        summation += nx.average_clustering(smallWorlds_G)
                                               
    clusteringCoefficientArray[i] = summation / numberOfRepeats



# Plot the resulting data.
plt.figure("Clustering Coefficients Of Small-World Networks (N = " + str(N) + ")")
plt.plot(P_Array, clusteringCoefficientArray, 'o')

xArray = np.linspace(P_Array[0], P_Array[-1], 1000)
plt.plot(xArray, ExpectedClusteringValue(averageDegree, xArray))

plt.xlabel("Probability")
plt.ylabel("Clustering Coefficient")
plt.title("Clustering Coefficients Of Small-World Networks (N = " + str(N) + ")")
plt.grid()
plt.savefig('NetworkTypes/SmallWorld_Network/Average Clustering Coefficients Of Small-World Networks(Varying P)')
plt.show()


# Output the data to a .txt file.
fileDestination = 'NetworkTypes/SmallWorld_Network/AverageClusteringCoefficients (Varying P).txt'
IO.WritePlottingDataToTxtFile(fileDestination, "P", P_Array, "Difference", clusteringCoefficientArray)

