from helper import *
from algorithms import *
import sys

# checks if there is 1 command-line argument
if len(sys.argv) != 2:
    print("Usage: python main.py k")
    sys.exit(1)
elif sys.argv[1] not in ["20", "40", "60"]:
    print("Number of houses must be 20, 40 or 60")
    sys.exit()

nr_houses = int(sys.argv[1])

alle_hill = []

for i in range(500):
    print(i)
    # create start map
    houses = random_start(nr_houses)
    # run hill climber with 10 iterations
    info = hill_climber(houses, 1000)
    houses, values = info[0], info[1]
    # values += simulated_annealing(houses, 650)[1]

    # alle_hill.append(values)

# print(alle_hill)

plot_graph(values, "joe")

# final_values = []
#
# gem_hill = [0] * 1002
#
# for hill in alle_hill:
#     final_values.append(hill[-1])
#     for i in range(len(hill)):
#         gem_hill[i] += hill[i] / 500
#
# print(gem_hill)
# print(final_values)
# run simulated annealing with 10 iterations
# simulated_annealing(houses, 10)
#
# with open('Results/average_simhill500.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for item in gem_hill:
#         writer.writerows([[item]])
#
# with open('Results/final_simhill500.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for item in final_values:
#         writer.writerows([[item]])
