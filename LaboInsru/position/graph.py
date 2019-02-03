import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


class Graph:

    def __init__(self):
        self.sauce = 1

    def show(self):
        filename = 'data.xlsx'
        x ,y = self.importXLSData(filename)
        self.display(x,y)

    def importTXTData(self, filename):
        x, y = np.loadtxt('{}'.format(filename),unpack=True,skiprows=1,delimiter=',')
        dataDict = {'x':x,'y':y}
        return dataDict

    def importXLSData(self, filename):
        file = pd.ExcelFile(filename)
        position  = file.parse('position')
        x = position['positionV']
        y = position['tensionV']
        x = np.asarray(x)
        y = np.asarray(y)
        return x[:45],y[:45]

    def display(self,x,y):
        fig, axe = plt.subplots()
        axe.plot(x, y)
        axe.errorbar(x,y,xerr=0.1,yerr=0.01)
        axe.set_xlabel('Déplacement  [mm]')
        axe.set_ylabel('Tension [V]')
        plt.show()


    def normalizeABSPressure(self,dictData):
         dataDictAbsNorm = []
         maxABSP = max(dictData['absP'])
         for absP in dictData['absP']:
             dataDictAbsNorm.append(absP/maxABSP)
         return dataDictAbsNorm


d = Graph()
d.show()
