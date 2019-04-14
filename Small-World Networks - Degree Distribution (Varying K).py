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
# This section produces a fit for various small-world networks (changing K).
#------------------------------------------------------------------------------------------

N = 4000
probability = 0.5

K_Array = np.arange(5, 105, 5)

heightArray = np.zeros(len(K_Array))
heightArrayErrors = np.zeros(len(K_Array))
centreArray = np.zeros(len(K_Array))
centreArrayErrors = np.zeros(len(K_Array))
STD_Array = np.zeros(len(K_Array))
STD_ArrayErrors = np.zeros(len(K_Array))

for i in range(len(K_Array)):

    adjacencyMatrix =  nx.to_numpy_matrix(  nx.watts_strogatz_graph(N, K_Array[i], probability)  )
    degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

    popt, pcov = curve_fit(
                        Gaussian,
                        degreeDistribution[0, :],
                        degreeDistribution[1, :],
                        (N, K_Array[i], K_Array[i]))
    
    #plt.figure()
    #plt.plot(degreeDistribution[0, :], degreeDistribution[1, :], 'o')
    #jArray = np.linspace(degreeDistribution[0,0], degreeDistribution[0, -1], 20000)
    #plt.plot(jArray, Gaussian(jArray, popt[0], popt[1], popt[2]), label='Curve Of Best Fit')
    #plt.xlim(0, 200)
    #plt.grid()
    #plt.legend(loc='best')
    #plt.xlabel('Degree')
    #plt.ylabel('Number Of Nodes')
    #plt.title('Degree Distribution Of Small-World Networks, K = ' + str(K_Array[i]))
    #plt.savefig("NetworkTypes/SmallWorld_Network/Debug/Small-World Networks - Degree Distribution (Varying K).png")
    

    pvar = np.diag(pcov)

    heightArray[i] = popt[0]
    heightArrayErrors[i] = np.sqrt(pvar[0])
    centreArray[i] = popt[1]
    centreArrayErrors[i] = np.sqrt(pvar[1])
    STD_Array[i] = np.sqrt((popt[2])**2)
    STD_ArrayErrors[i] = np.sqrt(pvar[2])
    print (K_Array[i])


fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying K) - Height.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'K', K_Array, 'Height Of Peak', heightArray)
#K_Array, heightArray = IO.ReadPlottingDataFromTxtFile(fileDestination)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying K) - Height Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'K', K_Array, 'Height Of Peak Errors', heightArrayErrors)
#K_Array, heightArrayErrors = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying K) - Centre.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'K', K_Array, 'Centre Of Peak', centreArray)
#K_Array, centreArray = IO.ReadPlottingDataFromTxtFile(fileDestination)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying K) - Centre Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'K', K_Array, 'Centre Of Peak Errors', centreArrayErrors)
#K_Array, centreArrayErrors = IO.ReadPlottingDataFromTxtFile(fileDestination)

fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying K) - STD.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'K', K_Array, 'STD Of Peak', STD_Array)
#K_Array, STD_Array = IO.ReadPlottingDataFromTxtFile(fileDestination)
fileDestination = 'NetworkTypes/SmallWorld_Network/DegreeDistribution (Varying K) - STD Errors.txt'
IO.WritePlottingDataToTxtFile(fileDestination, 'K', K_Array, 'STD Of Peak Errors', STD_ArrayErrors)
#K_Array, STD_ArrayErrors = IO.ReadPlottingDataFromTxtFile(fileDestination)


plt.figure("Small-World Networks - Degree Distribution (Varying K - Height)")
#plt.plot(N_Array, heightArray, 'o', label='Data')
plt.errorbar(K_Array, heightArray, yerr = heightArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Initial Degree')
plt.ylabel('Height Of Peak')
plt.title('Gaussian Fitting Of Small-World Networks (Varying K - Height Of Peak)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying K - Height).png")
plt.show()

plt.figure()
plt.plot(np.log(K_Array), np.log(heightArray), 'o')
plt.show()

plt.figure("Small-World Networks - Degree Distribution (Varying K - Centre)")
#plt.plot(N_Array, centreArray, 'o', label='Data')
plt.errorbar(K_Array, centreArray, yerr = centreArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Initial Degree')
plt.ylabel('Centre Of Peak')
plt.title('Gaussian Fitting Of Small-World Networks (Varying K - Centre Of Peak)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying K - Centre).png")
plt.show()

plt.figure("Small-World Networks - Degree Distribution (Varying K - STD)")
#plt.plot(N_Array, centreArray, 'o', label='Data')
plt.errorbar(K_Array, STD_Array, yerr = STD_ArrayErrors/2, fmt = 'o', label='Data')
plt.grid()
plt.legend(loc='best')
plt.xlabel('Initial Degree')
plt.ylabel('STD Of Peak')
plt.title('Gaussian Fitting Of Small-World Networks (Varying K - STD)')
plt.savefig("NetworkTypes/SmallWorld_Network/Small-World Networks - Degree Distribution (Varying K - STD).png")
plt.show()



