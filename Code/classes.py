import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import colors
import matplotlib
import numpy as np

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
x, y = 2, 2

for i in range(12):
    houses.append(Singlefamily(i, x, y, 0))
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
    houses.append(Bungalow(i + 12, x, y, 0))
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
    houses.append(Maison(i + 17, x, y, 0))
    rect3 = matplotlib.patches.Rectangle((x, y), 11, 10.5, color='blue')
    ax.add_patch(rect3)
    if x <= 126:
        x = x + 17
    else:
        x = 6
        y = y + 16.5

for house in houses:
    print(house)

# upper left corner of house itself
x, y = houses[0].x, houses[0].y + houses[0].depth

# lower left corner of house above this house
a = houses[14].x
b = houses[14].y

# width and depth of house above this house
width, depth = houses[14].width, houses[14].depth
min_freespace = 180.0

for x in range(houses[0].x * 2, (houses[0].x + houses[0].width) * 2):
    freespace = 0.0
    y = houses[0].y + houses[0].depth
    while True:
        if a <= float(x) / 2 < a + width and b <= y < b + depth:
            break
        elif y == 160.0:
            break
        elif x == 180.0:
            break
        else:
            freespace = freespace + 0.5
        y += 0.5
    if freespace < min_freespace:
        min_freespace = freespace

#     print(freespace)
#
print(min_freespace)

# upper right corner of house itself
x, y = houses[0].x + houses[0].width , houses[0].y + houses[0].depth

# upper left corner of house next to this house (right)
a = houses[1].x
b = houses[1].y + houses[1].depth

# width and depth of house next to this house (right)
width, depth = houses[1].width, houses[1].depth

for y in range((houses[0].x + houses[0].width) * 2, houses[0].x * 2, -1):
    freespace = 0.0
    x = houses[0].x + houses[0].width
    while True:
        if b - depth < float(y) / 2 <= b and a <= x < a + width:
            break
        elif x >= 160.0:
            break
        elif y >= 180.0:
            break
        else:
            freespace = freespace + 0.5
        x += 0.5
    if freespace < min_freespace:
        min_freespace = freespace

#     print(freespace)
#
print(min_freespace)


# lower right corner of house itself
x, y = houses[0].x + houses[0].width, houses[0].y
# upper right corner of house underneath this house
a = 10.0
b = 0.0
# width and depth of house underneath this house
width, depth = 8.0, 0.0

for x in range(20, 4, -1):
    freespace = 0.0
    y = 2.0
    while True:
        if a - width < float(x) / 2 <= a and b <= x < b + depth:
            break
        elif x == 160.0 or x == 0:
            break
        elif y == 180.0 or y == 0:
            break
        else:
            freespace = freespace + 0.5
        y -= 0.5

    # if a house is at the end of the grid, this distance is not used
    # to calculate the extra freespace
    # if freespace < min_freespace:
        # min_freespace = freespace

    # print(freespace)

print(min_freespace)

# lower left corner of house itself
x, y = 2.0, 2.0
# upper left corner of house next to this house (left)
a = 0.0
b = 2.0
# width and depth of house next to this house (left)
width, depth = 0.0, 8.0

for y in range(4, 20):
    freespace = 0.0
    x = 2.0
    while True:
        if b <= float(y) / 2 < b + depth and a <= x < a + width:
            break
        elif x == 160.0 or x == 0:
            break
        elif y == 180.0 or y == 0:
            break
        else:
            freespace = freespace + 0.5
        x -= 0.5
    if freespace < min_freespace:
        min_freespace = freespace
#     print(freespace)
#
print(min_freespace)



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

plt.title("Map AmstelHaege")
plt.grid()
plt.show()
