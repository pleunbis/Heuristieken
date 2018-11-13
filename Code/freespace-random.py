import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import numpy as np
import random
import math
from math import hypot
from house_classes import *

# def cal(houses):
#     current_house=houses[-1]
#     min_freespace = 180.0
#     for house in houses:
#         if house == current_house:
#             # print(house)
#             continue
#
#         # upper left corner of house itself
#         x, y = current_house.x, current_house.y + current_house.depth
#
#         # lower left corner of house above this house
#         a = house.x
#         b = house.y
#
#         # width and depth of house above this house
#         width, depth = house.width, house.depth
#
#         for x in range(int(current_house.x * 2), int((current_house.x + current_house.width) * 2 + 1)):
#             freespace = 0.0
#             y = current_house.y + current_house.depth
#             while True:
#                 if a <= float(x) / 2 <= a + width and b <= y <= b + depth:
#                     break
#                 elif y >= 180.0 or y <= 0:
#                     if freespace > current_house.freespace:
#                         freespace = 180
#                     break
#                 else:
#                     freespace = freespace + 0.5
#                 y += 0.5
#             if freespace < min_freespace:
#                 min_freespace = freespace
#
#         # print(house)
#         # print(min_freespace)
#
#         # upper right corner of house itself
#         x, y = current_house.x + current_house.width , current_house.y + current_house.depth
#
#         # upper left corner of house next to this house (right)
#         a = house.x
#         b = house.y + house.depth
#
#         # width and depth of house next to this house (right)
#         width, depth = house.width, house.depth
#
#         for y in range(int((current_house.y + current_house.depth) * 2), int(current_house.y * 2 - 1), -1):
#             freespace = 0.0
#             x = current_house.x + current_house.width
#             while True:
#                 if b - depth <= float(y) / 2 <= b and a <= x <= a + width:
#                     break
#                 elif x >= 160.0 or x <= 0:
#                     if freespace > current_house.freespace:
#                         freespace = 180
#                     break
#                 else:
#                     freespace = freespace + 0.5
#                 x += 0.5
#             if freespace < min_freespace:
#                 min_freespace = freespace
#
#         # print(min_freespace)
#
#         # lower right corner of house itself
#         x, y = current_house.x + current_house.width, current_house.y
#
#         # upper right corner of house underneath this house
#         a = house.x + house.width
#         b = house.y + house.depth
#
#         # width and depth of house underneath this house
#         width, depth = house.width, house.depth
#
#         for x in range(int((current_house.x + current_house.width) * 2), int(current_house.x * 2 - 1), -1):
#             freespace = 0.0
#             y = current_house.y
#             while True:
#                 if a - width <= float(x) / 2 <= a and b - depth <= y <= b:
#                     break
#                 elif y >= 180.0 or y <= 0:
#                     if freespace > current_house.freespace:
#                         freespace = 180
#                     break
#                 else:
#                     freespace = freespace + 0.5
#                 y -= 0.5
#
#             if freespace < min_freespace:
#                 min_freespace = freespace
#
#             # print(freespace)
#
#         # print(min_freespace)
#
#         # lower left corner of house itself
#         x, y = current_house.x, current_house.y
#
#         # lower right corner of house next to this house (left)
#         a = house.x + house.width
#         b = house.y
#
#         # width and depth of house next to this house (left)
#         width, depth = house.width, house.depth
#
#         for y in range(int(current_house.y * 2), int((current_house.y + current_house.depth) * 2 + 1)):
#             freespace = 0.0
#             x = current_house.x
#             while True:
#                 if b <= float(y) / 2 <= b + depth and a - width <= x <= a:
#                     break
#                 elif x >= 160.0 or x <= 0:
#                     if freespace > current_house.freespace:
#                         freespace = 180
#                     break
#                 else:
#                     freespace = freespace + 0.5
#                 x -= 0.5
#             if freespace < min_freespace:
#                 min_freespace = freespace
#
#     min_freespace -= current_house.freespace
#     current_house.extra_freespace = min_freespace
#
#     return current_house


