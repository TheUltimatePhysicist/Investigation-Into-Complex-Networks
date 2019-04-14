import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from SupportingFunctions import Network_Analysis_Functions 
from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


def ExpectedPathLengthCurve(array, verticalTranslation):
    return ((np.log(array)) / (np.log(np.log(array)))) + verticalTranslation

#------------------------------------------------------------------------------------------
# Important Arrays.
#------------------------------------------------------------------------------------------

datasetDesignation = np.array(["socfb-Caltech36",
                               "socfb-Reed98",
                               "socfb-Haverford76",
                               "socfb-Simmons81",
                               "socfb-Swarthmore42",
                               "socfb-Amherst41",
                               "socfb-Bowdoin47",
                               "socfb-Hamilton46",
                               "socfb-Trinity100",
                               "socfb-USFCA72",
                               "socfb-Williams40",
                               "socfb-Oberlin44",
                               "socfb-Smith60",
                               "socfb-Wellesley22",
                               "socfb-Vassar85",
                               "socfb-Middlebury45",
                               "socfb-Pepperdine86",
                               "socfb-Colgate88",
                               "socfb-Santa74",
                               "socfb-Wesleyan43",
                               "socfb-Mich67",
                               "socfb-Bucknell39",
                               "socfb-Brandeis99",
                               "socfb-Howard90",
                               "socfb-Rice31"])

numberOfDatasets = len(datasetDesignation)

numberOfNodesArray_1 = np.array([769,
                               962,
                               1446,
                               1518,
                               1659,
                               2235,
                               2252,
                               2314,
                               2613,
                               2682,
                               2790,
                               2920,
                               2970,
                               2970,
                               3068,
                               3075,
                               3445,
                               3482,
                               3578,
                               3593,
                               3748,
                               3826,
                               3898,
                               4047,
                               4047])

'''
#
meanShortestPathLengths = []
numberOfNodesArray = []

for i in range(numberOfDatasets):
    dataset_G = nx.read_edgelist('NetworkRepository_Data/' + datasetDesignation[i] + '/' + datasetDesignation[i] + '.txt')
    
    if(nx.is_connected(dataset_G) == True):
        meanShortestPathLengths.append(nx.average_shortest_path_length(dataset_G))
        numberOfNodesArray.append(numberOfNodesArray_1[i])
        print(str(i) + ' is valid')
    else:
        numberOfDatasets = numberOfDatasets - 1
        print(str(i) + ' is NOT valid')

meanShortestPathLengths = np.array(meanShortestPathLengths)
numberOfNodesArray = np.array(numberOfNodesArray)

fileDestination = 'NetworkRepository_Data/AverageShortestPathLength.txt'
IO.WritePlottingDataToTxtFile(fileDestination, "Number Of Nodes", numberOfNodesArray, "Average Shortest Path Length", meanShortestPathLengths)
'''

#
fileDestination = 'NetworkRepository_Data/AverageShortestPathLength.txt'
numberArray, meanShortestPathLengths = IO.ReadPlottingDataFromTxtFile(fileDestination)

plt.figure()
plt.grid()
plt.plot(numberArray, meanShortestPathLengths, 'o', label='Data')

rejectN = ([962, 2920, 2970, 4047])
rejectL = ([2.461460580087011, 2.5794220201138502, 2.5851341528000336, 2.4174042005935936])

plt.plot(rejectN, rejectL, 'o', c='gray', label='Reject')


numberArray_temp, meanPathArray_temp = IO.CleanRepeatedValuesOfNetworkRepData(numberArray, meanShortestPathLengths)


# Fit a line to the data. Small-World.
popt, pcov = curve_fit(
                    Distribution_Analysis_Functions.LogCurve,
                    numberArray_temp, meanPathArray_temp,
                    0.4)
xArray = np.linspace(rejectN[0], rejectN[len(rejectN) - 1], 1000)
plt.plot(xArray, Distribution_Analysis_Functions.LogCurve(xArray, popt[0]), label = 'WS Curve Of Best Fit')

'''
# Fit a line to the data. Scale-Free.
popt, pcov = curve_fit(
                    ExpectedPathLengthCurve,
                    numberArray_temp, meanPathArray_temp,
                    1)
xArray = np.linspace(rejectN[0], rejectN[len(rejectN) - 1], 1000)
plt.plot(xArray, ExpectedPathLengthCurve(xArray, popt[0]), c='g', label = 'BA Curve Of Best Fit')
'''

plt.ylim(2, 3)
plt.legend(loc='best')
plt.xlabel("Number Of Nodes")
plt.ylabel("Average Shortest Path Length")
plt.title("Average Shortest Path Length Of Social Media Networks (Varying N)")
plt.savefig("NetworkRepository_Data/Average Shortest Path Length Of Social Media Networks (Varying N)")
plt.close()


print('')
print('----------------------------------------------')

pvar = np.diag(pcov)

print('ScalingFactor = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
#print('Gradient = ' + str(popt[0]) + ' +/- ' + str(np.sqrt(pvar[0])))
#print('Intercept = ' + str(popt[1]) + ' +/- ' + str(np.sqrt(pvar[1])))
print('----------------------------------------------')
print('')


differences = meanShortestPathLengths - Distribution_Analysis_Functions.LogCurve(numberArray, popt[0])
sum = 0
for i in range(len(meanShortestPathLengths)):
    sum += (differences[i])**2
RMS_Diff = (sum / len(meanShortestPathLengths))**(0.5)
print (RMS_Diff)



