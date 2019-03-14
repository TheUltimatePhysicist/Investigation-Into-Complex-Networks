import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from SupportingFunctions import Distribution_Analysis_Functions
from SupportingFunctions import Input_Output_Support_Functions as IO


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


numberOfDatasets = len(datasetDesignation) + 1

datasets_G = [None] * numberOfDatasets
datasets_adjacencyMatrices = [None] * numberOfDatasets
datasets_DegreeDistributionData = [None] * numberOfDatasets


for i in range(0, numberOfDatasets - 1):

    datasets_G[i] = nx.read_edgelist('NetworkRepository_Data/' + datasetDesignation[i] + '/' + datasetDesignation[i] + '.txt')
    datasets_adjacencyMatrices[i] = nx.to_numpy_matrix(datasets_G[i])
    datasets_DegreeDistributionData[i] = Distribution_Analysis_Functions.DegreeDistributionData(datasets_adjacencyMatrices[i])

    fileDestination = 'NetworkRepository_Data/' + datasetDesignation[i] + '/' + datasetDesignation[i] + '_DegreeDistribution.txt'
    IO.WritePlottingDataToTxtFile(fileDestination, "Degree", datasets_DegreeDistributionData[i][0, :], "Number Of Nodes", datasets_DegreeDistributionData[i][1, :])


