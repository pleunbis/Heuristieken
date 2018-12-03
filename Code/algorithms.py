from helper import *
# from freespacefast import houses
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import json
from math import hypot
from classes import *
import math

def random_start(nr_houses):
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
                for i in range(int(0.6 * nr_houses)):
                    positive = False
                    while positive == False:
                        # create random x and y
                        x = random.randrange(0, amstel_width, 1)
                        y = random.randrange(0, amstel_height, 1)

                        # append to houses
                        houses.append(Singlefamily(i, x, y, 0))

                        # calculate freespace for singlefamily house
                        current_house = houses[-1]
                        sf = calculate_freespace(current_house, houses)

                        sf.calculateprice()

                        if sf.extra_freespace < 0:
                            del houses[-1]
                        else:
                            sf_data = data["houses"]["sf"]
                            # create and show singlefamily house on grid
                            sf_rect = patches.Rectangle((sf.x, sf.y), sf_data["width"], sf_data["depth"], color="blue")
                            ax.add_patch(sf_rect)

                            # show freespace for singlefamily on grid
                            # show_freespace(sf)

                            positive = True

                # bungalows
                for i in range(int(0.25 * nr_houses)):
                    positive = False
                    while positive == False:
                        # create random x and y
                        x = random.randrange(0, amstel_width, 1)
                        y = random.randrange(0, amstel_height, 1)

                        # append to houses
                        houses.append(Bungalow(int(i + 0.6 * nr_houses), x, y, 0))

                        # calculate freespace for bungalow
                        current_house = houses[-1]
                        b = calculate_freespace(current_house, houses)

                        b.calculateprice()

                        if b.extra_freespace < 0:
                            del houses[-1]
                        else:
                            b_data = data["houses"]["b"]
                            # create and show bungalow on grid
                            b_rect = patches.Rectangle((b.x, b.y), b_data["width"], b_data["depth"], color="deeppink")
                            ax.add_patch(b_rect)

                            # show freespace for bungalow on grid
                            # show_freespace(b)

                            positive = True

                # maisons
                for i in range(int(0.15 * nr_houses)):
                    positive = False
                    while positive == False:
                        # create random x and y
                        x = random.randrange(0, amstel_width, 1)
                        y = random.randrange(0, amstel_height, 1)

                        # append to houses
                        houses.append(Maison(int(i + 0.85 * nr_houses), x, y, 0))

                        # calculate freespace for maison
                        current_house = houses[-1]
                        m = calculate_freespace(current_house, houses)

                        m.calculateprice()

                        if m.extra_freespace < 0:
                            del houses[-1]
                        else:
                            m_data = data["houses"]["m"]
                            # create and show maison on grid
                            m_rect = patches.Rectangle((m.x, m.y), m_data["width"], m_data["depth"], color="gold")
                            ax.add_patch(m_rect)

                            # show freespace for maison on grid
                            # show_freespace(m)

                            positive = True

            for current_house in houses:
                calculate_freespace(current_house, houses)
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

    # plot_map(ax, fig)

    return houses

def hill_climber(houses, iterations):

    values = []
    counter = 0

    while counter < iterations:
        house_number = random.randrange(0, len(houses), 1)

        old_x = houses[house_number].x
        old_y = houses[house_number].y

        old_total = 0
        for house in houses:
            old_total = old_total + house.total_price

        if len(values) == 0:
            # print("joe")
            values.append(old_total)

        # create random x and y
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)

        houses[house_number].x = new_x
        houses[house_number].y = new_y

        all_positive = True

        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

        new_total = 0
        for house in houses:
            new_total = new_total + house.total_price

        if not all_positive:
            houses[house_number].x = old_x
            houses[house_number].y = old_y
        elif old_total > new_total:
            counter += 1
            houses[house_number].x = old_x
            houses[house_number].y = old_y
            values.append(old_total)
        else:
            counter += 1
            values.append(new_total)

        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    # plot_graph(values, "Hill climber AmstelHaege")

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
        # print(house)

    # print(max(old_total, new_total))

    # plot_map(ax, fig)

    return [houses, values]

def simulated_annealing(houses, iterations):

    old_total = 0
    for house in houses:
        old_total = old_total + house.total_price

    temperature = 0.3 * old_total

    values = []
    counter = 0

    while counter < iterations:
        # generates random house number to move
        house_number = random.randrange(0, len(houses), 1)

        old_x = houses[house_number].x
        old_y = houses[house_number].y

        old_total = 0
        for house in houses:
            old_total = old_total + house.total_price

        if len(values) == 0:
            values.append(old_total)

        # create random x and y
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)

        houses[house_number].x = new_x
        houses[house_number].y = new_y

        all_positive = True

        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

        new_total = 0
        for house in houses:
            new_total = new_total + house.total_price

        if not all_positive:
            houses[house_number].x = old_x
            houses[house_number].y = old_y
        elif old_total > new_total:
            counter += 1
            reduction = (new_total - old_total) * 0.6
            temperature = temperature * 0.99
            p_acceptance = math.exp(reduction/temperature)
            random_number = random.randrange(0, 10000) / 10000
            if random_number < p_acceptance:
                values.append(new_total)
            else:
                houses[house_number].x = old_x
                houses[house_number].y = old_y
                values.append(old_total)
        else:
            counter += 1
            values.append(new_total)
            temperature = temperature * 0.99

        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    # print(values)

    # plot_graph(values, "Simulated annealing AmstelHaege")

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for house in houses:
        if house.width == 8:
            color = "blue"
        elif house.width == 10:
            color = "deeppink"
        elif house.width == 11:
            color = "gold"
        rect = patches.Rectangle((house.x, house.y), house.width, house.depth, color=color)
        ax.add_patch(rect)

    # print(max(old_total, new_total))

    # plot_map(ax, fig)

    return [houses, values]

# houses = random_start(20)
# houses = hill_climber(houses, 500)
# simulated_annealing(houses, 2000)
