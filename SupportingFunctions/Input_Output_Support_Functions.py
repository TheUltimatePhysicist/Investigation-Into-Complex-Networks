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


def CleanRepeatedValuesOfNetworkRepData(inputArray1, inputArray2):

        # Indices (12, 13) and (23,24) are identical in N.
        outputArray1 = np.zeros(len(inputArray1) - 2)
        outputArray2 = np.zeros(len(inputArray2) - 2)

        for i in range(0, 12):
                outputArray1[i] = inputArray1[i]
                outputArray2[i] = inputArray2[i]
        
        outputArray1[12] = (inputArray1[12] + inputArray1[13]) / 2
        outputArray2[12] = (inputArray2[12] + inputArray2[13]) / 2

        for i in range(13, 22):
                outputArray1[i] = inputArray1[i + 1]
                outputArray2[i] = inputArray2[i + 1]

        outputArray1[22] = (inputArray1[23] + inputArray1[24]) / 2
        outputArray2[22] = (inputArray2[23] + inputArray2[24]) / 2

        return outputArray1, outputArray2


def CleanArraysOfZeroValues(inputArray1, inputArray2):
        
        #
        outputArray1 = []
        outputArray2 = []

        #
        for i in range(len(inputArray1)):

                if ((inputArray1[i] != 0) and (inputArray2[i] != 0)):

                        outputArray1.append(inputArray1[i])
                        outputArray2.append(inputArray2[i])
        
        outputArray1 = np.array(outputArray1)
        outputArray2 = np.array(outputArray2)
        
        return outputArray1, outputArray2