repetition = []
for repeat in range(1):
    helemaalgoed = False
    while helemaalgoed == False:
        helemaalgoed = True
        fig = plt.figure()
        ax = fig.add_subplot(111)
        Paste_house = True

        while Paste_house == True:
            Paste_house = False
            houses = []

            # singlefamily houses
            for i in range(12):
                positief = False
                while positief == False:
                    # create random x and y
                    x = random.randrange(0, 170, 1)
                    y = random.randrange(0, 150, 1)

                    # append to houses
                    houses.append(Singlefamily(i, x, y, 0))
                    current_house=houses[-1]
                    min_freespace = 180.0
                    min_radius = 180.0
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
                        circle_x = x
                        circle_y = y


                        # lower right corner of house next to this house (left)
                        a = house.x + house.width
                        b = house.y

                        rect_x = a
                        rect_y = b + house.depth

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
                    # print(current_house, ":", min_radius)

                    # cal(houses)
                    current_house.calculateprice()
                    if current_house.extra_freespace < 0:
                        del houses[-1]
                    else:

                        # create rectangle
                        rect1 = matplotlib.patches.Rectangle((current_house.x, current_house.y), 8, 8, color="blue")
                        ax.add_patch(rect1)
                        positief = True
                # print(current_house)
                # create rectangle
                # rect1 = matplotlib.patches.Rectangle((x, y), 8, 8, color="blue")
                # ax.add_patch(rect1)

            # bungalows
            for i in range(5):
                positief = False
                while positief == False:
                    # create random x and y
                    x = random.randrange(0, 180, 1)
                    y = random.randrange(0, 160, 1)

                    # append to houses
                    houses.append(Bungalow(i + 12, x, y, 0))
                    current_house=houses[-1]
                    min_freespace = 180.0
                    min_radius = 180.0
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

                        circle_x = x
                        circle_y = y

                        # lower right corner of house next to this house (left)
                        a = house.x + house.width
                        b = house.y

                        # upper right corner of other house
                        rect_x = a
                        rect_y = b + house.depth

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
                    # print(current_house, ":", min_radius)
                    current_house.calculateprice()
                    if current_house.extra_freespace < 0:
                        del houses[-1]
                    else:

                        # create rectangle
                        rect2 = matplotlib.patches.Rectangle((current_house.x, current_house.y), 10, 7.5, color="deeppink")
                        ax.add_patch(rect2)
                        positief = True
                # print(current_house)
                # create rectangle
                # rect2 = matplotlib.patches.Rectangle((x, y), 10, 7.5, color="deeppink")
                # ax.add_patch(rect2)

            # maisons
            for i in range(3):
                positief = False
                while positief == False:
                    # create random x and y
                    x = random.randrange(0, 160, 1)
                    y = random.randrange(0, 180, 1)

                    # append to houses
                    houses.append(Maison(i + 17, x, y, 0))
                    current_house=houses[-1]
                    min_freespace = 180.0
                    min_radius = 180.0
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

                        circle_x = x
                        circle_y = y

                        # lower right corner of house next to this house (left)
                        a = house.x + house.width
                        b = house.y

                        # upper right corner of other house
                        rect_x = a
                        rect_y = b + house.depth

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
                    # print(current_house, ":", min_radius)
                    current_house.calculateprice()

                    if current_house.extra_freespace < 0:

                        del houses[-1]
                    else:

                        # create rectangle
                        rect3 = matplotlib.patches.Rectangle((current_house.x, current_house.y), 11, 10.5, color="gold")
                        ax.add_patch(rect3)
                        positief = True

        for current_house in houses:
            min_freespace = 180.0
            min_radius = 180.0
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
                circle_x = x
                circle_y = y


                # lower right corner of house next to this house (left)
                a = house.x + house.width
                b = house.y

                rect_x = a
                rect_y = b + house.depth

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
            # print(current_house, ":", min_radius)

            # cal(houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                helemaalgoed = False



    total = 0
    for house in houses:
        total = total + house.total_price
        print(house)
    repetition.append(total)
    repetition.sort()
# print(total)
print(repetition)
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
