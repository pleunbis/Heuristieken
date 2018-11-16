import json

with open('Data/amstel.json') as file:
    data = json.load(file)

house = data["houses"]

class House_Type():
    def __init__(self, width, depth, freespace, value, price_improvement):
        self.width = width
        self.depth = depth
        self.freespace = freespace
        self.value = value
        self.price_improvement = price_improvement

class Maison(House_Type):
    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, float(house["m"]["width"]), float(house["m"]["depth"]), float(house["m"]["freespace"]), float(house["m"]["value"]), float(house["m"]["price_improvement"]))
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace
        self.total_price = float(house["m"]["value"])
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_freespace) + ", " + str(self.total_price)
    def calculateprice(self):
        self.total_price = self.value * (1 + self.extra_freespace * self.price_improvement)
        return round(self.total_price, 2)

class Bungalow(House_Type):
    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, float(house["b"]["width"]), float(house["b"]["depth"]), float(house["b"]["freespace"]), float(house["b"]["value"]), float(house["b"]["price_improvement"]))
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace
        self.total_price = float(house["b"]["value"])
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_freespace) + ", " + str(self.total_price)
    def calculateprice(self):
        self.total_price = self.value * (1 + self.extra_freespace * self.price_improvement)
        return round(self.total_price, 2)

class Singlefamily(House_Type):
    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, float(house["sf"]["width"]), float(house["sf"]["depth"]), float(house["sf"]["freespace"]), float(house["sf"]["value"]), float(house["sf"]["price_improvement"]))
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace
        self.total_price = float(house["sf"]["value"])
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_freespace) + ", " + str(self.total_price)
    def calculateprice(self):
        self.total_price = self.value * (1 + self.extra_freespace * self.price_improvement)
        return round(self.total_price, 2)

class Water():
    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, 18, 20, 0, 0, 0)
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace
        self.total_price = 0
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_freespace) + ", " + str(self.total_price)
    def calculateprice(self):
        self.total_price = self.value * (1 + self.extra_freespace * self.price_improvement)
        return round(self.total_price, 2)        
