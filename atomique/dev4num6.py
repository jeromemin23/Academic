import math as m
import sympy as sp

# constants declaration
mu = (1.672*10**(-27))/2
lambdaS = 2.80 * 10**(-15)
V0S = 35.1
omega = m.sqrt(3.57)
hBar = 6.626 * 10**(-34)
x = sp.Symbol('x')

# equations declaration
eqnL0g = sp.sqrt(x / V0S)
eqnL0d = -1*sp.sqrt(1 - (x / V0S)) * (1/(sp.tan(omega*sp.sqrt(1 - (x / V0S)))))
eqn = sp.Eq(eqnL0g,eqnL0d)

#solving

print(sp.solve(eqn,minimal=True,warn=True))
