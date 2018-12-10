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
        while all_positive == False:
            all_positive = True
            plt.close("all")
            # fig = plt.figure()
            # ax = fig.add_subplot(111)
            Paste_house = True

            waters = []
            waters.append(Water( 0, 0 , 72 , 80))

            while Paste_house == True:
                Paste_house = False
                houses = []
                if nr_houses == 60:

                    print("joe")
                    # Add the singlefamily houses.
                    for i in range(int(0.6 * nr_houses)):
                        positive = False
                        while positive == False:

                            # Create random x and y.
                            x = random.randrange(72, amstel_width, 1)
                            if x < 72:
                                y = random.randrange(80, amstel_height, 1)
                            else:
                                y = random.randrange(0, amstel_height, 1)
                            # print(x,y)


                            # Append to houses.
                            houses.append(Singlefamily(i, x, y, 0))

                            # Calculate freespace for singlefamily house.
                            current_house = houses[-1]
                            sf = calculate_freespace(current_house, houses)

                            # Call calculateprice to calculate the price.
                            sf.calculateprice()

                            # If houses overlap, delete this house from list.
                            if sf.extra_freespace < 0:
                                del houses[-1]
                                # print("joe")
                            else:
                                # House is added, go to the next house.
                                positive = True
                                print("geplaatst")

                    # Add the bungalows.
                    for i in range(int(0.25 * nr_houses)):
                        positive = False
                        while positive == False:

                            # Create random x and y.
                            x = random.randrange(72, amstel_width, 1)
                            if x < 72:
                                y = random.randrange(80, amstel_height, 1)
                            else:
                                y = random.randrange(0, amstel_height, 1)

                            # Append to houses.
                            houses.append(Bungalow(int(i + 0.6 * nr_houses), x, y, 0))

                            # Calculate freespace for bungalow.
                            current_house = houses[-1]
                            bgl = calculate_freespace(current_house, houses)

                            # Calculate price.
                            bgl.calculateprice()

                            # If houses overlap, delete this house from list.
                            if bgl.extra_freespace < 0:
                                del houses[-1]
                                # print("joe")
                            else:
                                # House is added, go to next house.
                                positive = True
                                print("geplaatst")


                    # Add the maisons.
                    for i in range(int(0.15 * nr_houses)):
                        positive = False
                        while positive == False:

                            # Create random x and y.
                            x = random.randrange(72, amstel_width, 1)
                            if x < 72:
                                y = random.randrange(80, amstel_height, 1)
                            else:
                                y = random.randrange(0, amstel_height, 1)
                            # print(x,y)
                            # Append to houses.
                            houses.append(Maison(int(i + 0.85 * nr_houses), x, y, 0))

                            # Calculate freespace for maison.
                            current_house = houses[-1]
                            ms = calculate_freespace(current_house, houses)

                            # Calculate price.
                            ms.calculateprice()

                            # If houses overlap, delete this house from list.
                            if ms.extra_freespace < 0:
                                del houses[-1]
                                # print("joe")

                            else:
                                # House is added, go to next house.
                                positive = True
                                print("geplaatst")

                else:
                    print('klopt niet')
                    # Add the singlefamily houses.
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

                            # If houses overlap, delete this house from list.
                            if sf.extra_freespace < 0:
                                del houses[-1]
                            else:
                                # House is added, go to the next house.
                                positive = True

                    # Add the bungalows.
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
                            bgl = calculate_freespace(current_house, houses)

                            # Calculate price.
                            bgl.calculateprice()

                            # If houses overlap, delete this house from list.
                            if bgl.extra_freespace < 0:
                                del houses[-1]
                            else:
                                # House is added, go to next house.
                                positive = True

                    # Add the maisons.
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
                            ms = calculate_freespace(current_house, houses)

                            # Calculate price.
                            ms.calculateprice()

                            # If houses overlap, delete this house from list.
                            if ms.extra_freespace < 0:
                                del houses[-1]
                            else:
                                # House is added, go to next house.
                                positive = True



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

        if nr_houses == 60:

            print("60 huizen variant")
        else:

            # Add water
            waters = add_water(houses)

            if len(waters) == 0:
                random_start(nr_houses)

            # Calculate the total price of the map.
            total = 0
            for house in houses:
                total += house.total_price

            repetition.append(total)
            repetition.sort()

    # print(total)

        create_map(houses, waters)

    return houses

# Function for Hill Climber
def hill_climber(houses, iterations):

    plt.close("all")
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

        # Create random x en y for new place for the random chosen house.
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)

        # Set x en y for the random house.
        houses[house_number].x = new_x
        houses[house_number].y = new_y

        # Variable keeps track if random swap is valid.
        all_positive = True

        # Calculate the freespace of each house in list.
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()

            # If the amount of extra freespace is negative, start again.
            if current_house.extra_freespace < 0:
                all_positive = False

        # Calculate the new total price.
        new_total = 0
        for house in houses:
            new_total += house.total_price

        # If the map is not valid, swap random chosen house back to old x and y.
        if not all_positive:
            houses[house_number].x = old_x
            houses[house_number].y = old_y

        # If the map is valid but the value is lower than old total.
        elif old_total > new_total:
            counter += 1
            houses[house_number].x = old_x
            houses[house_number].y = old_y
            values.append(old_total)
        else:
            # If map value is higher, we have a valid iteration so add one to counter and append the new higher value to values.
            counter += 1
            values.append(new_total)

        # print(max(old_total, new_total))



        # VERA HIER NA KIJKEN, IS DIT NOG NODIG?
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    waters = add_water(houses)

    create_map(houses, waters)

    return [houses, values]

# Function for Simulated Annealing.
def simulated_annealing(houses, iterations):

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

        # Create a random x and y where the random house is going to be placed.
        new_x = random.randrange(0, amstel_width, 1)
        new_y = random.randrange(0, amstel_height, 1)

        # Set x and y from the house.
        houses[house_number].x = new_x
        houses[house_number].y = new_y

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
        if not all_positive:
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

            # If random number is lower the acceptance, accept the swap and append new total to values.
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

        # print(max(old_total, new_total))

            # Set temperature.
            temperature = temperature * 0.99



        # VERA wat moet hier gebeuren.
        for current_house in houses:
            calculate_freespace(current_house, houses)
            current_house.calculateprice()
            if current_house.extra_freespace < 0:
                all_positive = False

    # print(values)
    waters = add_water(houses)

    create_map(houses, waters)

    return [houses, values]

# houses = random_start(20)
# houses = hill_climber(houses, 500)
# simulated_annealing(houses, 2000)
