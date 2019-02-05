import numpy as np
import math


class Cooler:

    def __init__(self):
        self.finHeight = 0.02
        self.fanRPM = 2000
        self.fanLc = self.finHeight
        self.airViscosity = 15.89 * 10**(-6)
        self.Nusselt = 4.36
        self.conductivityAir = 0.0306
        self.finLenght = 0.0954
        self.finPerimeter = 0.076
        self.finConductivity = 250
        self.finCrossArea = 0.00024
        self.finTotalArea = 0.092565
        self.numberOfFins = 51
        self.singleFinArea = self.finTotalArea/self.numberOfFins
        self.fanBaseArea = 0.005
        self.fanTotalArea =  self.finTotalArea + self.fanBaseArea
        self.N0securityFactor = 0.5



    def calculateRtot(self):
        speed = self.calculateWinfSpeed()
        Re = self.calculateReynolds(speed)
        print('Reynolds : {}'.format(Re))
        #UPDATE NUSSELT
        h = self.calculateHconv()
        m = self.calculateM(h)
        Nf = self.calculateNf(m)
        N0 = 1- (((self.singleFinArea * self.numberOfFins)/self.fanTotalArea))*(1- Nf)
        Rtot = 1/(self.N0securityFactor * N0 * h * self.fanTotalArea)
        print(Rtot)
        return Rtot


    def calculateWinfSpeed(self):
        speed = self.finHeight/(1/(self.fanRPM/60))
        return speed

    def calculateReynolds(self,speed):
        Re = (speed * self.fanLc)/ self.airViscosity
        return Re

    def calculateHconv(self):
        h = (self.Nusselt * self.conductivityAir)/self.finLenght
        return h

    def calculateM(self,h):
        m = math.sqrt((h * self.finPerimeter)/(self.finConductivity * self.finCrossArea))
        return m

    def calculateNf(self,m):
        Nf = math.tanh(m * self.fanLc)/ (m * self.fanLc)
        return Nf


class Conduction:

    def __init__(self):
        self.beamDiameter = 0.001
        self.glassDiameter = 0.01
        self.glassDepth = 0.01
        self.shellConductivity = 250
        self.glassConducticity = 1.38
        self.shellDiameter = 0.011


    def calculateResis(self):
        rGlass = self.calculateGlassResis()
        rShell = self.calculateShellResis()
        return rGlass, rShell

    def calculateGlassResis(self):
        R = (math.log((self.glassDiameter/self.beamDiameter)))/(2* math.pi * self.glassConducticity)
        return R

    def calculateShellResis(self):
        R = (math.log((self.shellDiameter/self.glassDiameter)))/(2* math.pi * self.shellConductivity)
        return R





a = Cooler()
b = Conduction()
rSys = a.calculateRtot()
rGlass, rShell = b.calculateResis()

def calculateMaxGlassTemp(Tambiant = 20, powerIn = 10):
    Tverre = (powerIn * (rSys + rShell + rGlass)) - Tambiant
    print('Max glass temperature : {}'.format(Tverre))

calculateMaxGlassTemp()
