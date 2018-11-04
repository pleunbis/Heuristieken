class Huissoort():
    def __init__(self, breedte, diepte, vrijstand, waarde, prijsverbetering):
        self.breedte = breedte
        self.diepte = diepte
        self.vrijstand = vrijstand
        self.waarde = waarde
        self.prijsverbetering = prijsverbetering

class Maison(Huissoort):
    def __init__(self, id, x, y, extra_vrijstand):
        Huissoort.__init__(self, 10, 11.5, 6, 610000, 0.06)
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

huisjes = []
x, y = 2, 2

for i in range(12):
    huisjes.append(Eengezinswoning(i, x, y, 0))
    if x < 138:
        x = x + 10
    else:
        x = 2
        y = y + 10

for i in range(5):
    if x == 2 and y == 2:
        x, y = 3, 3
    elif y == 2:
        y = 3
    elif x == 2:
        x = 3
    huisjes.append(Bungalow(i + 12, x, y, 0))
    if x < 134:
        x = x + 13
    else:
        x = 3
        y = y + 10.5

for i in range(3):
    if x == 3 and y == 3:
        x, y = 6, 6
    elif x == 3:
        x == 6
    elif y == 3:
        y = 6
    huisjes.append(Maison(i + 17, x, y, 0))
    if x < 128:
        x = x + 16
    else:
        x = 6
        y = y + 17.5

for huisje in huisjes:
    print(huisje)
