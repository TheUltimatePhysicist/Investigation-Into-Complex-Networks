import scipy
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


def Gaussian(xArray, height, centre, sigma):
    return height * np.exp(((xArray - centre)**2)/(-2*(sigma**2)))


#------------------------------------------------------------------------------------------
# This section produces a fit for various small-world networks (changing P).
#------------------------------------------------------------------------------------------

N = 4000
averageDegree = 10

P_Array = np.arange(0.05, 1.05, 0.05)

heightArray = np.zeros(len(P_Array))
heightArrayErrors = np.zeros(len(P_Array))
centreArray = np.zeros(len(P_Array))
centreArrayErrors = np.zeros(len(P_Array))
STD_Array = np.zeros(len(P_Array))
STD_ArrayErrors = np.zeros(len(P_Array))

for i in range(len(P_Array)):

    adjacencyMatrix =  nx.to_numpy_matrix(  nx.watts_strogatz_graph(N, averageDegree, P_Array[i])  )
    degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

    popt, pcov = curve_fit(
                        Gaussian,
                        degreeDistribution[0, :],
                        degreeDistribution[1, :],
                        (N, averageDegree, averageDegree))

    #plt.figure()
    #plt.plot(degreeDistribution[0, :], degreeDistribution[1, :], 'o')
    #jArray = np.linspace(degreeDistribution[0,0], degreeDistribution[0, -1], 20000)
    #plt.plot(jArray, Gaussian(jArray, popt[0], popt[1], popt[2]), label='Curve Of Best Fit')
    #plt.xlim(0, 200)
    #plt.grid()
    #plt.legend(loc='best')
    #plt.xlabel('Degree')
    #plt.ylabel('Number Of Nodes')
    #plt.title('Degree Distribution Of Small-World Networks, P = ' + str(P_Array[i]))
    #plt.savefig("NetworkTypes/SmallWorld_Network/Debug/Small-World Networks - Degree Distribution (Varying P).png")


    pvar = np.diag(pcov)

    heightArray[i] = popt[0]
    heightArrayErrors[i] = np.sqrt(pvar[0])
    centreArray[i] = popt[1]
    centreArrayErrors[i] = np.sqrt(pvar[1])
    STD_Array[i] = np.sqrt((popt[2])**2)
    STD_ArrayErrors[i] = np.sqrt(pvar[2])
    print (P_Array[i])


fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying P) - Height.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'P', P_Array, 'Height Of Peak', heightArray)
#P_Array, heightArray = IO.ReadPlottingDataFromTxtFile(fileDestination)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying P) - Height Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'P', P_Array, 'Height Of Peak Errors', heightArrayErrors)
#P_Array, heightArrayErrors = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying P) - Centre.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'P', P_Array, 'Centre Of Peak', centreArray)
#P_Array, centreArray = IO.ReadPlottingDataFromTxtFile(fileDestination)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying P) - Centre Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'P', P_Array, 'Centre Of Peak Errors', centreArrayErrors)
#P_Array, centreArrayErrors = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying P) - STD.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'P', P_Array, 'STD Of Peak', STD_Array)
#P_Array, STD_Array = IO.ReadPlottingDataFromTxtFile(fileDestination)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying P) - STD Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'P', P_Array, 'STD Of Peak Errors', STD_ArrayErrors)
#P_Array, STD_ArrayErrors = IO.ReadPlottingDataFromTxtFile(fileDestination)


plt.figure("Small-World Networks - Degree Distribution (Varying P - Height)")
#plt.plot(N_Array, heightArray, 'o', label='Data')
plt.errorbar(P_Array, heightArray, yerr = heightArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Probability')
plt.ylabel('Height Of Peak')
plt.title('Degree Distribution Gaussian Fitting Of Small-World Networks (Varying P - Height Of Peak)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying P - Height).png")
plt.show()


plt.figure()
plt.plot(np.log(P_Array), np.log(heightArray), 'o')
plt.show()


plt.figure("Small-World Networks - Degree Distribution (Varying P - Centre)")
#plt.plot(N_Array, centreArray, 'o', label='Data')
plt.errorbar(P_Array, centreArray, yerr = centreArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Probability')
plt.ylabel('Centre Of Peak')
plt.title('Degree Distribution Gaussian Fitting Of Small-World Networks (Varying P - Centre Of Peak)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying P - Centre).png")
plt.show()

plt.figure("Small-World Networks - Degree Distribution (Varying P - STD)")
#plt.plot(N_Array, centreArray, 'o', label='Data')
plt.errorbar(P_Array, STD_Array, yerr = STD_ArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Probability')
plt.ylabel('STD Of Peak')
plt.title('Degree Distribution Gaussian Fitting Of Small-World Networks (Varying P - STD)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying P - STD).png")
plt.show()



