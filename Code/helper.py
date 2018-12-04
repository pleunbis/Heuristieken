import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
import csv
from math import hypot
from classes import *
from matplotlib.ticker import FuncFormatter

# load in data
with open('Data/amstel.json') as file:
    data = json.load(file)

# map dimensions
amstel_width = data["map"]["width"]
amstel_height = data["map"]["height"]

# calculates freespace for each house in list
def calculate_freespace(current_house, list):
    # current_house = list[-1]
    min_freespace = 180.0
    min_radius = 180.0
    for house in list:
        if house == current_house:
            # print(house)
            continue

        current_x = current_house.x
        current_y = current_house.y
        current_width = current_house.width
        current_depth = current_house.depth

        # lower left corner of closest house above current house
        other_x = house.x
        other_y = house.y
        other_width = house.width
        other_depth = house.depth

        # check if overlap
        if current_x <= other_x <= current_x + current_width and current_y <= other_y <= current_y + current_depth:
            min_freespace = -1
        elif current_x <= other_x <= current_x + current_width and current_y <= other_y + other_depth <= current_y + current_depth:
            min_freespace = -1
        elif current_x <= other_x + other_width <= current_x + current_width and current_y <= other_y + other_depth <= current_y + current_depth:
            min_freespace = -1
        elif current_x <= other_x + other_width <= current_x + current_width and current_y <= other_y <= current_y + current_depth:
            min_freespace = -1
        # check if on grid
        elif current_x + current_width + current_house.freespace > amstel_width or current_y + current_depth + current_house.freespace > amstel_height:
            min_freespace = -1
        elif current_x - current_house.freespace < 0 or current_y - current_house.freespace < 0:
            min_freespace = -1
        # house above this house
        if (current_x <= other_x <= current_x + current_width or current_x <= other_x + other_width <= current_x + current_width) and other_y >= current_y + current_depth:
            freespace = other_y - (current_y + current_depth)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # house to the right of this house
        elif (current_y <= other_y <= current_y + current_depth or current_y <= other_y + other_depth <= current_y + current_depth) and other_x >= current_x + current_width:
            freespace = other_x - (current_x + current_width)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # house beneath this house
        elif (current_x <= other_x <= current_x + current_width or current_x <= other_x + other_width <= current_x + current_width) and current_y >= other_y + other_depth:
            freespace = current_y - (other_y + other_depth)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # house to the left of this house
        elif (current_y <= other_y <= current_y + current_depth or current_y <= other_y + other_depth <= current_y + current_depth) and current_x >= other_x + other_width:
            freespace = current_x - (other_x + other_width)
            freespace = round(freespace * 2) / 2
            if freespace < min_freespace:
                min_freespace = freespace
        # top left corner
        elif other_x + other_width <= current_x and other_y >= current_y + current_depth:
            radius = hypot((other_x + other_width) - current_x, other_y - (current_y + current_depth))
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius
        # top right corner
        elif other_x >= current_x + current_width and other_y >= current_y + current_depth:
            radius = hypot(other_x - (current_x + current_width), other_y - (current_y + current_depth))
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius
        # bottom right corner
        elif other_x >= current_x + current_width and other_y + other_depth <= current_y:
            radius = hypot(other_x - (current_x + current_width), (other_y + other_depth) - current_y)
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius
        # bottom left corner
        elif other_x + other_width <= current_x and other_y + other_depth <= current_y:
            radius = hypot((other_x + other_width) - current_x, (other_y + other_depth) - current_y)
            radius = round(radius * 2) / 2
            if radius < min_freespace:
                min_freespace = radius

    min_freespace -= current_house.freespace
    current_house.extra_freespace = min_freespace

    return current_house

# shows calculated freespace around house on grid
def show_freespace(house):

    # colors
    line = "darkorange"
    fill = "white"

    # sides
    bottom = patches.Rectangle((house.x, house.y - house.freespace), house.width, house.freespace, edgecolor=line, facecolor=fill)
    right = patches.Rectangle((house.x + house.width , house.y), house.freespace, house.depth, edgecolor=line, facecolor=fill)
    top = patches.Rectangle((house.x, house.y + house.depth), house.width, house.freespace, edgecolor=line, facecolor=fill)
    left = patches.Rectangle((house.x - house.freespace, house.y), house.freespace, house.depth, edgecolor=line, facecolor=fill)

    # corners
    bottomleft = patches.Wedge((house.x, house.y), house.freespace, 180, 270, edgecolor=line, facecolor=fill)
    bottomright = patches.Wedge((house.x + house.width, house.y), house.freespace, 270, 360, edgecolor=line, facecolor=fill)
    topright = patches.Wedge((house.x + house.width, house.y + house.depth), house.freespace, 0, 90, edgecolor=line, facecolor=fill)
    topleft = patches.Wedge((house.x, house.y + house.depth), house.freespace, 90, 180, edgecolor=line, facecolor=fill)

    # add on grid
    ax.add_patch(bottom)
    ax.add_patch(right)
    ax.add_patch(top)
    ax.add_patch(left)
    ax.add_patch(bottomleft)
    ax.add_patch(bottomright)
    ax.add_patch(topright)
    ax.add_patch(topleft)

    return house

def plot_map(ax, fig):
    ax.set_facecolor("green")

    plt.xlim(0, amstel_width)
    plt.ylim(0, amstel_height)

    plt.ylabel("Length (in m)", size=14)
    plt.xlabel("Width (in m)", size=14)

    # major_xticks = np.arange(0, amstel_width, 1)
    #
    # major_yticks = np.arange(0, amstel_height, 1)
    #
    # plt.xticks(major_xticks)
    # plt.yticks(major_yticks)

    # show map
    fig.canvas.set_window_title("Map AmstelHaege")
    plt.title("Map AmstelHaege", size=16)
    # plt.grid()
    plt.show()

def plot_graph(list, title):
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

def millions(y, pos):
    return "%1.1f" % (y * 1e-6)



# random_start()
