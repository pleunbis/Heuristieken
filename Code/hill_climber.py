from freespacefast import houses, amstel_width, amstel_height, calculate_freespace
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
from math import hypot
from classes import *

def hill_climber(iterations):


    values = []
    counter = 0

    while counter < iterations:

        # print(counter)
        # generates random house number to move
        # print(houses[:-4])
        house_number = random.randrange(0, len(houses), 1)
        # print(house_number)

        old_x = houses[house_number].x
        old_y = houses[house_number].y
        # print(old_x, old_y)

        old_total = 0
        for house in houses:
            old_total = old_total + house.total_price
        # print(old_total)

        if len(values) == 0:
            # print("joe")
            values.append(old_total)

        # create random x and y
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)
        # print(new_x, new_y)

        houses[house_number].x = new_x
        houses[house_number].y = new_y

        all_positive = True

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

        # print("freespace berekend")

        new_total = 0
        for house in houses:
            new_total = new_total + house.total_price

        # print(all_positive, new_total)
        if not all_positive:
            houses[house_number].x = old_x
            houses[house_number].y = old_y
        elif old_total > new_total:
            counter += 1
            # print("joe")
            houses[house_number].x = old_x
            houses[house_number].y = old_y
            values.append(old_total)
        else:
            counter += 1
            # print("joe")
            values.append(new_total)

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
        #
        # for house in houses:
        #     print(house)

    return values

    fig, ax = plt.subplots()
    plt.plot(values)
    plt.title("Hill climber AmstelHaege")
    plt.xlabel("Iterations")
    plt.ylabel("Value of map (millions)")
    formatter = FuncFormatter(millions)
    ax.yaxis.set_major_formatter(formatter)
    # plt.axis([0, 4999, 0, 15000000])
    # plt.xticks(np.arange(0, 5000, 500))
    # plt.yticks(np.arange(0, 16000000, 1000000))
    fig = plt.gcf()
    fig.canvas.set_window_title("Hill climber AmstelHaege")
    plt.show()



    # plt.close("all")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for house in houses:
        if house.width == 8:
            color = "blue"
        elif house.width == 10:
            color = "deeppink"
        elif house.width == 11:
            color = "gold"
        elif house.width == 18:
            color = "skyblue"
        sf_rect = patches.Rectangle((house.x, house.y), house.width, house.depth, color=color)
        ax.add_patch(sf_rect)
        print(house)

    print(max(old_total, new_total))

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

def millions(y, pos):
    return "%1.1f" % (y * 1e-6)

alle_hill = []
for i in range(10):
    alle_hill.append(hill_climber(50))

gem_hill = [0] * 51

for hill in alle_hill:
    for i in range(len(hill)):
        gem_hill[i] += hill[i] / 10


print(alle_hill)
print(gem_hill)
