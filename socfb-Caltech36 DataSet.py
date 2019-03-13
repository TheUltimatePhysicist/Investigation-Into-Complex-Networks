import networkx as nx
import matplotlib.pyplot as plt

from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


# Number Of Nodes = 769

G = nx.read_edgelist('NetworkRepository_Data/socfb-Caltech36/socfb-Caltech36.txt')

print (len(G))
print (nx.number_of_edges(G))
print (nx.average_clustering(G))

#plt.axis('off')

#nx.draw_networkx(G, with_labels = False, node_size = 35)
#plt.show()


# Extract degree distribution data 
# ([0, :] = x = degree, [1, :] = y = number of nodes)

adjacencyMatrix = nx.to_numpy_matrix(G)

degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

fileDestination = 'NetworkRepository_Data/socfb-Caltech36/socfb-Caltech36_DegreeDistribution.txt'
IO.WritePlottingDataToTxtFile(fileDestination, "Degree", degreeDistribution[0, :], "Number Of Nodes", degreeDistribution[1, :])


degreeArray, numberArray = IO.ReadPlottingDataFromTxtFile(fileDestination)

# Plot the degree distribution data.

plt.figure()
plt.plot(degreeArray, numberArray)
plt.xlabel("Degree")
plt.ylabel("Number Of Nodes")
plt.title("Degree Distribution For socfb-Caltech36 (N = " + str(len(G)) + ")")
#plt.legend(loc = "best")
plt.grid()
#plt.savefig("Degree Distribution For socfb-Caltech36 (N = " + str(len(G)) + ")")
plt.show()
