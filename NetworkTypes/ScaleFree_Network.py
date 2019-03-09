import numpy as np
import random

import networkx as nx


# Create an adjacency matrix which corresponds to a scale-free network.

def GenerateAdjacencyMatrix(numberOfNodes, alpha = 0.41, beta = 0.54, gamma = 0.05, delta_in = 0.2, delta_out = 0, createUsing = None, seed = None):

    """
    Parameters:	
        n (integer) – Number of nodes in graph
        alpha (float) – Probability for adding a new node connected to an existing node chosen randomly according to the in-degree distribution.
        beta (float) – Probability for adding an edge between two existing nodes. One existing node is chosen randomly according the in-degree distribution and the other chosen randomly according to the out-degree distribution.
        gamma (float) – Probability for adding a new node connected to an existing node chosen randomly according to the out-degree distribution.
        delta_in (float) – Bias for choosing ndoes from in-degree distribution.
        delta_out (float) – Bias for choosing ndoes from out-degree distribution.
        create_using (graph, optional (default MultiDiGraph)) – Use this graph instance to start the process (default=3-cycle).
        seed (integer, optional) – Seed for random number generator

    NOTE: Alpha + Beta + Gamma = 1
    """

    G = nx.scale_free_graph(numberOfNodes, alpha, beta, gamma, delta_in, delta_out, createUsing, seed)
    adjacencyMatrix = nx.to_numpy_matrix(G)

    return adjacencyMatrix


