# Capteur de position linéaire				1 février	

coéquipière: Sarah Paradis

----

## Préparation

### Théorie

 Deux types de capteurs linéaires : le potentiomètre linéaire et le transformateur différentiel variable

#### Potentiomètre linéaire

![](potLinéaire.jpg)

Comme un potentiomètre standard, mais son élément résistif est une tige mobile.

Afin de ne pas tenir compte des résistance dse connexions, une source est utilisé.

![](montagePot.jpg)

Il est possible d'utilisé la formule suivante pour étalonner le système :

$$ \frac{Vsortie}{Vsource} = \frac{Rx}{Rtotal}$$

Ce genre de cappteur est utilisé dans les situations ou la friction interne n'est pas nuisible.

#### Transformateur linéaire différentiel varaible (LVDT)

![](LVDT.jpg)

Lorsque le noyau est centré, V2=V3 car le couplage magnétique est le même. DAns un déplacement vers la doite, V3 augmente et V2 diminue. Pour faciliter la tache on raccorde V2 et V3 et ont mesure donc V3-V2.



-  si le noyau es déplacer d'un bord ou de l'autre, la polarité du signal va changer.
- La source doit avoir une impédance très faible pour minimiser ls varisations de courant dans la boucle primaire (on veut que la tension qui varient est seulement du au déplacement du noyau)

**Avantage: ** son noyau peut etre déplacé sans aucune friction

Afin que la tension résiduelle ne brouille pas les donnnées, il st possibl de :

- On la nélige si on n'a pas besoin d'une grandre précision
- Traité le signal élctroniquement
- Si le déplacement est bien défini, on peut régler le séro de l'appareil dans une zone linéaire

## But

Se familiariser avec le transformateur. Étudier la source d’excitation et la tension résiduelle, faire létalonnage du capteur de position linéaire et, finalement, l’utiliser pour faire une mesure d’inclinaison.



## Plan de conception

#### Mesurer l'impédance de la source d'excitation

- avec un ohmetre??
- Pour s'assurer qu sa n'influ le voltage envoyé aux bobines

#### Trouver la zone non-linéaire correspondant à la tension résiduelle

- déplacer le noyau et trouver l'endroit ou le signal est le plus bas
- S'assurer qu'il y a non-linéarité dans les mesures autour du point zéro

#### Étalonner le capteur dans une zone linéaire

- Définir un voltage (à peu pres au milieu du déplacment) qui sera le nouveau zéro.

#### Mesurer la l'inclinaison

- no fucking clue



## Manipulations

#### Mesruer l'impédance de la source alternative et la fréquence de la source :

- On pose une tension de 1.5 V et on change la valeur de déphasage entre la source et le signaltotal out. On essai de minimiser le déphasage. fréquence = 2.75kHz
- mesurer l'impédance  de la source avec un ohmètre  =  83.5 ohm +/- 0.2   (à 1.46 V  () et )

#### Trouver la zone non-linéaire (même chose pour les 2 appareils)

- Varier la position et trouver les noter les valeurs de potentiel pour reteouver la constante $$Vsignsl = C deltax$$

  > On observe que la zone de non linéarité est tres grande. environ la moitié de la règle



### Position

#### Position de la règle et tension mesuré de la sortie

| position +/- 0.1 (mm) | Tension (V) +/- 0.01 |
| --------------------- | -------------------- |
| 0                     | 0.531                |
| 5                     | 0.602                |
| 10                    | 0.683                |
| 15                    | 0.75                 |
| 20                    | 0.772                |
| 25                    | 0.76                 |
| 30                    | 0.76                 |
| 35                    | 0.775                |
| 40                    | 0.793                |
| 45                    | 0.8                  |
| 50                    | 0.78                 |
| 55                    | 0.763                |
| 60                    | 0.76                 |
| 65                    | 0.77                 |
| 70                    | 0.768                |
| 75                    | 0.715                |
| 80                    | 0.626                |
| 85                    | 0.551                |
| 90                    | 0.507                |
| 95                    | 0.48                 |
| 100                   | 0.47                 |

![](marchepo.png)

On observe pas la parabole sourire voulu, de plus la valeur du minimum n'est pas damms le bonne ordre de grandeur. Cela devrit etre d'environ 0.1V.

