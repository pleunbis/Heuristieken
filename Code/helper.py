import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
import csv
from math import hypot
from matplotlib.ticker import FuncFormatter
from collections import namedtuple
from operator import mul
from classes import *

# load in data
with open('Data/amstel.json') as file:
    data = json.load(file)

# map dimensions
amstel_width = data["map"]["width"]
amstel_height = data["map"]["height"]


def calculate_freespace(current_house, list):
    """Calculates freespace for each house in list"""

    min_freespace = 180.0
    min_radius = 180.0
    for house in list:
        if house == current_house:
            continue

        # lower left corner of current house
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
        if (current_x <= other_x <= current_x + current_width
            and current_y <= other_y <= current_y + current_depth):
            min_freespace = -1
        elif (current_x <= other_x <= current_x + current_width
            and current_y <= other_y + other_depth <= current_y + current_depth):
            min_freespace = -1
        elif (current_x <= other_x + other_width <= current_x + current_width
            and current_y <= other_y + other_depth <= current_y + current_depth):
            min_freespace = -1
        elif (current_x <= other_x + other_width <= current_x + current_width
            and current_y <= other_y <= current_y + current_depth):
            min_freespace = -1

        # check if on map
        elif (current_x + current_width + current_house.freespace > amstel_width
            or current_y + current_depth + current_house.freespace > amstel_height):
            min_freespace = -1
        elif (current_x - current_house.freespace < 0
            or current_y - current_house.freespace < 0):
            min_freespace = -1

        # house above current house
        if ((current_x <= other_x <= current_x + current_width
            or current_x <= other_x + other_width <= current_x + current_width)
            and other_y >= current_y + current_depth):
            freespace = other_y - (current_y + current_depth)
            freespace = round(freespace * 2) / 2
            
            if freespace < min_freespace:
                min_freespace = freespace
        
        # house right of current house
        elif ((current_y <= other_y <= current_y + current_depth
            or current_y <= other_y + other_depth <= current_y + current_depth)
            and other_x >= current_x + current_width):
            freespace = other_x - (current_x + current_width)
            freespace = round(freespace * 2) / 2
            
            if freespace < min_freespace:
                min_freespace = freespace
        
        # house beneath current house
        elif ((current_x <= other_x <= current_x + current_width
            or current_x <= other_x + other_width <= current_x + current_width)
            and current_y >= other_y + other_depth):
            freespace = current_y - (other_y + other_depth)
            freespace = round(freespace * 2) / 2
            
            if freespace < min_freespace:
                min_freespace = freespace
        
        # house left of current house
        elif ((current_y <= other_y <= current_y + current_depth
            or current_y <= other_y + other_depth <= current_y + current_depth)
            and current_x >= other_x + other_width):
            freespace = current_x - (other_x + other_width)
            freespace = round(freespace * 2) / 2
            
            if freespace < min_freespace:
                min_freespace = freespace
        
        # top left corner
        elif (other_x + other_width <= current_x
            and other_y >= current_y + current_depth):
            radius = hypot(
                    (other_x + other_width) - current_x,
                    other_y - (current_y + current_depth)
                    )
            radius = round(radius * 2) / 2
            
            if radius < min_freespace:
                min_freespace = radius
        
        # top right corner
        elif (other_x >= current_x + current_width
            and other_y >= current_y + current_depth):
            radius = hypot(
                    other_x - (current_x + current_width),
                    other_y - (current_y + current_depth)
                    )
            radius = round(radius * 2) / 2
            
            if radius < min_freespace:
                min_freespace = radius
        
        # bottom right corner
        elif (other_x >= current_x + current_width
            and other_y + other_depth <= current_y):
            radius = hypot(
                    other_x - (current_x + current_width),
                    (other_y + other_depth) - current_y
                    )
            radius = round(radius * 2) / 2
            
            if radius < min_freespace:
                min_freespace = radius
        
        # bottom left corner
        elif (other_x + other_width <= current_x
            and other_y + other_depth <= current_y):
            radius = hypot(
                    (other_x + other_width) - current_x,
                    (other_y + other_depth) - current_y)
            radius = round(radius * 2) / 2
            
            if radius < min_freespace:
                min_freespace = radius

    min_freespace -= current_house.freespace
    current_house.extra_freespace = min_freespace

    return current_house


