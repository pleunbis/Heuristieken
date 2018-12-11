from helper import *
from algorithms import *
import sys
import time

start = time.time()
# Check if there is 1 command-line argument
if len(sys.argv) != 2:
    print("Usage: python main.py k")
    sys.exit(1)
elif sys.argv[1] not in ["20", "40", "60"]:
    print("Number of houses must be 20, 40 or 60")
    sys.exit()

nr_houses = int(sys.argv[1])

# random_start(nr_houses)

# alle_sa = []
# maximum = 0
# maximum_houses = []
# maximum_waters = []
# maximum_values = []
# final_values = []
# # Create start map Simulated Annealing
# runs = 2
# iterations = 250
# for i in range(runs):
#     houses = random_start(nr_houses)[0]
#     # Run sa climber with 10 iterations
#     # info = sa_climber(houses, 500)
#     info = simulated_annealing(houses, iterations)
#     houses = info[0]
#
#     total = 0
#     for house in houses:
#         total += house.total_price
#
#     waters = info[2]
#     values = info[1]
#
#     if total > maximum:
#         maximum = total
#         maximum_houses = houses
#         maximum_waters = waters
#         maximum_values = values
#
#     alle_sa.append(values)
# total = 0
#
# gem_sa = [0] * (iterations + 1)
#
# for sa in alle_sa:
#     final_values.append(sa[-1])
#     for i in range(len(sa)):
#         gem_sa[i] += sa[i] / runs
#
# end = time.time()
# print(end - start)
# print(maximum)
# for house in maximum_houses:
#     print(house)
# create_map(maximum_houses, maximum_waters)
# plot_graph(maximum_values, "Simulated Annealing")
# plot_graph(gem_sa, "Average Simulated Annealing")
#
alle_hill = []
maximum = 0
maximum_houses = []
maximum_waters = []
maximum_values = []
final_values = []
# Create start map Simulated Annealing
runs = 2
iterations = 250
for i in range(runs):
    houses = random_start(nr_houses)[0]
    # Run hill climber with 10 iterations
    info = hill_climber(houses, iterations)
    # info = simulated_annealing(houses, iterations)
    houses = info[0]
    total = 0
    for house in houses:
        total += house.total_price

    waters = info[2]
    values = info[1]

    if total > maximum:
        maximum = total
        maximum_houses = houses
        maximum_waters = waters
        maximum_values = values
    alle_hill.append(values)
total = 0

gem_hill = [0] * (iterations + 1)

for hill in alle_hill:
    final_values.append(hill[-1])
    for i in range(len(hill)):
        gem_hill[i] += hill[i] / runs

# for house in houses:
#     total += house.total_price
end = time.time()
print(end - start)
print(maximum)
for house in maximum_houses:
    print(house)
create_map(maximum_houses, maximum_waters)
plot_graph(maximum_values, "Hill Climber")
plot_graph(gem_hill, "Average Hill Climber")

# alle_hill_sa = []
# maximum = 0
# maximum_houses = []
# maximum_values = []
# maximum_waters = []
# final_values = []
# # Create start map Simulated Annealing
# runs = 2
# iterations = 250
# for i in range(runs):
#     houses = random_start(nr_houses)[0]
#     # Run hill climber with 10 iterations
#     info = hill_climber(houses, iterations)
#     # info = simulated_annealing(houses, iterations)
#     houses = info[0]
#     values = info[1]
#
#     info = simulated_annealing(houses, iterations)
#     values += info[1]
#
#     houses = info[0]
#     waters = info[2]
#
#     total = 0
#     for house in houses:
#         total += house.total_price
#
#     if total > maximum:
#         maximum = total
#         maximum_houses = houses
#         maximum_waters = waters
#         maximum_values = values
#
#     alle_hill_sa.append(values)
#
# total = 0
#
# gem_hill_sa = [0] * (iterations * 2 + 2)
#
# for hill_sa in alle_hill_sa:
#     final_values.append(hill_sa[-1])
#     for i in range(len(hill_sa)):
#         gem_hill_sa[i] += hill_sa[i] / runs
#
# end = time.time()
# print(end - start)
# print(maximum)
# for house in maximum_houses:
#     print(house)
# create_map(maximum_houses, maximum_waters)
# plot_graph(maximum_values, "Hill Climber + Simulated Annealing")
# plot_graph(gem_hill_sa, "Average Hill Climber + Simulated Annealing")
#
#
# with open('Results/Hillclimber + simulated annealing/Data/average_hill_sa_2_250.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for item in gem_hill_sa:
#         writer.writerows([[item]])
#
# with open('Results/Hillclimber + simulated annealing/Data/final_hill_sa_2_250.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     for item in final_values:
#         writer.writerows([[item]])





# Run sa climber with 10 iterations
# houses = sa_climber(houses, 500)[0]

# # Run simulated annealing with 10 iterations
# simulated_annealing(houses, 10)[0]
