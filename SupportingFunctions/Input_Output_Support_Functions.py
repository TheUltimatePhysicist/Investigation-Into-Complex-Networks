import numpy as np


#--------------------------------------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------------------------------------

def WritePlottingDataToTxtFile(fileObject, xlabel, xArray, ylabel, yArray):

    # Write to the file.
    for i in range(0, xArray.shape[0]):
        fileObject.write(str(xArray[i]) + ",   " + str(yArray[i]) + "\n")
    