def add_houses(nr_houses, all_positive):
    """Finds valid location for house in map"""

    houses = []

    # if 60 version is run, add water already
    if nr_houses == 60:
        waters = add_water(houses, nr_houses)

    # add singlefamily houses
    for i in range(int(0.6 * nr_houses)):
        positive = False

        while positive == False:
            x = random.randrange(0, amstel_width, 1)

            # if 60 version is run, set random range within boundaries
            if nr_houses == 60:
                if x < 40 or x > 132:
                    y = random.randrange(36, 116, 1)
                else:
                    y = random.randrange(0, amstel_height, 1)

            # random range for other versions
            else:
                y = random.randrange(0, amstel_height, 1)

            # append to houses
            houses.append(Singlefamily(i, x, y, 0))

            # calculate freespace for singlefamily house
            current_house = houses[-1]
            
            sf = calculate_freespace(current_house, houses)

            # calculate price for singlefamily house
            sf.calculateprice()

            # if houses overlap, delete this house from list
            if sf.extra_freespace < 0:
                del houses[-1]
            else:
                # house is added, go to the next house
                positive = True

    # add the bungalows
    for i in range(int(0.25 * nr_houses)):
        positive = False

        while positive == False:
            x = random.randrange(0, amstel_width, 1)

            # if 60 version is run, set random range within boundaries
            if nr_houses == 60:
                if x < 40 or x > 130:
                    y = random.randrange(36, 116, 1)
                else:
                    y = random.randrange(0, amstel_height, 1)

            # random range for other versions
            else:
                y = random.randrange(0, amstel_height, 1)

            # append to houses
            houses.append(Bungalow(int(i + 0.6 * nr_houses), x, y, 0))

            # calculate freespace for bungalow
            current_house = houses[-1]
            
            bgl = calculate_freespace(current_house, houses)

            # calculate price for bungalow
            bgl.calculateprice()

            # if houses overlap, delete this house from list
            if bgl.extra_freespace < 0:
                del houses[-1]
            else:
                # house is added, go to next house
                positive = True

    # add the maisons
    for i in range(int(0.15 * nr_houses)):
        positive = False
        counter = 0
        while positive == False:
            x = random.randrange(0, amstel_width, 1)

            # if 60 version is run, set random range within boundaries
            if nr_houses == 60:
                if x < 40 or x > 129:
                    y = random.randrange(36, 113, 1)
                else:
                    y = random.randrange(0, amstel_height, 1)

            # random range for other versions
            else:
                y = random.randrange(0, amstel_height, 1)

            # append to houses
            houses.append(Maison(int(i + 0.85 * nr_houses), x, y, 0))

            # calculate freespace for maison
            current_house = houses[-1]
            
            ms = calculate_freespace(current_house, houses)

            # calculate price for maison
            ms.calculateprice()

            # if houses overlap, delete this house from list
            if ms.extra_freespace < 0:
                del houses[-1]
                counter += 1
                if counter == 1000:
                    positive = True
                    all_positive = False
            else:
                # house is added, go to next house
                positive = True

    # if 60 version is run, give empty water list
    if nr_houses != 60:
        waters = []

    return [houses, waters, all_positive]


def swap_houses(houses, house_number):
    """Swaps x and y coordinates of house"""

    # create random x and y for new place of random chosen house
    if len(houses) == 60:
        if houses[house_number].width == 8:
            new_x = random.randrange(0, amstel_width, 1)
            if new_x < 40 or new_x > 132:
                new_y = random.randrange(36, 116, 1)
            else:
                new_y = random.randrange(0, amstel_height, 1)
        elif houses[house_number].width == 10:
            new_x = random.randrange(0, amstel_width, 1)
            if new_x < 40 or new_x > 130:
                new_y = random.randrange(36, 116, 1)
            else:
                new_y = random.randrange(0, amstel_height, 1)
        else:
            new_x = random.randrange(0, amstel_width, 1)
            if new_x < 40 or new_x > 129:
                new_y = random.randrange(36, 113, 1)
            else:
                new_y = random.randrange(0, amstel_height, 1)

    else:
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)

    # set x and y for the random house
    houses[house_number].x = new_x
    houses[house_number].y = new_y

    return [new_x, new_y]


