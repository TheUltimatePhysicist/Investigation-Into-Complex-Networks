import numpy as np


#--------------------------------------------------------------------------------------------------
# FUNCTIONS
#--------------------------------------------------------------------------------------------------

def WritePlottingDataToTxtFile(fileName, xlabel, xArray, ylabel, yArray):

        outputFile = open(fileName, 'w')

        # Write to the file.
        for i in range(0, xArray.shape[0]):
                outputFile.write(str(xArray[i]) + ",   " + str(yArray[i]) + "\n")
        
        outputFile.close()


def ReadPlottingDataFromTxtFile(fileName):

        arrayLoaded = np.loadtxt(fileName, delimiter = ', ')

        array1 = np.zeros(len(arrayLoaded))
        array2 = np.zeros(len(arrayLoaded))

        for i in range (len(arrayLoaded)):
                array1[i] = arrayLoaded[i][0]
                array2[i] = arrayLoaded[i][1]

        return array1, array2


