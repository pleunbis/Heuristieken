from classes import *
from helper import *
import math
import matplotlib.pyplot as plt
import random


def random_start(nr_houses):
    """Generates a random start map"""
    total = 0

    # all_positive keeps track if house can be placed
    all_positive = False
    while all_positive is False:
        all_positive = True
        houses = []

        added_houses = add_houses(nr_houses, all_positive)

        # stores information from add_houses function in correct variables
        houses, waters = added_houses[0], added_houses[1]
        all_positive = added_houses[2]

        # calculates freespace
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # checks if the freespace is satisfactory
            if current_house.extra_freespace < 0:
                all_positive = False

    # adds water for 20/40 variant
    if nr_houses != 60:
        waters = add_water(houses, len(houses))

        # if adding water was not possible, execute random_start function
        if len(waters) == 0:
            return random_start(nr_houses)

    # calculate the total price of the map
    total = 0
    for house in houses:
        total += house.total_price

    # creates map of random start solution
    create_map(houses, waters)

    return [houses, waters, total]


def hill_climber(houses, iterations):
    """This function executes the hill climber algorithm"""
    plt.close("all")

    old_houses = houses
    values = []
    counter = 0

    # loops until requested number of iterations is done
    while counter < iterations:

        # picks a random house to swap
        house_number = random.randrange(0, len(houses), 1)

        old_x = houses[house_number].x
        old_y = houses[house_number].y

        # calculates the price of the old map
        old_total = 0
        for house in houses:
            old_total += house.total_price

        # adds price of random start map to values list
        if len(values) == 0:
            values.append(old_total)

        # sets random x and y for the random house
        houses[house_number].x = swap_houses(houses, house_number)[0]
        houses[house_number].y = swap_houses(houses, house_number)[1]

        all_positive = True

        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # checks if the required freespace is met
            if current_house.extra_freespace < 0:
                all_positive = False

        new_total = 0
        for house in houses:
            new_total += house.total_price

        # undo the swap, if it's not valid
        if all_positive is False:
            houses[house_number].x = old_x
            houses[house_number].y = old_y
        # undo the swap, if the new value is worse than the old value
        elif old_total > new_total:
            counter += 1
            houses[house_number].x = old_x
            houses[house_number].y = old_y
            values.append(old_total)
        else:
            counter += 1
            values.append(new_total)

        # calculates the freespace again, so it's stored properly
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    waters = add_water(houses, len(houses))

    # if adding water was not possible, execute the hill_climber function again
    if len(waters) == 0:
        return hill_climber(old_houses, iterations)

    # creates map of final solution
    create_map(houses, waters)

    return [houses, values, waters]


def simulated_annealing(houses, iterations):
    """This function executes the simulated annealing algorithm"""

    old_houses = houses

    # calculates the price of the old map
    old_total = 0
    for house in houses:
        old_total += house.total_price

    # defines the initial temperature
    temperature = 0.3 * old_total

    values = []
    counter = 0

    # loops until requested number of iterations is done
    while counter < iterations:

        # picks a random house to swap
        house_number = random.randrange(0, len(houses), 1)

        old_x = houses[house_number].x
        old_y = houses[house_number].y

        # calculates the price of the old map
        old_total = 0
        for house in houses:
            old_total += house.total_price

        # adds price of random start map to values list
        if len(values) == 0:
            values.append(old_total)

        # sets random x and y for the random house
        houses[house_number].x = swap_houses(houses, house_number)[0]
        houses[house_number].y = swap_houses(houses, house_number)[1]

        all_positive = True

        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # checks if the required freespace is met
            if current_house.extra_freespace < 0:
                all_positive = False

        new_total = 0
        for house in houses:
            new_total += house.total_price

        # undo the swap, if it's not valid
        if all_positive is False:
            houses[house_number].x = old_x
            houses[house_number].y = old_y

        # if old value is higher than the new, calculate acceptance probability
        elif old_total > new_total:
            counter += 1

            reduction = (new_total - old_total) * 0.6

            temperature = temperature * 0.99

            # calculates acceptance propability
            p_acceptance = math.exp(reduction/temperature)

            random_number = random.randrange(0, 10000) / 10000

            # check if new map is accepted
            if random_number < p_acceptance:
                values.append(new_total)
            else:
                # undo the swap
                houses[house_number].x = old_x
                houses[house_number].y = old_y
                values.append(old_total)
        # if new price is higher, swap is accepted
        else:
            counter += 1
            values.append(new_total)

            # new temperature is calculated
            temperature = temperature * 0.99

        # calculates the freespace again, so it's stored properly
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    waters = add_water(houses, len(houses))

    # if water was not possible, execute the simulated_annealing function again
    if len(waters) == 0:
        return simulated_annealing(old_houses, iterations)

    # creates map of final solution
    create_map(houses, waters)

    return [houses, values, waters]
