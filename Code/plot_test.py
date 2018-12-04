from statistics import mean
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import csv
from helper import plot_graph

final_values = []

with open('Results/final_simhill500.csv', 'r') as f:
  reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
  for row in reader:
  	final_values.append(row[0])

print("mean: ", mean(final_values))
print("max: ", max(final_values))
print("min: ", min(final_values))

def millions(x, pos):
    return '%3i' % (x*1e-6)

formatter = FuncFormatter(millions)

bins=[13000000, 13100000, 13200000, 13300000, 13400000, 13500000, 13600000, 13700000, 13800000, 13900000, 14000000, 14100000, 14200000, 14300000, 14400000, 14500000, 14600000, 14700000, 14800000, 14900000, 15000000, 15100000, 15200000, 15300000, 15400000, 15500000, 15600000, 15700000, 15800000, 15900000, 16000000, 16100000]

fig, ax = plt.subplots()
plt.hist(final_values, bins, rwidth=0.88)
plt.title("Final values hill climber -> simulated annealing")
ax.xaxis.set_major_formatter(formatter)
plt.xlabel("Value in millions")
plt.ylabel("Frequency")
plt.show()
# plt.savefig("randomwalk.png")

average_hillclimber = []
with open('Results/average_simhill500.csv', 'r') as f:
  reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
  for row in reader:
  	average_hillclimber.append(row[0])

plot_graph(average_hillclimber, "Average hill climber -> simulated annealing")
