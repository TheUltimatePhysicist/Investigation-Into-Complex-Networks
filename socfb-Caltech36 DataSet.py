
import networkx as nx

from scipy.io import mmread

#rawData = mmread('socfb-Caltech36.mtx')

G = nx.read_edgelist('socfb-Caltech36.mtx')

#print (rawData)


