import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
from math import hypot
from house_classes import *

with open('Data/amstel.json') as file:
    data = json.load(file)

amstel_width = int(data["map"]["width"])
amstel_height = int(data["map"]["height"])

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
        elif current_x + current_width + current_house.freespace > int(data["map"]["width"]) or current_y + current_depth + current_house.freespace > int(data["map"]["height"]):
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

repetition = []
for repeat in range(1):
    all_positive = False
    while all_positive == False:
        all_positive = True
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
                    x = random.randrange(0, 150, 1)
                    y = random.randrange(0, 170, 1)

                    # append to houses
                    houses.append(Singlefamily(i, x, y, 0))

                    # apply function
                    singlefamily = calculate_freespace(houses)

                    singlefamily.calculateprice()

                    if singlefamily.extra_freespace < 0:
                        del houses[-1]
                    else:
                        sf = data["houses"]["sf"]
                        # create rectangle
                        rect1 = patches.Rectangle((singlefamily.x, singlefamily.y), float(sf["width"]), float(sf["depth"]), color="blue")
                        rect2=  patches.Rectangle((singlefamily.x  , singlefamily.y -singlefamily.freespace), singlefamily.width, singlefamily.freespace, edgecolor="darkorange",facecolor="white")
                        rect3=  patches.Rectangle((singlefamily.x  + singlefamily.width , singlefamily.y), singlefamily.freespace,singlefamily.depth,edgecolor="darkorange",facecolor="white")
                        rect4=  patches.Rectangle((singlefamily.x  , singlefamily.y  + singlefamily.depth), singlefamily.width, singlefamily.freespace,edgecolor="darkorange",facecolor="white")
                        rect5=  patches.Rectangle((singlefamily.x -singlefamily.freespace , singlefamily.y ), singlefamily.freespace, singlefamily.depth,edgecolor="darkorange",facecolor="white")
                        wedge1 = patches.Wedge((singlefamily.x, singlefamily.y), singlefamily.freespace, 180, 270, edgecolor="darkorange",facecolor="white")
                        wedge2 = patches.Wedge((singlefamily.x + singlefamily.width, singlefamily.y), singlefamily.freespace, 270, 360,edgecolor="darkorange",facecolor="white")
                        wedge3 = patches.Wedge((singlefamily.x+ singlefamily.width, singlefamily.y + singlefamily.depth), singlefamily.freespace, 0, 90, edgecolor="darkorange",facecolor="white")
                        wedge4 = patches.Wedge((singlefamily.x, singlefamily.y  + singlefamily.depth), singlefamily.freespace, 90, 180, edgecolor="darkorange",facecolor="white")
                        ax.add_patch(rect1)
                        ax.add_patch(rect2)
                        ax.add_patch(rect3)
                        ax.add_patch(rect4)
                        ax.add_patch(rect5)
                        ax.add_patch(wedge1)
                        ax.add_patch(wedge2)
                        ax.add_patch(wedge3)
                        ax.add_patch(wedge4)
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

                    # apply function
                    bungalow = calculate_freespace(houses)

                    bungalow.calculateprice()

                    if bungalow.extra_freespace < 0:
                        del houses[-1]
                    else:
                        b = data["houses"]["b"]
                        # create rectangle
                        rect11 = patches.Rectangle((bungalow.x, bungalow.y), float(b["width"]), float(b["depth"]), color="deeppink")
                        rect12=  patches.Rectangle((bungalow.x  , bungalow.y -bungalow.freespace), bungalow.width, bungalow.freespace,edgecolor="darkorange",facecolor="white")
                        rect13=  patches.Rectangle((bungalow.x  + bungalow.width , bungalow.y), bungalow.freespace,bungalow.depth,edgecolor="darkorange",facecolor="white")
                        rect14=  patches.Rectangle((bungalow.x  , bungalow.y  + bungalow.depth), bungalow.width, bungalow.freespace,edgecolor= "darkorange",facecolor="white")
                        rect15=  patches.Rectangle((bungalow.x -bungalow.freespace , bungalow.y ), bungalow.freespace, bungalow.depth,edgecolor="darkorange",facecolor="white")
                        wedge9 = patches.Wedge((bungalow.x, bungalow.y), bungalow.freespace, 180, 270, edgecolor="darkorange",facecolor="white")
                        wedge10 = patches.Wedge((bungalow.x + bungalow.width, bungalow.y), bungalow.freespace, 270, 360, edgecolor="darkorange",facecolor="white")
                        wedge11 = patches.Wedge((bungalow.x+ bungalow.width, bungalow.y + bungalow.depth), bungalow.freespace, 0, 90, edgecolor="darkorange",facecolor="white")
                        wedge12 = patches.Wedge((bungalow.x, bungalow.y  + bungalow.depth), bungalow.freespace, 90, 180, edgecolor="darkorange",facecolor="white")
                        ax.add_patch(rect11)
                        ax.add_patch(rect12)
                        ax.add_patch(rect13)
                        ax.add_patch(rect14)
                        ax.add_patch(rect15)
                        ax.add_patch(wedge9)
                        ax.add_patch(wedge10)
                        ax.add_patch(wedge11)
                        ax.add_patch(wedge12)
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

                    # apply function
                    maison = calculate_freespace(houses)

                    maison.calculateprice()

                    if maison.extra_freespace < 0:
                        del houses[-1]
                    else:
                        m = data["houses"]["m"]
                        # create rectangle
                        rect6 = patches.Rectangle((maison.x, maison.y), float(m["width"]), float(m["depth"]), color="gold")
                        rect7=  patches.Rectangle((maison.x  , maison.y -maison.freespace), maison.width, maison.freespace,edgecolor="darkorange",facecolor="white")
                        rect8=  patches.Rectangle((maison.x  + maison.width , maison.y), maison.freespace,maison.depth,edgecolor="darkorange",facecolor="white")
                        rect9=  patches.Rectangle((maison.x  , maison.y  + maison.depth), maison.width, maison.freespace,edgecolor="darkorange",facecolor="white")
                        rect10=  patches.Rectangle((maison.x -maison.freespace , maison.y ), maison.freespace, maison.depth,edgecolor="darkorange",facecolor="white")
                        wedge5 = patches.Wedge((maison.x, maison.y), maison.freespace, 180, 270, edgecolor="darkorange",facecolor="white")
                        wedge6 = patches.Wedge((maison.x + maison.width, maison.y), maison.freespace, 270, 360, edgecolor="darkorange",facecolor="white")
                        wedge7 = patches.Wedge((maison.x+ maison.width, maison.y + maison.depth), maison.freespace, 0, 90, edgecolor="darkorange",facecolor="white")
                        wedge8 = patches.Wedge((maison.x, maison.y  + maison.depth), maison.freespace, 90, 180,edgecolor="darkorange",facecolor="white")
                        ax.add_patch(rect6)
                        ax.add_patch(rect7)
                        ax.add_patch(rect8)
                        ax.add_patch(rect9)
                        ax.add_patch(rect10)
                        ax.add_patch(wedge5)
                        ax.add_patch(wedge6)
                        ax.add_patch(wedge7)
                        ax.add_patch(wedge8)
                        positive = True
            # water
            for i in range(4):
                positive = False
                while positive == False:
                    # create random x and y
                    x = random.randrange(0, amstel_width, 1)
                    y = random.randrange(0, amstel_height, 1)

                    # append to houses
                    houses.append(Water(i + 20, x, y, 0))
                    # print(Water(18, 20, x, y))

                    # apply function
                    water = calculate_freespace(houses)

                    if water.extra_freespace < 0:
                        del houses[-1]
                    else:

                        # create rectangle
                        rect6 = patches.Rectangle((water.x, water.y), 18, 20, color="skyblue")
                        ax.add_patch(rect6)
                        positive = True

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
                elif current_x + current_width + current_house.freespace > int(data["map"]["width"]) or current_y + current_depth + current_house.freespace > int(data["map"]["height"]):
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
    print(house)
repetition.append(total)
repetition.sort()

# print(total)
print(repetition)

plt.xlim(0, amstel_width)
plt.ylim(0, amstel_height)


major_xticks = np.arange(0, amstel_width, 1)

major_yticks = np.arange(0, amstel_height, 1)


plt.xticks(major_xticks)
plt.yticks(major_yticks)

# show map
plt.title("Map AmstelHaege")
plt.grid()
plt.show()
