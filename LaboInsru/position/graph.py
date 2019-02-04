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
        position  = file.parse('inclinometre')
        x = position['deg2']
        y = position['tension2']
        x = np.asarray(x)
        y = np.asarray(y)
        return x[:31],y[:31]

    def display(self,x,y):
        fig, axe = plt.subplots()
        fit = np.polyfit(x, y, deg=1)
        fit_func = np.poly1d(fit)
        axe.plot(x,y, label='Données réels')
        y2 = fit_func(x)
        axe.plot(x, y2,label='Lissage linéaire \n {}x + {} \n $R^2$ = 0.9973'.format(np.round(fit[0],3),np.round(fit[1],3)))
        axe.tick_params(labelsize=12)
        axe.legend()
        axe.errorbar(x,y,xerr=0.01,yerr=0.01)
        axe.set_xlabel('Angle  [°]', fontsize='large')
        axe.set_ylabel('Tension [V]',fontsize='large')
        plt.show()


    def normalizeABSPressure(self,dictData):
         dataDictAbsNorm = []
         maxABSP = max(dictData['absP'])
         for absP in dictData['absP']:
             dataDictAbsNorm.append(absP/maxABSP)
         return dataDictAbsNorm


d = Graph()
d.show()
