import math as m
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# constants declaration

"""
xSym = sp.Symbol('x')

# equations declaration
eqnL0g = sp.sqrt(xSym / V0S)
eqnL0d = -1*sp.sqrt(1 - (xSym / V0S)) * (1/(sp.tan(omega*sp.sqrt(1 - (xSym / V0S)))))
eqn = sp.Eq(eqnL0g, eqnL0d)

#solving

print(sp.solve(eqn,minimal=True,warn=True))
"""


" SECTION VISUEL LOL xD"

fig, axes = plt.subplots(2, 2)

for S in [0, 1]:

    mu = (1.672*10**(-27))/2
    mp = 938.27205 * 10**6 * 1.602176*10**(-19) / (3*10**8)**2
    hBar = 1.054571800 * 10**(-34)

    lambdaS = [2.80, 2.05][S] * 10**(-15)
    V0S = [11.8, 35.1][S] * 4
    omega = m.sqrt(mp * lambdaS**2 * V0S * 10**6 * 1.602176*10**(-19)/hBar**2)

    def L0LeftEQ(x):
        return np.sqrt(x / V0S)

    def L0RightEQ(x):
        return -1*np.sqrt(1 - (x / V0S)) * (1/(np.tan(omega*np.sqrt(1 - (x / V0S)))))

    # def L1LeftEQ(x):
    #     return np.sqrt(x / V0S)
    #
    # def L1RightEQ(x):
    #     return -1*np.sqrt(1 - (x / V0S)) * (1/(np.tan(omega*np.sqrt(1 - (x / V0S)))))

    scanArray = np.arange(0, 50, 0.001)

    axes[0][S].plot(scanArray, L0LeftEQ(scanArray), label="leftEQ")
    axes[0][S].plot(scanArray, L0RightEQ(scanArray), label="rightEQ")


plt.legend(loc="best")
plt.show()

""" x = energy in MeV """
