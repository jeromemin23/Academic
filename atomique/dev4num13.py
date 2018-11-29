
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
# print("Neutrons: ", nljNeutrons)
# print("Protons : ", nljProtons)

A = 208
V0 = 40
hw = 54*A**(-1/3)
D = 0.0225*hw
C = 0.1*hw
s = 1/2


def energy(index):
    n, l, j = index
    return (-V0 + hw*(2*(n-1) + l + 3/2) - D*l*(l+1) - (C/2)*(j*(j+1) - l*(l+1) - s*(s+1))) * (2*j + 1)

energyNeutrons = [energy(index) for index in nljNeutrons]
energyProtons = [energy(index) for index in nljProtons]

totalEnergy = sum(energyNeutrons) + sum(energyProtons)

print(sum(energyNeutrons), sum(energyProtons))
print("\nTotal Energy = {} MeV".format(round(totalEnergy, 2)))

""" Valeur théorique: 1636 MeV """
