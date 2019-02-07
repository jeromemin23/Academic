import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


class Graph:

    def __init__(self):
        self.sauce = 1

    def show(self):
        filename = 'dataA.xlsx'
        x ,y,x1,y1 = self.importXLSData(filename)
        self.display(x,y,x1,y1)

    def importTXTData(self, filename):
        x, y = np.loadtxt('{}'.format(filename),unpack=True,skiprows=1,delimiter=',')
        dataDict = {'x':x,'y':y}
        return dataDict

    def importXLSData(self, filename):
        file = pd.ExcelFile(filename)
        position = file.parse('position')
        xD = position['position']
        yD = position['tension']
        xD = np.asarray(xD)
        yD = np.asarray(yD)

        # xG = position['degG']
        # yG = position['tensionG']
        # xG = np.asarray(xG)
        # yG = np.asarray(yG)
        return xD[5:20],yD[5:20],xD[20:33],yD[20:33]

    def display(self,xD,yD,xG,yG):
        fig, axe = plt.subplots()

        fit = np.polyfit(xD, yD, deg=1)
        fit_func = np.poly1d(fit)
        axe.errorbar(xD,yD,xerr=0.5,yerr=0.03,fmt="+",label='Données réels')
        y2D = fit_func(xD)
        axe.plot(xD, y2D,label='Lissage linéaire droite\n {}x + {} \n $R^2$ = 0.9934'.format(np.round(fit[0],3),np.round(fit[1],3)))

        fit = np.polyfit(xG, yG, deg=1)
        fit_func = np.poly1d(fit)
        axe.errorbar(xG,yG,xerr=0.5,yerr=0.03,fmt="+",label='Données réels')
        y2G = fit_func(xG)
        axe.plot(xG, y2G,label='Lissage linéaire gauche\n {}x + {} \n $R^2$ = 0.9967'.format(np.round(fit[0],3),np.round(fit[1],3)))

        axe.tick_params(labelsize=12)
        axe.set_title('''Tension de sortie $V_2-V_3$ en fonction du déplacement linéaire''')
        axe.legend()
        axe.set_xlabel('Déplacement  [mm]', fontsize='large')
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
