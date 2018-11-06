import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import colors
import matplotlib
import numpy as np
import random

class House_Type():
    def __init__(self, width, depth, freespace, value, price_improvement):
        self.width = width
        self.depth = depth
        self.freespace = freespace
        self.value = value
        self.price_improvement = price_improvement

class Maison(House_Type):
    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, 11, 10.5, 6, 610000, 0.06)
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_freespace)

class Bungalow(House_Type):
    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, 10, 7.5, 3, 399000, 0.04)
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_freespace)

class Singlefamily(House_Type):
    def __init__(self, id, x, y, extra_freespace):
        House_Type.__init__(self, 8, 8, 2, 285000, 0.03)
        self.id = id
        self.x = x
        self.y = y
        self.extra_freespace = extra_freespace
    def __str__(self):
        return str(self.id) + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.extra_freespace)

fig = plt.figure()
ax = fig.add_subplot(111)

houses = []

# Singlefamily houses
for i in range(12):

    # create random x and y
    x = random.randrange(0, 180, 1)
    y = random.randrange(0, 160, 1)

    # append to houses
    houses.append(Singlefamily(i, x, y, 0))

    # create rectange
    rect1 = matplotlib.patches.Rectangle((x, y), 8, 8, color='yellow')
    ax.add_patch(rect1)


# Bungalows houses
for i in range(5):

    # create random x and y
    x = random.randrange(0, 180, 1)
    y = random.randrange(0, 160, 1)

    # append to houses
    houses.append(Bungalow(i + 12, x, y, 0))

    # create rectange
    rect2 = matplotlib.patches.Rectangle((x, y), 10, 7.5, color='red')
    ax.add_patch(rect2)

# Maisons
for i in range(3):

    # create random x and y
    x = random.randrange(0, 160, 1)
    y = random.randrange(0, 180, 1)

    # append to houses
    houses.append(Maison(i + 17, x, y, 0))

    # create rectange
    rect3 = matplotlib.patches.Rectangle((x, y), 11, 10.5, color='blue')
    ax.add_patch(rect3)
# break

plt.ylim(0, 180)
plt.xlim(0, 160)

major_xticks = np.arange(0, 160, 1)

major_yticks = np.arange(0, 180, 1)


plt.xticks(major_xticks)
plt.yticks(major_yticks)

#
plt.title("Map AmstelHaege")
plt.grid()
plt.show()

for current_house in houses:
    min_freespace = 180.0
    for house in houses:
        if house == current_house:
            # print(house)
            continue

        # upper left corner of house itself
        x, y = current_house.x, current_house.y + current_house.depth

        # lower left corner of house above this house
        a = house.x
        b = house.y

        # width and depth of house above this house
        width, depth = house.width, house.depth

        for x in range(int(current_house.x * 2), int((current_house.x + current_house.width) * 2 + 1)):
            freespace = 0.0
            y = current_house.y + current_house.depth
            while True:
                if a <= float(x) / 2 <= a + width and b <= y <= b + depth:
                    break
                elif y >= 180.0 or y <= 0:
                    if freespace > current_house.freespace:
                        freespace = 180
                    break
                else:
                    freespace = freespace + 0.5
                y += 0.5
            if freespace < min_freespace:
                min_freespace = freespace

        # print(house)
        # print(min_freespace)

        # upper right corner of house itself
        x, y = current_house.x + current_house.width , current_house.y + current_house.depth

        # upper left corner of house next to this house (right)
        a = house.x
        b = house.y + house.depth

        # width and depth of house next to this house (right)
        width, depth = house.width, house.depth

        for y in range(int((current_house.y + current_house.depth) * 2), int(current_house.y * 2 - 1), -1):
            freespace = 0.0
            x = current_house.x + current_house.width
            while True:
                if b - depth <= float(y) / 2 <= b and a <= x <= a + width:
                    break
                elif x >= 160.0 or x <= 0:
                    if freespace > current_house.freespace:
                        freespace = 180
                    break
                else:
                    freespace = freespace + 0.5
                x += 0.5
            if freespace < min_freespace:
                min_freespace = freespace

        # print(min_freespace)

        # lower right corner of house itself
        x, y = current_house.x + current_house.width, current_house.y

        # upper right corner of house underneath this house
        a = house.x + house.width
        b = house.y + house.depth

        # width and depth of house underneath this house
        width, depth = house.width, house.depth

        for x in range(int((current_house.x + current_house.width) * 2), int(current_house.x * 2 - 1), -1):
            freespace = 0.0
            y = current_house.y
            while True:
                if a - width <= float(x) / 2 <= a and b - depth <= y <= b:
                    break
                elif y >= 180.0 or y <= 0:
                    if freespace > current_house.freespace:
                        freespace = 180
                    break
                else:
                    freespace = freespace + 0.5
                y -= 0.5

            if freespace < min_freespace:
                min_freespace = freespace

            # print(freespace)

        # print(min_freespace)

        # lower left corner of house itself
        x, y = current_house.x, current_house.y

        # lower right corner of house next to this house (left)
        a = house.x + house.width
        b = house.y

        # width and depth of house next to this house (left)
        width, depth = house.width, house.depth

        for y in range(int(current_house.y * 2), int((current_house.y + current_house.depth) * 2 + 1)):
            freespace = 0.0
            x = current_house.x
            while True:
                if b <= float(y) / 2 <= b + depth and a - width <= x <= a:
                    break
                elif x >= 160.0 or x <= 0:
                    if freespace > current_house.freespace:
                        freespace = 180
                    break
                else:
                    freespace = freespace + 0.5
                x -= 0.5
            if freespace < min_freespace:
                min_freespace = freespace

        # print(min_freespace)

    min_freespace -= current_house.freespace
    current_house.extra_freespace = min_freespace
    print(current_house)
