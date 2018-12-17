import sys
import time
from algorithms import *
from helper import *

# usage:
# main.py number of houses, algorithm, number of runs, number of iterations

# start to hold the time
start = time.time()

# check if there are 3 command-line arguments
if len(sys.argv) < 3:
    print("Choose the number of houses and the algorithm")
    sys.exit(1)
elif len(sys.argv) > 6:
    print("Too many arguments")
    sys.exit(1)

# check for valid number of houses
elif sys.argv[1] not in ["20", "40", "60"]:
    print("Number of houses must be 20, 40 or 60")
    sys.exit()

# check for valid algorithm
elif sys.argv[2] not in ["random", "simulated_annealing", "hill_climber",
                         "hill_climber+simulated_annealing"]:
    print("Algorithm does not exist")
    sys.exit()

elif sys.argv[2] != "random":
    # check for valid number of iterations and runs
    if len(sys.argv) < 5:
        print("Fill in runs or and iterations")
        sys.exit()
    
    # simulated annealing
    elif sys.argv[2] == "hill_climber+simulated_annealing":
        if len(sys.argv) < 6:
            print("Fill in iterations for both hill climber" +
                  "and simulated annealing")
            sys.exit()
        else:
            iterations1 = int(sys.argv[5])
    
    runs = int(sys.argv[3])
    iterations = int(sys.argv[4])

elif sys.argv[2] == "random":
    if len(sys.argv) > 3:
        print("Too many arguments for random algorithm")
        sys.exit()

# set variables
nr_houses = int(sys.argv[1])
algorithm = sys.argv[2]

# if random is chosen
if algorithm == "random":
    random_start(nr_houses)

# if simulated_annealing is chosen
elif algorithm == "simulated_annealing":
    all_sa = []
    maximum = 0
    maximum_houses = []
    maximum_waters = []
    maximum_values = []
    final_values = []

    for i in range(runs):
        print(i)
        houses = random_start(nr_houses)[0]
        info = simulated_annealing(houses, iterations)
        houses = info[0]

        total = 0
        for house in houses:
            total += house.total_price

        values = info[1]
        waters = info[2]

        if total > maximum:
            maximum = total
            maximum_houses = houses
            maximum_waters = waters
            maximum_values = values

        all_sa.append(values)
    
    total = 0

    # average simulated annealing
    av_sa = [0] * (iterations + 1)

    for sa in all_sa:
        final_values.append(sa[-1])
        for i in range(len(sa)):
            av_sa[i] += sa[i] / runs

    end = time.time()
    print(end - start)
    print(maximum)
    
    # print id, coordinates, freespace and value of each house on final map
    for house in maximum_houses:
        print(house)
    
    create_map(maximum_houses, maximum_waters)
    plot_graph(maximum_values, "Simulated Annealing")
    plot_graph(av_sa, "Average Simulated Annealing")

    with open('a20_average_sa_500_5000.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in av_sa:
            writer.writerows([[item]])

    with open('a20_sa_500_5000.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in final_values:
            writer.writerows([[item]])

# if hill climber is chosen
elif algorithm == "hill_climber":

    all_hill = []
    maximum = 0
    maximum_houses = []
    maximum_waters = []
    maximum_values = []
    final_values = []

    for i in range(runs):
        print(i)
        houses = random_start(nr_houses)[0]
        info = hill_climber(houses, iterations)
        houses = info[0]
        total = 0
        for house in houses:
            total += house.total_price

        values = info[1]
        waters = info[2]

        if total > maximum:
            maximum = total
            maximum_houses = houses
            maximum_waters = waters
            maximum_values = values
        all_hill.append(values)
    
    total = 0

    # average hill climber
    av_hill = [0] * (iterations + 1)

    for hill in all_hill:
        final_values.append(hill[-1])
        for i in range(len(hill)):
            av_hill[i] += hill[i] / runs

    end = time.time()
    print(end - start)
    print(maximum)
    
    # print id, coordinates, freespace and value of each house on final map
    for house in maximum_houses:
        print(house)
    
    create_map(maximum_houses, maximum_waters)
    plot_graph(maximum_values, "Hill Climber")
    plot_graph(av_hill, "Average Hill Climber")

    with open('a20_average_hill_500_5000.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in av_hill:
            writer.writerows([[item]])

    with open('a20_hill_500_5000.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in final_values:
            writer.writerows([[item]])

# if combination of hill climber and simulated annealing is chosen
elif algorithm == "hill_climber+simulated_annealing":

    all_hill_sa = []
    maximum = 0
    maximum_houses = []
    maximum_values = []
    maximum_waters = []
    final_values = []

    for i in range(runs):
        print(i)
        houses = random_start(nr_houses)[0]

        info = hill_climber(houses, iterations)

        houses = info[0]
        values = info[1]

        info = simulated_annealing(houses, iterations1)
        values += info[1]

        houses = info[0]
        waters = info[2]

        total = 0
        for house in houses:
            total += house.total_price

        if total > maximum:
            maximum = total
            maximum_houses = houses
            maximum_waters = waters
            maximum_values = values

        all_hill_sa.append(values)

    total = 0

    # average hill climber + simulated annealing
    av_hill_sa = [0] * (iterations1 + iterations + 2)

    for hill_sa in all_hill_sa:
        final_values.append(hill_sa[-1])
        for i in range(len(hill_sa)):
            av_hill_sa[i] += hill_sa[i] / runs

    end = time.time()
    print(end - start)
    print(maximum)
    
    # print id, coordinates, freespace and value of each house on final map
    for house in maximum_houses:
        print(house)
    
    create_map(maximum_houses, maximum_waters)
    plot_graph(maximum_values, "Hill Climber + Simulated Annealing")
    plot_graph(av_hill_sa, "Average Hill Climber + Simulated Annealing")


    # write values to csv file
    with open('a20_average_hill_sa_500_5000.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in av_hill_sa:
            writer.writerows([[item]])

    with open('a20_hill_sa_500_5000.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in final_values:
            writer.writerows([[item]])
