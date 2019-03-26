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


#------------------------------------------------------------------------------------------
# This section demonstrates the degree distribution for a small-world network of a given
# size.
#------------------------------------------------------------------------------------------

N = 200
averageDegree = 20
probability = 0.6

#G = nx.watts_strogatz_graph(N, averageDegree, probability)
#plt.figure()
#nx.draw(G)
#plt.show()

adjacencyMatrix =  nx.to_numpy_matrix(  nx.watts_strogatz_graph(N, averageDegree, probability)  )
degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (N = ' + str(N) + ', P0 = ' + str(averageDegree) + ', p = ' + str(probability) + ')'
IO.WritePlottingDataToTxtFile(fileDestination, 'Degree', degreeDistribution[0,:], 'Number Of Nodes', degreeDistribution[1,:])

plt.figure("Small-World Networks - Degree Distribution")
plt.plot(degreeDistribution[0, :], degreeDistribution[1, :])



popt, pcov = curve_fit(
                        Distribution_Analysis_Functions.DiracDeltaFunction,
                        degreeDistribution[0, :],
                        degreeDistribution[1, :],
                        (averageDegree, probability))

print ('Fitted Number Of Neighboring Nodes = ' + str(popt[0]))
print ('Fitted Probability = ' + str(popt[1]))

jArray = np.linspace(degreeDistribution[0,0], degreeDistribution[0, -1], 1000)
plt.plot(jArray, N * Distribution_Analysis_Functions.DiracDeltaFunction(jArray, averageDegree, probability))


plt.grid()
plt.xlabel('Degree')
plt.ylabel('Number Of Nodes')
plt.title('Degree Distribution Of Small-World Networks, N = ' + str(N))
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution.png")


#------------------------------------------------------------------------------------------
# This section produces a fit for various small-world networks.
#------------------------------------------------------------------------------------------



