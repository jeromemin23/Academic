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
        self.finArea = 0.092565
        self.numberOfFins = 51
        self.fanBaseArea = 0
        self.fanTotalArea = (self.numberOfFins * self.finArea) + self.fanBaseArea



    def calculateTverre(self,Tambiant, powerIn):
        speed = self.calculateWinfSpeed()
        Re = self.calculateReynolds(speed)
        print('Reynolds : {}'.format(Re))
        #UPDATE NUSSELT
        h = self.calculateHconv()
        m = self.calculateM(h)
        Nf = self.calculateNf(m)
        a = (1- ((self.numberOfFins * self.finArea)/self.fanTotalArea)*(1- Nf))
        Tverre = (powerIn/(h * self.finArea * (1- ((self.numberOfFins * self.finArea)/self.fanTotalArea)*(1- Nf))) ) + Tambiant
        print(Tverre)


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






a = Cooler()
a.calculateTverre(Tambiant=300, powerIn=10)
