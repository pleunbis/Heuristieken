from helper import *
from algorithms import *
import sys

# Check if there is 1 command-line argument
if len(sys.argv) != 2:
    print("Usage: python main.py k")
    sys.exit(1)
elif sys.argv[1] not in ["20", "40", "60"]:
    print("Number of houses must be 20, 40 or 60")
    sys.exit()

nr_houses = int(sys.argv[1])

# alle_sa = []
# # Create start map Simulated Annealing
# runs = 1
# iterations = 500
# for i in range(runs):
#     houses = random_start(nr_houses)[0]
#     # Run sa climber with 10 iterations
#     # info = sa_climber(houses, 500)
#     info = simulated_annealing(houses, iterations)
#     houses = info[0]
#
#     for house in houses:
#         print(house)
#     waters = info[2]
#     values = info[1]
#     alle_sa.append(values)
# total = 0
#
# gem_sa = [0] * (iterations + 1)
#
# for sa in alle_sa:
#     # final_values.append(sa[-1])
#     for i in range(len(sa)):
#         gem_sa[i] += sa[i] / runs
#
# for house in houses:
#     total += house.total_price
# print(total)
# create_map(houses, waters)
# plot_graph(values, "Simulated Annealing")
# plot_graph(gem_sa, "Average Simulated Annealing")

# alle_hill = []
# # Create start map Simulated Annealing
# runs = 1
# iterations = 500
# for i in range(runs):
#     houses = random_start(nr_houses)[0]
#     # Run hill climber with 10 iterations
#     info = hill_climber(houses, 500)
#     # info = simulated_annealing(houses, iterations)
#     houses = info[0]
#
#     for house in houses:
#         print(house)
#     waters = info[2]
#     values = info[1]
#     alle_hill.append(values)
# total = 0
#
# gem_hill = [0] * (iterations + 1)
#
# for hill in alle_hill:
#     # final_values.append(hill[-1])
#     for i in range(len(hill)):
#         gem_hill[i] += hill[i] / runs
#
# for house in houses:
#     total += house.total_price
# print(total)
# create_map(houses, waters)
# plot_graph(values, "Hill Climber")
# plot_graph(gem_hill, "Average Hill Climber")

alle_hill_sa = []
# Create start map Simulated Annealing
runs = 1
iterations = 500
for i in range(runs):
    houses = random_start(nr_houses)[0]
    # Run hill climber with 10 iterations
    info = hill_climber(houses, iterations)
    # info = simulated_annealing(houses, iterations)
    houses = info[0]
    values = info[1]

    info = simulated_annealing(houses, iterations)
    values += info[1]

    for house in houses:
        print(house)
    waters = info[2]

    alle_hill_sa.append(values)

total = 0
# print(alle_hill_sa)
# print(len(alle_hill_sa))

gem_hill_sa = [0] * (iterations * 2 + 2)

for hill_sa in alle_hill_sa:

    # print(alle_hill_sa)
    print(len(hill_sa))
    print(len(gem_hill_sa))

    # final_values.append(hill_sa[-1])
    for i in range(len(hill_sa)):
        gem_hill_sa[i] += hill_sa[i] / runs

for house in houses:
    total += house.total_price
print(total)
create_map(houses, waters)
plot_graph(values, "Hill Climber + Simulated Annealing")
plot_graph(gem_hill_sa, "Average Hill Climber + Simulated Annealing")





# Run sa climber with 10 iterations
# houses = sa_climber(houses, 500)[0]

# # Run simulated annealing with 10 iterations
# simulated_annealing(houses, 10)[0]
