import json

with open('Data/amstel.json') as file:
    data = json.load(file)

house = data["houses"]


class House_Type():
    """Class for house type"""

    def __init__(self, width, depth, freespace, value, price_improvement):
        self.width = width
        self.depth = depth
        self.freespace = freespace
        self.value = value
        self.price_improvement = price_improvement


class Maison(House_Type):
    """Class for maisons"""

    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, house["m"]["width"], house["m"]["depth"],
                            house["m"]["freespace"], house["m"]["value"],
                            house["m"]["price_improvement"])
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace

    def __str__(self):
        return (str(self.id) + ", " + str(self.x) + ", "
        + str(self.y) + ", " + str(self.extra_freespace) + ", "
        + str(self.total_price))

    def calculateprice(self):
        self.total_price = self.value * (1 + self.extra_freespace *
                                         self.price_improvement)
        return round(self.total_price, 2)


class Bungalow(House_Type):
    """Class for bungalow houses"""

    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, house["b"]["width"],
                            house["b"]["depth"], house["b"]["freespace"],
                            house["b"]["value"],
                            house["b"]["price_improvement"])
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace

    def __str__(self):
        return (str(self.id) + ", " + str(self.x) + ", "
        + str(self.y) + ", " + str(self.extra_freespace)
        + ", " + str(self.total_price))

    def calculateprice(self):
        self.total_price = self.value * (1 + self.extra_freespace *
                                         self.price_improvement)
        return round(self.total_price, 2)


class Singlefamily(House_Type):
    """Class for singlefamily houses"""

    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, house["sf"]["width"], house["sf"]["depth"],
                            house["sf"]["freespace"], house["sf"]["value"],
                            house["sf"]["price_improvement"])
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace

    def __str__(self):
        return (str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", "
        + str(self.extra_freespace) + ", " + str(self.total_price))

    def calculateprice(self):
        self.total_price = self.value * (1 + self.extra_freespace *
                                         self.price_improvement)
        return round(self.total_price, 2)


class Water():
    """Class for water"""

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return (str(self.x) + ", " + str(self.y) + ", " + str(self.width)
        + ", " + str(self.height))
