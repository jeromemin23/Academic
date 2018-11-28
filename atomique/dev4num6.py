import math as m
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# constants declaration
mu = (1.672*10**(-27))/2
lambdaS = 2.80 * 10**(-15)
V0S = 35.1
omega = m.sqrt(3.57)
hBar = 6.626 * 10**(-34)

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


def L1leftEQ(x):
    return np.sqrt(x / V0S)


def L1rightEQ(x):
    return -1*np.sqrt(1 - (x / V0S)) * (1/(np.tan(omega*np.sqrt(1 - (x / V0S)))))

scanArray = np.arange(-10, 50, 0.001)

plt.plot(scanArray, L1leftEQ(scanArray), label="leftEQ")
plt.plot(scanArray, L1rightEQ(scanArray), label="rightEQ")
plt.legend(loc="best")
plt.show()