def add_water(houses, nr_houses):
    """Finds space for water in the map using a matrix"""

    # https://stackoverflow.com/questions/2478447/
    # find-largest-rectangle-containing-only-zeros-in-an-n%C3%97n-binary-matrix

    if nr_houses == 40 or nr_houses == 20:
        Info = namedtuple('Info', 'start height')

        def max_rect(mat, value=0):
            """Find height, width of the largest rectangle
            containing all `value`'s"""

            it = iter(mat)
            hist = [(el==value) for el in next(it, [])]
            max_rect = max_rectangle_size(hist) + (0,)
            for irow,row in enumerate(it):
                # irow+1, we already used one row for initializing max_rect
                hist = [(1+h) if el == value else 0 for h, el in zip(hist, row)]
                max_rect = max(max_rect,
                            max_rectangle_size(hist) + (irow+1,), key=area
                            )

            return max_rect

        def max_rectangle_size(histogram):
            """Find height, width of the largest rectangle
            that fits entirely under the histogram"""

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
                        stack.append(Info(start, height))
                    elif stack and height < top().height:
                        max_size = max(max_size,
                                    (top().height, (pos - top().start),
                                    top().start), key=area
                                    )
                        start, _ = stack.pop()
                        continue
                    break

            pos += 1
            for start, height in stack:
                max_size = max(max_size, 
                            (height, (pos - start), start), key=area
                            )

            return max_size

        def area(size):
            return size[0] * size[1]

        # create matrix
        matrix = np.zeros((362, 322))

        for house in houses:
            x = int(house.x * 2)
            y = int(house.y * 2)
            width = int(house.width * 2)
            depth = int(house.depth * 2)

            for i in range(x, x + width):
                for j in range(y, y + depth):
                    matrix[i][j] = 1

        waters = []
        opp = 0

        # check if water takes 20% of map and max of 4 waters
        while opp < 0.2 * (180 * 160) and len(waters) < 4:

            max_rect1 = max_rect(matrix)
            height = max_rect1[0]
            width = max_rect1[1]
            left_column = max_rect1[2]
            bottom_row = max_rect1[3]

            # apply height and width ratio
            if height > 4 * width:
                height = 4 * width
            elif width > 4 * height:
                width = 4 * height

            for i in range(left_column, left_column + width - 1):
                for j in range(bottom_row - (height - 1), bottom_row):
                    matrix[j][i] = 2

            # size of water surface
            opp += (width / 2) * (height / 2)

            # append to list
            waters.append(Water(float(left_column / 2),
                    float((bottom_row - (height-1)) / 2),
                    float(width / 2),
                    float(height / 2)))

        # empty list if required amount of water is not met
        if opp < 0.2 * (180 * 160):
            waters = []

    # if 60 version is run, add fixed water locations
    else:
        waters = []
        waters.append(Water(0, 0 , 36 , 40))
        waters.append(Water(0, 140 , 36 , 40))
        waters.append(Water(124, 0 , 36 , 40))
        waters.append(Water(124, 140 , 36 , 40))

    return waters


def show_freespace(house):
    """Shows calculated freespace around house on map"""

    # colors
    line = "darkorange"
    fill = "darkorange"

    # sides
    bottom = patches.Rectangle(
            (house.x, house.y - house.freespace),
            house.width, house.freespace, edgecolor=line, facecolor=fill
            )
    right = patches.Rectangle(
            (house.x + house.width, house.y),
            house.freespace, house.depth, edgecolor=line, facecolor=fill
            )
    top = patches.Rectangle(
            (house.x, house.y + house.depth),
            house.width, house.freespace, edgecolor=line, facecolor=fill
            )
    left = patches.Rectangle(
            (house.x - house.freespace, house.y),
            house.freespace, house.depth, edgecolor=line, facecolor=fill
            )

    # corners
    bottomleft = patches.Wedge(
            (house.x, house.y),
            house.freespace, 180, 270, edgecolor=line, facecolor=fill
            )
    bottomright = patches.Wedge(
            (house.x + house.width, house.y),
            house.freespace, 270, 360, edgecolor=line, facecolor=fill
            )
    topright = patches.Wedge(
            (house.x + house.width, house.y + house.depth),
            house.freespace, 0, 90, edgecolor=line, facecolor=fill
            )
    topleft = patches.Wedge(
            (house.x, house.y + house.depth),
            house.freespace, 90, 180, edgecolor=line, facecolor=fill
            )

    # add onto map
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
    """Transfers outcomes into a map"""

    fig = plt.figure()
    ax = fig.add_subplot(111)

    fig.canvas.set_window_title("Map AmstelHaege")
    ax.set_facecolor("green")

    # define colors of every housetype
    for house in houses:
        if house.width == 8:
            color = "blue"
        elif house.width == 10:
            color = "deeppink"
        elif house.width == 11:
            color = "gold"

        # add houses onto map
        rect = patches.Rectangle(
            (house.x, house.y), house.width, house.depth, color=color
            )
        
        ax.add_patch(rect)

    for water in waters:
        # add water onto map
        water_rect = patches.Rectangle(
            (water.y, water.x), water.height,water.width, color="skyblue"
            )
        
        ax.add_patch(water_rect)

    plt.xlim(0, amstel_width)
    plt.ylim(0, amstel_height)
    plt.title("Final map AmstelHaege", size=14)
    plt.xlabel("Width (in m)", size=12)
    plt.ylabel("Length (in m)", size=12)
    plt.show()


def plot_graph(list, title):
    """Creates linegraph of values"""

    def millions(y, pos):
        return "%1.1f" % (y * 1e-6)

    # avoid unnecessary zeroes on visualisation
    formatter = FuncFormatter(millions)

    fig, ax = plt.subplots()
    fig.canvas.set_window_title(title)
    ax.yaxis.set_major_formatter(formatter)
    
    plt.plot(list)
    plt.title(title, size=14)
    plt.xlabel("Iterations", size=12)
    plt.ylabel("Value of map (millions)", size=12)
    plt.show()
