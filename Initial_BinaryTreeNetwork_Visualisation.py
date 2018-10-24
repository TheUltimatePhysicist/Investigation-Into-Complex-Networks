# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:03:36 2018

@author: aqilr
"""

import numpy as np
import matplotlib.pyplot as plt


# Create a graph.

yLimit = 2

plt.figure()
plt.ylim(0, yLimit)
plt.title('Simple Binary Tree Network Visualisation')


# Function to generate binary nodes.

def binaryNode(xVal, yVal):
    
    xVal1 = xVal + 1
    xVal2 = xVal + 1
    
    deltaY = yLimit - yVal
    if (deltaY < yVal):
        deltaY = deltaY / 2
    else:
        deltaY = yVal / 2
        
    yVal1 = yVal + deltaY
    yVal2 = yVal - deltaY
    return (xVal1, yVal1, xVal2, yVal2)
    

# Plot the nodes.

initialNodeX = 0
initialNodeY = yLimit / 2

while 1 == 1:
    xVal1, yVal1, xVal2, yVal2 = binaryNode(initialNodeX, initialNodeY)
    
    plt.scatter(xVal1, yVal1)
    plt.scatter(xVal2, yVal2)
    
    initialNodeX = xVal1
    
    plt.show()
    plt.pause(1)
    
    

