import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
import csv
from math import hypot
from classes import *

# load in data
with open('Data/amstel.json') as file:
    data = json.load(file)

# map dimensions
amstel_width = int(data["map"]["width"])
amstel_height = int(data["map"]["height"])

# calculates freespace for each house in list
def calculate_freespace(list):
    current_house = list[-1]
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

    # sides
    downside = patches.Rectangle((house.x, house.y - house.freespace), house.width, house.freespace, edgecolor="darkorange", facecolor="white")
    rightside = patches.Rectangle((house.x + house.width , house.y), house.freespace, house.depth, edgecolor="darkorange", facecolor="white")
    upside = patches.Rectangle((house.x, house.y + house.depth), house.width, house.freespace, edgecolor="darkorange", facecolor="white")
    leftside = patches.Rectangle((house.x - house.freespace, house.y), house.freespace, house.depth, edgecolor="darkorange", facecolor="white")

    # corners
    bottomleft = patches.Wedge((house.x, house.y), house.freespace, 180, 270, edgecolor="darkorange", facecolor="white")
    bottomright = patches.Wedge((house.x + house.width, house.y), house.freespace, 270, 360, edgecolor="darkorange", facecolor="white")
    topright = patches.Wedge((house.x + house.width, house.y + house.depth), house.freespace, 0, 90, edgecolor="darkorange", facecolor="white")
    topleft = patches.Wedge((house.x, house.y + house.depth), house.freespace, 90, 180, edgecolor="darkorange", facecolor="white")

    # add on grid
    ax.add_patch(downside)
    ax.add_patch(rightside)
    ax.add_patch(upside)
    ax.add_patch(leftside)
    ax.add_patch(bottomleft)
    ax.add_patch(bottomright)
    ax.add_patch(topright)
    ax.add_patch(topleft)

    return house


repetition = []
for repeat in range(1):
    all_positive = False
    while all_positive == False:
        all_positive = True
        plt.close("all")
        fig = plt.figure()
        ax = fig.add_subplot(111)
        Paste_house = True

        while Paste_house == True:
            Paste_house = False
            houses = []

            # singlefamily houses
            for i in range(12):
                positive = False
                while positive == False:
                    # create random x and y
                    x = random.randrange(0, amstel_width, 1)
                    y = random.randrange(0, amstel_height, 1)

                    # append to houses
                    houses.append(Singlefamily(i, x, y, 0))

                    # calculate freespace for singlefamily house
                    sf = calculate_freespace(houses)

                    sf.calculateprice()

                    if sf.extra_freespace < 0:
                        del houses[-1]
                    else:
                        sf_data = data["houses"]["sf"]
                        # create and show singlefamily house on grid
                        sf_rect = patches.Rectangle((sf.x, sf.y), float(sf_data["width"]), float(sf_data["depth"]), color="blue")
                        ax.add_patch(sf_rect)

                        # show freespace for singlefamily on grid
                        # show_freespace(sf)

                        positive = True

            # bungalows
            for i in range(5):
                positive = False
                while positive == False:
                    # create random x and y
                    x = random.randrange(0, amstel_width, 1)
                    y = random.randrange(0, amstel_height, 1)

                    # append to houses
                    houses.append(Bungalow(i + 12, x, y, 0))

                    # calculate freespace for bungalow
                    b = calculate_freespace(houses)

                    b.calculateprice()

                    if b.extra_freespace < 0:
                        del houses[-1]
                    else:
                        b_data = data["houses"]["b"]
                        # create and show bungalow on grid
                        b_rect = patches.Rectangle((b.x, b.y), float(b_data["width"]), float(b_data["depth"]), color="deeppink")
                        ax.add_patch(b_rect)

                        # show freespace for bungalow on grid
                        # show_freespace(b)

                        positive = True
                # print(current_house)

            # maisons
            for i in range(3):
                positive = False
                while positive == False:
                    # create random x and y
                    x = random.randrange(0, amstel_width, 1)
                    y = random.randrange(0, amstel_height, 1)

                    # append to houses
                    houses.append(Maison(i + 17, x, y, 0))

                    # calculate freespace for maison
                    m = calculate_freespace(houses)

                    m.calculateprice()

                    if m.extra_freespace < 0:
                        del houses[-1]
                    else:
                        m_data = data["houses"]["m"]
                        # create and show maison on grid
                        m_rect = patches.Rectangle((m.x, m.y), float(m_data["width"]), float(m_data["depth"]), color="gold")
                        ax.add_patch(m_rect)

                        # show freespace for maison on grid
                        # show_freespace(m)

                        positive = True
            # water
            # for i in range(4):
            #     positive = False
            #     while positive == False:
            #         # create random x and y
            #         x = random.randrange(0, amstel_width, 1)
            #         y = random.randrange(0, amstel_height, 1)
            #
            #         # append to houses
            #         houses.append(Water(i + 60, x, y, 0))
            #         # print(Water(18, 20, x, y))
            #
            #         # apply function
            #         water = calculate_freespace(houses)
            #
            #         if water.extra_freespace < 0:
            #             del houses[-1]
            #         else:
            #
            #             # create rectangle
            #             rect6 = patches.Rectangle((water.x, water.y), 18, 20, color="skyblue")
            #             ax.add_patch(rect6)
            #             positive = True

        for current_house in houses:
            min_freespace = 180.0
            min_radius = 180.0
            for house in houses:
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
                elif (current_x <= other_x <= current_x + current_width or current_x <= other_x + other_width <= current_x + current_width) and other_y >= current_y + current_depth:
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

            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    total = 0
    for house in houses:
        total = total + house.total_price
        # print(house)
    repetition.append(total)
    repetition.sort()

# print(total)
print(repetition)

# write values to csv file
# with open('randomwalk.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for item in repetition:
#         writer.writerows([[item]])

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
# plt.grid()
plt.show()
