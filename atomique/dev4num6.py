import math as m
import sympy as sp
import numpy as np
from scipy import special as sc
import matplotlib.pyplot as plt

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

fig, axes = plt.subplots(3, 2, figsize=(12, 10))

for S in [0, 1]:

    mu = (1.672*10**(-27))/2
    mp = 938.27205 * 10**6 * 1.602176*10**(-19) / (3*10**8)**2
    hBar = 1.054571800 * 10**(-34)

    lambdaS = [2.80, 2.05][S] * 10**(-15)
    V0S = [11.8, 35.1][S] * 4
    omega = m.sqrt(mp * lambdaS**2 * V0S * 10**6 * 1.602176*10**(-19)/hBar**2)

    def LeftEQ(x):
        return np.sqrt(x / V0S)

    def L0RightEQ(x):
        result = -1*np.sqrt(1 - (x / V0S)) * (1/(np.tan(omega*np.sqrt(1 - (x / V0S)))))
        result[:-1][np.diff(result) < -1000] = np.nan  # remove vertical lines from tan(x)
        return result

    def L1RightEQ(x):
        term1 = 1/(np.tan(omega*np.sqrt(1 - (x / V0S))) * np.sqrt(1 - (x / V0S)))
        term2 = 1/(omega*(x / V0S) * (1 - (x / V0S)))
        result = (term1 - term2)**(-1)
        result[:-1][np.diff(result) < -1000] = np.nan
        return result

    def L2RightEQ(L, array):
        result = []

        for x in array:
            besselArgument1 = omega * np.sqrt(1 - (x / V0S))
            besselArgument2 = complex(0, omega * m.sqrt(x / V0S))
            # print (besselArgument2.real, besselArgument2.imag)
            term1 = - 1j * np.sqrt(1 - (x / V0S))
            # arg = sc.spherical_jn(2, besselArgument2)
            # arg2 = sc.spherical_yn(2, besselArgument2)
            term2 = sc.spherical_jn(L-1, besselArgument1)/ sc.spherical_jn(L, besselArgument1)
            term3 = (sc.spherical_jn(L, besselArgument2) + 1j * sc.spherical_yn(L, besselArgument2))
            term4 = (sc.spherical_jn(L-1, besselArgument2) + 1j * sc.spherical_yn(L-1, besselArgument2))
            result.append((term1 * term2 * (term3 / term4)).real)

        # result[:-1][np.diff(result) < -1000] = np.nan
        return result

    scanArray = np.arange(0, V0S, 0.0001)

    axes[0][S].plot(scanArray, LeftEQ(scanArray), linewidth=3)
    axes[0][S].plot(scanArray, L0RightEQ(scanArray), linewidth=3)
    axes[0][S].set_title("$L=0$, $S={}$".format(S), fontsize=18)
    axes[0][S].set_ylim(0, 1)

    axes[1][S].plot(scanArray, LeftEQ(scanArray), linewidth=3)
    axes[1][S].plot(scanArray, L1RightEQ(scanArray), linewidth=3)
    axes[1][S].set_title("$L=1$, $S={}$".format(S), fontsize=18)
    axes[1][S].set_ylim(0, 1)

    axes[2][S].plot(scanArray, LeftEQ(scanArray), linewidth=3)
    axes[2][S].plot(scanArray, L2RightEQ(2, scanArray), linewidth=3)
    axes[2][S].set_title("$L=2$, $S={}$".format(S), fontsize=18)
    axes[2][S].set_ylim(-8, 2)

plt.tight_layout()
# plt.savefig('sauce.png', dpi=600)
plt.show()
