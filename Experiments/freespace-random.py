import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
from math import hypot
from house_classes import *
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection


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

        # upper left corner of current house
        x, y = current_house.x, current_house.y + current_house.depth

        circle_x = x
        circle_y = y

        # lower left corner of closest house above current house
        a = house.x
        b = house.y

        # lower right corner of closest house above current house
        rect_x = a + house.width
        rect_y = b

        # width and depth of closest house above current house
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

        if rect_x <= circle_x and rect_y >= circle_y:
            radius = hypot(rect_x - circle_x, rect_y - circle_y)
            radius = round(radius * 2) / 2
            if radius < min_radius:
                min_radius = radius
            if radius < min_freespace:
                min_freespace = radius

        # upper right corner of current house
        x, y = current_house.x + current_house.width , current_house.y + current_house.depth

        circle_x = x
        circle_y = y

        # upper left corner of closest house right of current house
        a = house.x
        b = house.y + house.depth

        # lower left corner of closest house right of current house
        rect_x = a
        rect_y = b - house.depth

        # width and depth of closest house right of current house
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

        if rect_x >= circle_x and rect_y >= circle_y:
            radius = hypot(rect_x - circle_x, rect_y - circle_y)
            radius = round(radius * 2) / 2
            if radius < min_radius:
                min_radius = radius
            if radius < min_freespace:
                min_freespace = radius
            # print(house, radius)
        # print(min_freespace)

        # lower right corner of current house
        x, y = current_house.x + current_house.width, current_house.y

        circle_x = x
        circle_y = y

        # upper right corner of closest house underneath current house
        a = house.x + house.width
        b = house.y + house.depth

        # upper left corner of closest house underneath current house
        rect_x = a - house.width
        rect_y = b

        # width and depth of closest house underneath current house
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

            if rect_x >= circle_x and rect_y <= circle_y:
                radius = hypot(rect_x - circle_x, rect_y - circle_y)
                radius = round(radius * 2) / 2
                if radius < min_radius:
                    min_radius = radius
                if radius < min_freespace:
                    min_freespace = radius
                    # print(house, radius)

            # print(freespace)

        # print(min_freespace)

        # lower left corner of current house
        x, y = current_house.x, current_house.y
        circle_x = x
        circle_y = y

        # lower right corner of closest house left of current house
        a = house.x + house.width
        b = house.y

        # upper right corner of closest house left of current house
        rect_x = a
        rect_y = b + house.depth

        # width and depth of closest house left of current house
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

        if rect_x <= circle_x and rect_y <= circle_y:
            radius = hypot(rect_x - circle_x, rect_y - circle_y)
            radius = round(radius * 2) / 2
            if radius < min_radius:
                min_radius = radius
            if radius < min_freespace:
                min_freespace = radius
            # print(house, radius)

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
                        print(i*i)
                        m = data["houses"]["m"]
                        rect6 =  patches.Rectangle((maison.x, maison.y), float(m["width"]), float(m["depth"]), color="gold")
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
                        # create rectangle
                        # rect = patches.Rectangle((maison.x, maison.y), float(m["width"]), float(m["depth"]), color="gold")
                        # ax.add_patch(rect3)
                        positive = True


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
                        print(i)


                        # create rectangle and wedge to display freepace in grid
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
                        print()
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


        for current_house in houses:
            min_freespace = 180.0
            min_radius = 180.0
            for house in houses:
                if house == current_house:
                    # print(house)
                    continue

                # upper left corner of current house
                x, y = current_house.x, current_house.y + current_house.depth

                circle_x = x
                circle_y = y

                # lower left corner of closest house above current house
                a = house.x
                b = house.y

                # lower right corner of closest house above current house
                rect_x = a + house.width
                rect_y = b

                # width and depth of closest house above current house
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

                if rect_x <= circle_x and rect_y >= circle_y:
                    radius = hypot(rect_x - circle_x, rect_y - circle_y)
                    radius = round(radius * 2) / 2
                    if radius < min_radius:
                        min_radius = radius
                    if radius < min_freespace:
                        min_freespace = radius
                    # print(house, radius)

                # upper right corner of current house
                x, y = current_house.x + current_house.width , current_house.y + current_house.depth

                circle_x = x
                circle_y = y

                # upper left corner of closest house right of current house
                a = house.x
                b = house.y + house.depth

                # lower left corner of closest house right of current house
                rect_x = a
                rect_y = b - house.depth

                # width and depth of closest house right of current house
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

                if rect_x >= circle_x and rect_y >= circle_y:
                    radius = hypot(rect_x - circle_x, rect_y - circle_y)
                    radius = round(radius * 2) / 2
                    if radius < min_radius:
                        min_radius = radius
                    if radius < min_freespace:
                        min_freespace = radius
                    # print(house, radius)

                # lower right corner of current house
                x, y = current_house.x + current_house.width, current_house.y

                circle_x = x
                circle_y = y

                # upper right corner of closest house underneath current house
                a = house.x + house.width
                b = house.y + house.depth

                # upper left corner of closest house underneath current house
                rect_x = a - house.width
                rect_y = b

                # width and depth of closest house underneath current house
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

                    if rect_x >= circle_x and rect_y <= circle_y:
                        radius = hypot(rect_x - circle_x, rect_y - circle_y)
                        radius = round(radius * 2) / 2
                        if radius < min_radius:
                            min_radius = radius
                        if radius < min_freespace:
                            min_freespace = radius
                            # print(house, radius)

                # lower left corner of current house
                x, y = current_house.x, current_house.y
                circle_x = x
                circle_y = y

                # lower right corner of closest house left of current house
                a = house.x + house.width
                b = house.y

                # upper right corner of closest house left of current house
                rect_x = a
                rect_y = b + house.depth

                # width and depth of closest house left of current house
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

                if rect_x <= circle_x and rect_y <= circle_y:
                    radius = hypot(rect_x - circle_x, rect_y - circle_y)
                    radius = round(radius * 2) / 2
                    if radius < min_freespace:
                        min_freespace = radius


            min_freespace -= current_house.freespace
            current_house.extra_freespace = min_freespace
            # print(current_house, ":", min_radius)

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