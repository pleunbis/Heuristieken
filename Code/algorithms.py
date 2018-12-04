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

# Generates a random startgrid.
def random_start(nr_houses):
    repetition = []

    # Generates one time a grid.
    for repeat in range(1):

        # Boolean keep track if house can be placed.
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

                # Place the singlefamily houses.
                for i in range(int(0.6 * nr_houses)):
                    positive = False
                    while positive == False:

                        # Create random x and y.
                        x = random.randrange(0, amstel_width, 1)
                        y = random.randrange(0, amstel_height, 1)

                        # Append to houses.
                        houses.append(Singlefamily(i, x, y, 0))

                        # Calculate freespace for singlefamily house.
                        current_house = houses[-1]
                        sf = calculate_freespace(current_house, houses)

                        # Call calculateprice to calculate the price.
                        sf.calculateprice()

                        # If houses overlap, delete this house.
                        if sf.extra_freespace < 0:
                            del houses[-1]

                        # Add house to grid.
                        else:
                            sf_data = data["houses"]["sf"]

                            # Create and show singlefamily house on grid
                            sf_rect = patches.Rectangle((sf.x, sf.y), sf_data["width"], sf_data["depth"], color="blue")
                            ax.add_patch(sf_rect)

                            # House is placed, go to the next house.
                            positive = True

                # Place the bungalows.
                for i in range(int(0.25 * nr_houses)):
                    positive = False
                    while positive == False:

                        # Create random x and y.
                        x = random.randrange(0, amstel_width, 1)
                        y = random.randrange(0, amstel_height, 1)

                        # Append to houses.
                        houses.append(Bungalow(int(i + 0.6 * nr_houses), x, y, 0))

                        # Calculate freespace for bungalow.
                        current_house = houses[-1]
                        b = calculate_freespace(current_house, houses)

                        # Calculate price.
                        b.calculateprice()

                        # If houses overlap, delete last placed house.
                        if b.extra_freespace < 0:
                            del houses[-1]
                        else:
                            b_data = data["houses"]["b"]

                            # Create and show bungalow on grid.
                            b_rect = patches.Rectangle((b.x, b.y), b_data["width"], b_data["depth"], color="deeppink")
                            ax.add_patch(b_rect)

                            # House is placed, go to next house.
                            positive = True

                # # Place the maisons.
                for i in range(int(0.15 * nr_houses)):
                    positive = False
                    while positive == False:

                        # Create random x and y.
                        x = random.randrange(0, amstel_width, 1)
                        y = random.randrange(0, amstel_height, 1)

                        # Append to houses.
                        houses.append(Maison(int(i + 0.85 * nr_houses), x, y, 0))

                        # Calculate freespace for maison.
                        current_house = houses[-1]
                        m = calculate_freespace(current_house, houses)

                        # Calculate price.
                        m.calculateprice()

                        # If house overlap, delete.
                        if m.extra_freespace < 0:
                            del houses[-1]
                        else:
                            m_data = data["houses"]["m"]

                            # Create and show maison on grid.
                            m_rect = patches.Rectangle((m.x, m.y), m_data["width"], m_data["depth"], color="gold")
                            ax.add_patch(m_rect)

                            # House is placed, go to next house.
                            positive = True

            # add water to startgrid
            add_water(houses)
            #
            # # when there is no space for water
            # if space_for_water == False:
            #     all_positive = False

            # Calculate freespace and price.
            for current_house in houses:
                calculate_freespace(current_house, houses)
                current_house.calculateprice()

                # If houses are placed on a wrong place.
                if current_house.extra_freespace < 0:
                    all_positive = False


        # Calculate total grid pice.
        total = 0
        for house in houses:
            total +=  house.total_price

        repetition.append(total)
        repetition.sort()

    # print(total)
    plot_map(ax, fig)

    return houses

