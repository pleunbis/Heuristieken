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

# Create start map
houses = random_start(nr_houses)

# Run hill climber with 10 iterations
houses = hill_climber(houses, 5000)[0]

# # Run simulated annealing with 10 iterations
# simulated_annealing(houses, 10)[0]
