import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
import csv
from math import hypot
from classes import *
from matplotlib.ticker import FuncFormatter
from collections import namedtuple
from operator import mul

# Load in data
with open('Data/amstel.json') as file:
    data = json.load(file)

# Map dimensions
amstel_width = data["map"]["width"]
amstel_height = data["map"]["height"]

def calculate_freespace(current_house, list):
    """Calculates freespace for each house in list"""
    min_freespace = 180.0
    min_radius = 180.0
    for house in list:
        if house == current_house:
            continue

        # Lower left corner of current house
        current_x = current_house.x
        current_y = current_house.y
        current_width = current_house.width
        current_depth = current_house.depth

        # Lower left corner of closest house above current house
        other_x = house.x
        other_y = house.y
        other_width = house.width
        other_depth = house.depth

        # Check if overlap
        if current_x <= other_x <= current_x + current_width and current_y <= other_y <= current_y + current_depth:
            min_freespace = -1
        elif current_x <= other_x <= current_x + current_width and current_y <= other_y + other_depth <= current_y + current_depth:
            min_freespace = -1
        elif current_x <= other_x + other_width <= current_x + current_width and current_y <= other_y + other_depth <= current_y + current_depth:
            min_freespace = -1
        elif current_x <= other_x + other_width <= current_x + current_width and current_y <= other_y <= current_y + current_depth:
            min_freespace = -1

        # Check if on map
        elif current_x + current_width + current_house.freespace > amstel_width or current_y + current_depth + current_house.freespace > amstel_height:
            min_freespace = -1
        elif current_x - current_house.freespace < 0 or current_y - current_house.freespace < 0:
            min_freespace = -1
        # House above current house
        if (current_x <= other_x <= current_x + current_width or current_x <= other_x + other_width <= current_x + current_width) and other_y >= current_y + current_depth:
            freespace = other_y - (current_y + current_depth)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # House right of current house
        elif (current_y <= other_y <= current_y + current_depth or current_y <= other_y + other_depth <= current_y + current_depth) and other_x >= current_x + current_width:
            freespace = other_x - (current_x + current_width)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # House beneath current house
        elif (current_x <= other_x <= current_x + current_width or current_x <= other_x + other_width <= current_x + current_width) and current_y >= other_y + other_depth:
            freespace = current_y - (other_y + other_depth)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # House left of current house
        elif (current_y <= other_y <= current_y + current_depth or current_y <= other_y + other_depth <= current_y + current_depth) and current_x >= other_x + other_width:
            freespace = current_x - (other_x + other_width)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # Top left corner
        elif other_x + other_width <= current_x and other_y >= current_y + current_depth:
            radius = hypot((other_x + other_width) - current_x, other_y - (current_y + current_depth))
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius
        # Top right corner
        elif other_x >= current_x + current_width and other_y >= current_y + current_depth:
            radius = hypot(other_x - (current_x + current_width), other_y - (current_y + current_depth))
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius
        # Bottom right corner
        elif other_x >= current_x + current_width and other_y + other_depth <= current_y:
            radius = hypot(other_x - (current_x + current_width), (other_y + other_depth) - current_y)
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius
        # Bottom left corner
        elif other_x + other_width <= current_x and other_y + other_depth <= current_y:
            radius = hypot((other_x + other_width) - current_x, (other_y + other_depth) - current_y)
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius

    min_freespace -= current_house.freespace
    current_house.extra_freespace = min_freespace

    return current_house

