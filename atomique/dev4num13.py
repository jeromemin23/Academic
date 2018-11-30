
nljNeutrons = []
nljProtons = []
for n in range(1, 3+1):
    for l in range(0, 8-2*n):
        for j in [l+0.5, l-0.5]:
            if j > 0:
                nljNeutrons.append([n, l, j])
                nljProtons.append([n, l, j])
    nljProtons.pop()
    nljProtons.pop()
nljNeutrons.append([1, 6, 6.5])
nljProtons.append([1, 5, 5.5])

s = 1/2
A = 208
V0 = 50
hw = 41*A**(-1/3)
D = 0.0225*hw
C = 0.1*hw


def energy(index):
    n, l, j = index
    return (-V0 + hw*(2*(n-1) + l + 3/2) - D*l*(l+1) - (C/2)*(j*(j+1) - l*(l+1) - s*(s+1))) * (2*j + 1)

energyNeutrons = [energy(index) for index in nljNeutrons]
energyProtons = [energy(index) for index in nljProtons]
totalEnergy = sum(energyNeutrons) + sum(energyProtons)

print("Énergie dernier proton {} MeV".format(round(energyProtons[-1]/12, 2)))
print("Énergie dernier neutron {} MeV".format(round(energyNeutrons[-1]/14, 2)))
print("\nTotal Energy = {} MeV".format(round(totalEnergy, 2)))

""" Valeur théorique: 1636 MeV """