# Function for Hill Climber.
def hill_climber(houses, iterations):

    # List which keeps track of the new values.
    values = []

    # Counter keeps track of good iterations.
    counter = 0

    # Loop to make sure that an iteration is always a valid one.
    while counter < iterations:

        # Take a random house from houses.
        house_number = random.randrange(0, len(houses), 1)

        # Save the x and y of the house.
        old_x = houses[house_number].x
        old_y = houses[house_number].y

        # Save old value of the total price.
        old_total = 0
        for house in houses:
            old_total +=  house.total_price

        # The first total price is always the first value.
        if len(values) == 0:
            values.append(old_total)

        # Create random  x en y for new place for the random chosen house.
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)

        # Set x en y for the random house.
        houses[house_number].x = new_x
        houses[house_number].y = new_y

        # Variable keeps track if random swap is valid.
        all_positive = True

        # Calculate if the grid is valid.
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # If the grid is not valid, start again.
            if current_house.extra_freespace < 0:
                all_positive = False

        # Calculate the new total price.
        new_total = 0
        for house in houses:
            new_total += house.total_price

        # If hte grid is not valid, swap random chosen house back to old x and y.
        if not all_positive:
            houses[house_number].x = old_x
            houses[house_number].y = old_y

        # If the grid is valid but the value is lower than old total.
        elif old_total > new_total:
            counter += 1
            houses[house_number].x = old_x
            houses[house_number].y = old_y
            values.append(old_total)
        else:

            # If grid value is higher, we have a valid iteration so add one to counter and append the new higer value to values.
            counter += 1
            values.append(new_total)

        # VERA HIER NA KIJKEN, IS DIT NOG NODIG?
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

    # print(max(old_total, new_total))
    # plot_map(ax, fig)

    return [houses, values]

# Function for Simulated Annealing.
def simulated_annealing(houses, iterations):

    # Caculate the old total.
    old_total = 0
    for house in houses:
        old_total += house.total_price

    # Define a temperature.
    temperature = 0.3 * old_total

    # List which keeps track of the new values.
    values = []

    # Counter keeps track of good iterations.
    counter = 0

    # Loop to make sure that an iteration is always a valid one.
    while counter < iterations:

        # Generates random house number to move.
        house_number = random.randrange(0, len(houses), 1)

        # Save the x and y from that house.
        old_x = houses[house_number].x
        old_y = houses[house_number].y

        # Calculate the old total_price.
        old_total = 0
        for house in houses:
            old_total += house.total_price

        # The first total price is always the first value.
        if len(values) == 0:
            values.append(old_total)

        # Create a random x and y where the random chosen house is gonna be placed.
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)

        # Set x and y from the house.
        houses[house_number].x = new_x
        houses[house_number].y = new_y

        # Variable keeps track if random swap is valid.
        all_positive = True

        # Calculate if the grid is valid.
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # If the grid is not valid, start again.
            if current_house.extra_freespace < 0:
                all_positive = False

        # Calculate new total price.
        new_total = 0
        for house in houses:
            new_total += house.total_price

        # If grid is not valid, set house back to old x and y.
        if not all_positive:
            houses[house_number].x = old_x
            houses[house_number].y = old_y

        # If old total is higher than new total, Caculate acceptence.
        elif old_total > new_total:
            counter += 1

            # Calculate reduction.
            reduction = (new_total - old_total) * 0.6

            # Caculate temperature.
            temperature = temperature * 0.99

            # Caculate acceptence.
            p_acceptance = math.exp(reduction/temperature)

            # Take a random number.
            random_number = random.randrange(0, 10000) / 10000

            # If random number is lower the acceptence, accept the swap and append new total to values.
            if random_number < p_acceptance:
                values.append(new_total)
            else:

                # Else we swap the house back to orginial x and y.
                houses[house_number].x = old_x
                houses[house_number].y = old_y

                # Append old total.
                values.append(old_total)

        # If total price is higher than old total price take the swap.
        else:
            counter += 1
            values.append(new_total)

            # Set temperatureself.
            temperature = temperature * 0.99

        # VERA wat moet hier gebeuren.
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    # print(values)
    # plot_graph(values, "Simulated annealing AmstelHaege")

    # Add to figure.
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
