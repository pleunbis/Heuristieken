from helper import *
from algorithms import *

# create start map
houses = random_start()

# run hill climber with 10 iterations
houses = hill_climber(houses, 10)

# run simulated annealing with 10 iterations
simulated_annealing(houses, 10)
