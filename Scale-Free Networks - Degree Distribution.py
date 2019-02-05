import scipy
import math as m
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import ScaleFree_Network
import Network_Analysis_Functions
import Distribution_Analysis_Functions
from Input_Output_Support_Functions import *


#------------------------------------------------------------------------------------------
# This section demonstrates the power-law tail of the degree distribution for a scale-free
# network of a given size.
#------------------------------------------------------------------------------------------

N = 500

adjacencyMatrix = ScaleFree_Network.GenerateAdjacencyMatrix(N)
degreeDistribution = Distribution_Analysis_Functions.DegreeDistributionData(adjacencyMatrix)

plt.figure("Scale-Free Networks - Degree Distribution")
plt.loglog(degreeDistribution[0, :], degreeDistribution[1, :])
plt.savefig("Scale-Free Networks - Degree Distribution.png")


#------------------------------------------------------------------------------------------
# This section fits an exponential to the power-tails of various scale-free networks.
#------------------------------------------------------------------------------------------

