from collections import namedtuple
from operator import mul
import numpy as np
from freespacefast import houses, amstel_width, amstel_height, calculate_freespace
from classes import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

Info = namedtuple('Info', 'start height')

def max_rect(mat, value=0):
    """returns (height, width, left_column, bottom_row) of the largest rectangle
    containing all `value`'s.

    Example:
    [[0, 0, 0, 0, 0, 0, 0, 0, 3, 2],
     [0, 4, 0, 2, 4, 0, 0, 1, 0, 0],
     [1, 0, 1, 0, 0, 0, 3, 0, 0, 4],
     [0, 0, 0, 0, 4, 2, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
     [4, 3, 0, 0, 1, 2, 0, 0, 0, 0],
     [3, 0, 0, 0, 2, 0, 0, 0, 0, 4],
     [0, 0, 0, 1, 0, 3, 2, 4, 3, 2],
     [0, 3, 0, 0, 0, 2, 0, 1, 0, 0]]
     gives: (3, 4, 6, 5)
    """
    it = iter(mat)
    hist = [(el==value) for el in next(it, [])]
    max_rect = max_rectangle_size(hist) + (0,)
    for irow,row in enumerate(it):
        hist = [(1+h) if el == value else 0 for h, el in zip(hist, row)]
        max_rect = max(max_rect, max_rectangle_size(hist) + (irow+1,), key=area)
        # irow+1, because we already used one row for initializing max_rect

    return max_rect

def max_rectangle_size(histogram):
    stack = []
    top = lambda: stack[-1]
    max_size = (0, 0, 0) # height, width and start position of the largest rectangle
    pos = 0 # current position in the histogram
    for pos, height in enumerate(histogram):
        start = pos # position where rectangle starts
        while True:
            if not stack or height > top().height:
                stack.append(Info(start, height)) # push
            elif stack and height < top().height:
                max_size = max(max_size, (top().height, (pos - top().start), top().start), key=area)
                start, _ = stack.pop()
                continue
            break # height == top().height goes here

    pos += 1
    for start, height in stack:
        max_size = max(max_size, (height, (pos - start), start), key=area)

    return max_size

def area(size):
    return size[0] * size[1]

matrix = np.zeros((360, 320))

for house in houses:
    x = int(house.x * 2)
    y = int(house.y * 2)
    width = int(house.width * 2)
    depth = int(house.depth * 2)

    for i in range(x, x + width):
        for j in range(y, y + depth):
            matrix[i][j] = 1

# print(matrix)
waters = []
opp = 0
while opp < 0.2 * (180 * 160):
    max_rect1 = max_rect(matrix)

    height = max_rect1[0]
    width = max_rect1[1]
    left_column = max_rect1[2]
    bottom_row = max_rect1[3]

    for i in range(left_column, left_column + width):
        for j in range(bottom_row - (height - 1), bottom_row + 1):
            matrix[j][i] = 2

    opp += width * height

    waters.append(Water(float(left_column / 2), float((bottom_row - (height - 1)) / 2), float(width / 2), float(height / 2)))

    print(matrix)
    print(opp)

fig = plt.figure()
ax = fig.add_subplot(111)
for house in houses:
    if house.width == 8:
        color = "blue"
    elif house.width == 10:
        color = "deeppink"
    elif house.width == 11:
        color = "gold"
    sf_rect = patches.Rectangle((house.x, house.y), house.width, house.depth, color=color)
    ax.add_patch(sf_rect)

for water in waters:
    sf_rect = patches.Rectangle((water.x, water.y), water.width, water.height, color="skyblue")
    ax.add_patch(sf_rect)

plt.xlim(0, amstel_width)
plt.ylim(0, amstel_height)

plt.ylabel("Length (in m)")
plt.xlabel("Width (in m)")

# major_xticks = np.arange(0, amstel_width, 1)

# major_yticks = np.arange(0, amstel_height, 1)

# plt.xticks(major_xticks)
# plt.yticks(major_yticks)

# show map
plt.title("Map AmstelHaege")
fig.canvas.set_window_title("Map AmstelHaege")
# plt.grid()
plt.show()
