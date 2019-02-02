import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# Create a numpy matrix.

adjacencyMatrix = np.array([[0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                           [1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                           [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                           [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
                           [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
                           [1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                           [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]])

# Note the above matrix comes from the following website: 
# https://www.sciencedirect.com/science/article/pii/S1568494616300242
#
# Also note that the generated plot is from range 0 to 9 where the
# source is from 1 to 10, the resulting plot is therefore correct.


# Initialise a graph.
#
# This step was taken from the following website tutorial:
# http://www.cse.ust.hk/~lhouab/tutorial/tutor_3.html

G = nx.from_numpy_matrix(adjacencyMatrix)


# Plot the network graph.

plt.figure()
nx.draw(G, with_labels = True, font_weight = 'bold')
plt.show()
