import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import colors
import matplotlib
import numpy as np

class Huissoort():
    def __init__(self, breedte, hoogte, vrijstand, waarde, prijsverbetering):
        self.breedte = breedte
        self.hoogte = hoogte
        self.vrijstand = vrijstand
        self.waarde = waarde
        self.prijsverbetering = prijsverbetering

class Maison(Huissoort):
    def __init__(self, id, x, y, extra_vrijstand):
        Huissoort.__init__(self, 11, 10.5, 6, 610000, 0.06)
        self.id = id
        self.x = x
        self.y = y
        self.extra_vrijstand = extra_vrijstand
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_vrijstand)

class Bungalow(Huissoort):
    def __init__(self, id, x, y, extra_vrijstand):
        Huissoort.__init__(self, 10, 7.5, 3, 399000, 0.04)
        self.id = id
        self.x = x
        self.y = y
        self.extra_vrijstand = extra_vrijstand
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_vrijstand)

class Eengezinswoning(Huissoort):
    def __init__(self, id, x, y, extra_vrijstand):
        Huissoort.__init__(self, 8, 8, 2, 285000, 0.03)
        self.id = id
        self.x = x
        self.y = y
        self.extra_vrijstand = extra_vrijstand
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_vrijstand)

fig = plt.figure()
ax = fig.add_subplot(111)

huisjes = []
x, y = 2, 2

for i in range(12):
    huisjes.append(Eengezinswoning(i, x, y, 0))
    rect1 = matplotlib.patches.Rectangle((x, y), 8, 8, color='yellow')
    ax.add_patch(rect1)
    if x <= 140:
        x = x + 10
    else:
        x = 2
        y = y + 10

x = x + 1
y = y + 1

for i in range(5):
    # if x == 2 and y == 2:
    #     x, y = 3, 3
    # elif y == 2:
    #     y = 3
    # elif x == 2:
    #     x = 3
    huisjes.append(Bungalow(i + 12, x, y, 0))
    rect2 = matplotlib.patches.Rectangle((x, y), 10, 7.5, color='red')
    ax.add_patch(rect2)
    if x <= 134:
        x = x + 13
    else:
        x = 3
        y = y + 10.5

x = x + 3
y = y + 3
for i in range(3):
    # if x == 3 and y == 3:
    #     x, y = 6, 6
    # elif x == 3:
    #     x == 6
    # elif y == 3:
    #     y = 6
    huisjes.append(Maison(i + 17, x, y, 0))
    rect3 = matplotlib.patches.Rectangle((x, y), 11, 10.5, color='blue')
    ax.add_patch(rect3)
    if x <= 126:
        x = x + 17
    else:
        x = 6
        y = y + 16.5

for huisje in huisjes:
    print(huisje)

# linker boven hoek vanuit het huisje
x, y = huisjes[0].x, huisjes[0].y + huisjes[0].hoogte

# linker onderhoek van het huisje die er boven staat
a = huisjes[14].x
b = huisjes[14].y

# breedte en hoogte van huisje erboven
breedte, hoogte = huisjes[14].breedte, huisjes[14].hoogte
min_vrijstand = 180.0

for x in range(huisjes[0].x * 2, (huisjes[0].x + huisjes[0].breedte) * 2):
    vrijstand = 0.0
    y = huisjes[0].y + huisjes[0].hoogte
    while True:
        if a <= float(x) / 2 < a + breedte and b <= y < b + hoogte:
            break
        elif y == 160.0:
            break
        elif x == 180.0:
            break
        else:
            vrijstand = vrijstand + 0.5
        y += 0.5
    if vrijstand < min_vrijstand:
        min_vrijstand = vrijstand

#     print(vrijstand)
#
# print(min_vrijstand)

# rechter boven hoek van het huisje zelf
x, y = huisjes[0].x + huisjes[0].breedte , huisjes[0].y + huisjes[0].hoogte

# linker boven hoek van het huisje ernaast
a = huisjes[1].x
b = huisjes[1].y + huisjes[1].hoogte

# breedte en hoogte van huisje ernaast
breedte, hoogte = huisjes[1].breedte, huisjes[1].hoogte

for y in range((huisjes[0].x + huisjes[0].breedte) * 2, huisjes[0].x * 2, -1):
    vrijstand = 0.0
    x = huisjes[0].x + huisjes[0].breedte
    while True:
        if b - hoogte < float(y) / 2 <= b and a <= x < a + breedte:
            break
        elif x >= 160.0:
            break
        elif y >= 180.0:
            break
        else:
            vrijstand = vrijstand + 0.5
        x += 0.5
    if vrijstand < min_vrijstand:
        min_vrijstand = vrijstand

#     print(vrijstand)
#
# print(min_vrijstand)


# rechter onderhoek van het huisje zelf
x, y = huisjes[0].x + huisjes[0].breedte, huisjes[0].y
# rechter bovenhoek van het huisje eronder
a = 10.0
b = 0.0
# breedte en hoogte van het huisje eronder
breedte, hoogte = 8.0, 0.0

for x in range(20, 4, -1):
    vrijstand = 0.0
    y = 2.0
    while True:
        if a - breedte < float(x) / 2 <= a and b <= x < b + hoogte:
            break
        elif x == 160.0 or x == 0:
            break
        elif y == 180.0 or y == 0:
            break
        else:
            vrijstand = vrijstand + 0.5
        y -= 0.5

    # als een huisje aan de zijkant staat
    # gebruik je afstand van dat huisje naar de kant niet
    # if vrijstand < min_vrijstand:
        # min_vrijstand = vrijstand

    print(vrijstand)

print(min_vrijstand)

# linker onderhoek van het huisje zelf
x, y = 2.0, 2.0
# linker bovenhoek van het huisje eronder
a = 0.0
b = 2.0
# breedte en hoogte van het huisje eronder
breedte, hoogte = 0.0, 8.0

for y in range(4, 20):
    vrijstand = 0.0
    x = 2.0
    while True:
        if b <= float(y) / 2 < b + hoogte and a <= x < a + breedte:
            break
        elif x == 160.0 or x == 0:
            break
        elif y == 180.0 or y == 0:
            break
        else:
            vrijstand = vrijstand + 0.5
        x -= 0.5
    if vrijstand < min_vrijstand:
        min_vrijstand = vrijstand
#     print(vrijstand)
#
# print(min_vrijstand)



# fig = plt.figure()
# ax = fig.add_subplot(111)
# rect1 = matplotlib.patches.Rectangle((0, 0), 3, 2, color='yellow')
# ax.add_patch(rect1)

plt.ylim(0, 180)
plt.xlim(0, 160)

major_xticks = np.arange(0, 160, 1)
# minor_xticks = np.arange(0, 160, 1)
major_yticks = np.arange(0, 180, 1)
# minor_yticks = np.arange(0, 180, 1)

plt.xticks(major_xticks)
# plt.xticks(minor_xticks, minor=True)
plt.yticks(major_yticks)
# plt.yticks(minor_yticks, minor=True)

plt.title("Plattegrond AmstelHaege")
plt.grid()
plt.show()