def add_water(houses):
    """Finds space for water in the map using a matrix"""

    Info = namedtuple('Info', 'start height')

    def max_rect(mat, value=0):
        """Find height, width of the largest rectangle containing all `value`'s"""
        it = iter(mat)
        hist = [(el==value) for el in next(it, [])]
        max_rect = max_rectangle_size(hist) + (0,)
        for irow,row in enumerate(it):
            # irow+1, because we already used one row for initializing max_rect
            hist = [(1+h) if el == value else 0 for h, el in zip(hist, row)]
            max_rect = max(max_rect, max_rectangle_size(hist) + (irow+1,), key=area)

        return max_rect

    def max_rectangle_size(histogram):
        """Find height, width of the largest rectangle that fits entirely under the histogram"""
        stack = []
        top = lambda: stack[-1]
        # height, width and start position of the largest rectangle
        max_size = (0, 0, 0)
        # current position in the histogram
        pos = 0
        for pos, height in enumerate(histogram):
            # position where rectangle starts
            start = pos
            while True:
                if not stack or height > top().height:
                    # push
                    stack.append(Info(start, height))
                elif stack and height < top().height:
                    max_size = max(max_size, (top().height, (pos - top().start), top().start), key=area)
                    start, _ = stack.pop()
                    continue
                # height == top().height goes here
                break

        pos += 1
        for start, height in stack:
            max_size = max(max_size, (height, (pos - start), start), key=area)
        return max_size
        print(max_size)

    def area(size):
        return size[0] * size[1]

    # Create matrix
    matrix = np.zeros((360, 320))

    for house in houses:
        x = int(house.x * 2)
        y = int(house.y * 2)
        # print(x)
        # print(y)
        width = int(house.width * 2)
        depth = int(house.depth * 2)

        for i in range(x, x + width):
            for j in range(y, y + depth):
                matrix[i][j] = 1

    # print(matrix)
    waters = []
    opp = 0
    # count_waters = 0
    # space_for_water = True

    # Check if water takes 20% of map
    while opp < 0.2 * (180 * 160):

        # Check if number of waters is < 4
        # if count_waters == 4:
        #     space_for_water = False
        #     break
        # else:
            # count_waters += count_waters
        max_rect1 = max_rect(matrix)
        print(max_rect1)
        height = max_rect1[0]
        width = max_rect1[1]
        left_column = max_rect1[2]
        bottom_row = max_rect1[3]

        for i in range(left_column, left_column + width):
            for j in range(bottom_row - (height - 1), bottom_row + 1):
                matrix[j][i] = 2

        opp += width * height

        # Append to list
        waters.append(Water(float(left_column / 2), float((bottom_row - (height-1)) / 2), float(width / 2), float(height / 2)))
        for water in waters:
            print(water)

        # print(matrix)
        print(opp)

    return waters

def show_freespace(house):
    """Shows calculated freespace around house on map"""

    # Colors
    line = "darkorange"
    fill = "darkorange"

    # Sides
    bottom = patches.Rectangle((house.x, house.y - house.freespace), house.width, house.freespace, edgecolor=line, facecolor=fill)
    right = patches.Rectangle((house.x + house.width , house.y), house.freespace, house.depth, edgecolor=line, facecolor=fill)
    top = patches.Rectangle((house.x, house.y + house.depth), house.width, house.freespace, edgecolor=line, facecolor=fill)
    left = patches.Rectangle((house.x - house.freespace, house.y), house.freespace, house.depth, edgecolor=line, facecolor=fill)

    # Corners
    bottomleft = patches.Wedge((house.x, house.y), house.freespace, 180, 270, edgecolor=line, facecolor=fill)
    bottomright = patches.Wedge((house.x + house.width, house.y), house.freespace, 270, 360, edgecolor=line, facecolor=fill)
    topright = patches.Wedge((house.x + house.width, house.y + house.depth), house.freespace, 0, 90, edgecolor=line, facecolor=fill)
    topleft = patches.Wedge((house.x, house.y + house.depth), house.freespace, 90, 180, edgecolor=line, facecolor=fill)

    # Add onto map
    ax.add_patch(bottom)
    ax.add_patch(right)
    ax.add_patch(top)
    ax.add_patch(left)
    ax.add_patch(bottomleft)
    ax.add_patch(bottomright)
    ax.add_patch(topright)
    ax.add_patch(topleft)

    return house

def create_map(houses, waters):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_facecolor("green")

    for house in houses:
        if house.width == 8:
            color = "blue"
        elif house.width == 10:
            color = "deeppink"
        elif house.width == 11:
            color = "gold"
        rect = patches.Rectangle((house.x, house.y), house.width, house.depth, color=color)
        ax.add_patch(rect)

    for water in waters:
        water_rect = patches.Rectangle((water.y, water.x), water.height,water.width, color="skyblue")
        ax.add_patch(water_rect)

    plt.xlim(0, amstel_width)
    plt.ylim(0, amstel_height)

    plt.ylabel("Length (in m)", size=12)
    plt.xlabel("Width (in m)", size=12)

    # major_xticks = np.arange(0, amstel_width, 1)
    # major_yticks = np.arange(0, amstel_height, 1)
    # plt.xticks(major_xticks)
    # plt.yticks(major_yticks)

    fig.canvas.set_window_title("Map AmstelHaege")
    plt.title("Map AmstelHaege", size=14)
    plt.show()

def plot_graph(list, title):

    def millions(y, pos):
        return "%1.1f" % (y * 1e-6)

    fig, ax = plt.subplots()
    plt.plot(list)
    plt.title(title)
    plt.xlabel("Iterations")
    plt.ylabel("Value of map (millions)")
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter)
    fig = plt.gcf()
    fig.canvas.set_window_title(title)
    plt.show()

# random_start()
