import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


class Graph:

    def __init__(self):
        self.sauce = 1

    def show(self):
        filename = 'data.txt'
        dataDict = self.importData(filename)
        self.display(dataDict)

    def importData(self, filename):
        x, y = np.loadtxt('{}'.format(filename),unpack=True,skiprows=1,delimiter=',')
        dataDict = {'x':x,'y':y}
        return dataDict

    def display(self,dataDict):
        plt.plot(dataDict['x'], dataDict['y'])
        plt.show()


    def normalizeABSPressure(self,dictData):
         dataDictAbsNorm = []
         maxABSP = max(dictData['absP'])
         for absP in dictData['absP']:
             dataDictAbsNorm.append(absP/maxABSP)
         return dataDictAbsNorm


d = Graph()
d.show()
