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



# for i in range(x, houses[-1].x + houses[-1].width):
#     for j in range(y, houses[-1].y + houses[-1].depth):
#         for house in houses[:-1]:
#             if house.x == x:
#                 exist == True
#                 print("overlapping")
#
#             elif house.y == y:
#                 exist == True
#                 print("overlapping")

# for house in houses[:-1]:
#     # print(house.id)
#     for i in range(x, houses[-1].x + houses[-1].width):
#         for j in range(y, houses[-1].y + houses[-1].depth):
#             if house.x == i and house.y == j:
#                 print(" ")

# for house in houses:
#     for h in houses[:house]:
#         for i in range(int(house.x) , int(house.x) + int(house.width):
#             for j in range(int(house.y), int(house.y) + int(house.depth)):
#                 for k in range(int(h.x) , int(h.x) + int(h.width)):
#                     for l in range(int(h.y), int(h.y) + int(h.depth)):
#                         if (int(i) == int(k) and int(j) == int(l)):
#                             print("ojeej overlap")