**Le branchements n'ont ps été effectuer correctement**

On peut maintenant trouvé la tension résiduelle seulement à l'oeil

| Position  +/- 0.1 (mm) | Tension(V) |
| ---------------------- | ---------- |
| 24                     | 1.44       |
| 25                     | 1.4        |
| 26                     | 1.36       |
| 27                     | 1.32       |
| 28                     | 1.28       |
| 29                     | 1.24       |
| 30                     | 1.2        |
| 31                     | 1.12       |
| 32                     | 1.04       |
| 33                     | 1          |
| 34                     | 0.92       |
| 35                     | 0.84       |
| 36                     | 0.76       |
| 37                     | 0.65       |
| 38                     | 0.6        |
| 39                     | 0.44       |
| 40                     | 0.4        |
| 41                     | 0.32       |
| 42                     | 0.24       |
| 43                     | 0.16       |
| 44                     | 0.24       |
| 45                     | 0.3        |
| 46                     | 0.4        |
| 47                     | 0.48       |
| 48                     | 0.56       |
| 49                     | 0.64       |
| 50                     | 0.76       |
| 51                     | 0.84       |
| 52                     | 0.88       |
| 53                     | 0.96       |
| 54                     | 1.04       |
| 55                     | 1.08       |
| 56                     | 1.16       |
| 57                     | 1.22       |
| 58                     | 1.28       |
| 59                     | 1.32       |
| 60                     | 1.32       |
| 61                     | 1.4        |
| 62                     | 1.36       |
| 63                     | 1.44       |
| 64                     | 1.48       |
| 65                     | 1.48       |
| 66                     | 1.52       |
| 67                     | 1.48       |

![](Vposition.png)

- Isoler seulement une zone linéaire
- isoler la variable C

![](droitePosition.png)

### inclinometre

Il y a 15 ml d'huile dans le bécher

Les tensions RMS et la fréquences sont lesl mêmes que pour le capteur de position.

#### étalonnage pour trouver la zone non linéaire

![](Untitled.png)

L = 480 +/- 5 mm 

| Position +/- 0.01mm | Tension (V) |
| ------------------- | ----------- |
| 1                   | 0.2         |
| 2                   | 0.24        |
| 3                   | 0.26        |
| 4                   | 0.28        |
| 5                   | 0.3         |
| 6                   | 0.32        |
| 7                   | 0.34        |
| 8                   | 0.34        |
| 9                   | 0.4         |
| 10                  | 0.44        |
| 11                  | 0.48        |
| 12                  | 0.5         |
| 13                  | 0.56        |
| 14                  | 0.64        |
| 15                  | 0.64        |
| 16                  | 0.64        |
| 17                  | 0.72        |
| 18                  | 0.74        |
| 19                  | 0.76        |
| 20                  | 0.8         |
| 21                  | 0.8         |
| 22                  | 0.88        |
| 23                  | 0.9         |
| 24                  | 0.92        |
| 25                  | 0.98        |
| 26                  | 1           |
| 27                  | 1.08        |
| 28                  | 1.1         |
| 29                  | 1.12        |
| 30                  | 1.2         |

![](droiteInclinometre.png)

| Position +/- 0.01mm | Tension (V) |
| ------------------- | ----------- |
| 0                   | 0.160       |
| -1                  | 0.24        |
| -2                  | 0.24        |
| -3                  | 0.3         |
| -4                  | 0.32        |
| -5                  | 0.36        |
| -6                  | 0.4         |
| -7                  | 0.42        |
| -8                  | 0.44        |
| -9                  | 0.48        |
| -10                 | 0.5         |
| -11                 | 0.56        |
| -12                 | 0.58        |
| -13                 | 0.6         |
| -14                 | 0.62        |
| -15                 | 0.68        |
| -16                 | 0.68        |
| -17                 | 0.74        |
| -18                 | 0.76        |
| -19                 | 0.8         |
| -20                 | 0.88        |
| -21                 | 0.88        |
| -22                 | 0.9         |
| -23                 | 0.96        |
| -24                 | 0.96        |
| -25                 | 1           |
| -26                 | 1.04        |
| -27                 | 1.08        |
| -28                 | 1.12        |
| -29                 | 1.16        |
| -30                 | 1.18        |



![](gaucheInclinometre.png)