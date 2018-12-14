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
    """Generates a random start map"""
    repetition = []

    for repeat in range(1):
        # Boolean keeps track if house can be placed.
        all_positive = False
        while all_positive is False:
            all_positive = True
            houses = []

            added_houses = add_houses(nr_houses)
            houses, waters = added_houses[0], added_houses[1]

        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # If houses are placed on a wrong place.
            if current_house.extra_freespace < 0:
                all_positive = False

        if nr_houses != 60:
            waters = add_water(houses, len(houses))

            if len(waters) == 0:
                return random_start(nr_houses)

            # Calculate the total price of the map.
            total = 0
            for house in houses:
                total += house.total_price

            repetition.append(total)
            repetition.sort()

    # create_map(houses, waters)

    return [houses, waters]


# Function for Hill Climber
def hill_climber(houses, iterations):
    plt.close("all")

    old_houses = houses
    values = []
    counter = 0

    # Loop to make sure that an iteration is always a valid one
    while counter < iterations:

        # Take a random house from houses
        house_number = random.randrange(0, len(houses), 1)

        # Save the x and y of the house
        old_x = houses[house_number].x
        old_y = houses[house_number].y

        # Save old value of the total price
        old_total = 0
        for house in houses:
            old_total += house.total_price

        # The first total price is always the first value
        if len(values) == 0:
            values.append(old_total)

        # Set x en y for the random house
        houses[house_number].x = swap_houses(houses, house_number)[0]
        houses[house_number].y = swap_houses(houses, house_number)[1]

        # Variable keeps track if random swap is valid
        all_positive = True

        # Calculate the freespace of each house in list
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # If the amount of extra freespace is negative, start again
            if current_house.extra_freespace < 0:
                all_positive = False

        # Calculate the new total price
        new_total = 0
        for house in houses:
            new_total += house.total_price

        # If the map is not valid, swap random chosen house back to old x and y
        if all_positive is false:
            houses[house_number].x = old_x
            houses[house_number].y = old_y

        # If the map is valid but the value is lower than old total
        elif old_total > new_total:
            counter += 1
            houses[house_number].x = old_x
            houses[house_number].y = old_y
            values.append(old_total)
        else:
            # If map value is higher, we have a valid iteration so add one to
            # counter and append the new higher value to values
            counter += 1
            values.append(new_total)

        # VERA HIER NA KIJKEN, IS DIT NOG NODIG?
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    waters = add_water(houses, len(houses))

    if len(waters) == 0:
        return hill_climber(old_houses, iterations)

    # create_map(houses, waters)

    return [houses, values, waters]


# Function for Simulated Annealing.
def simulated_annealing(houses, iterations):

    old_houses = houses

    # Calculate the old total.
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

        # Set x and y from the house.
        houses[house_number].x = swap_houses(houses, house_number)[0]
        houses[house_number].y = swap_houses(houses, house_number)[1]

        # Variable keeps track if random swap is valid.
        all_positive = True

        # Calculate the freespace of each house in list.
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # If the amount of extra freespace is negative, start again.
            if current_house.extra_freespace < 0:
                all_positive = False

        # Calculate new total price.
        new_total = 0
        for house in houses:
            new_total += house.total_price

        # If map is not valid, set house back to old x and y.
        if all_positive is false:
            houses[house_number].x = old_x
            houses[house_number].y = old_y

        # If old total is higher than new total, calculate acceptance.
        elif old_total > new_total:
            counter += 1

            # Calculate reduction.
            reduction = (new_total - old_total) * 0.6

            # Calculate temperature.
            temperature = temperature * 0.99

            # Calculate acceptance.
            p_acceptance = math.exp(reduction/temperature)

            # Take a random number.
            random_number = random.randrange(0, 10000) / 10000

            # If random number is lower the acceptance, accept the swap and
            # append new total to values.
            if random_number < p_acceptance:
                values.append(new_total)
            else:
                # Swap the house back to original x and y.
                houses[house_number].x = old_x
                houses[house_number].y = old_y

                # Append old total.
                values.append(old_total)

        # If total price is higher than old total price take the swap.
        else:
            counter += 1
            values.append(new_total)

            # Set temperature.
            temperature = temperature * 0.99

        # VERA wat moet hier gebeuren.
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    waters = add_water(houses, len(houses))

    if len(waters) == 0:
        return simulated_annealing(old_houses, iterations)

    # create_map(houses, waters)

    return [houses, values, waters]
