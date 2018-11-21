from statistics import mean
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import csv


random_values = []

with open('random_values.csv', 'r') as f:
  reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
  for row in reader:
  	random_values.append(row[0])

print("mean: ", mean(random_values))
print("max: ", max(random_values))
print("min: ", min(random_values))

def millions(x, pos):
    return '%1i' % (x*1e-6)

formatter = FuncFormatter(millions)

bins=[8000000, 8100000, 8200000, 8300000, 8400000, 8500000, 8600000, 8700000, 8800000, 8900000, 9000000, 9100000, 9200000, 9300000, 9400000, 9500000, 9600000, 9700000, 9800000, 9900000, 10000000, 10100000, 10200000, 10300000, 10400000, 10500000, 10600000, 10700000, 10800000, 10900000, 11000000, 11100000, 11200000, 11300000, 11400000, 11500000, 11600000, 11700000, 11800000, 11900000, 12000000, 12100000, 12200000, 12300000, 12400000, 12500000, 12600000, 12700000, 12800000, 12900000, 13000000]

fig, ax = plt.subplots()
plt.hist(random_values, bins, rwidth=0.88)
plt.title("Random walk AmstelHaege")
ax.xaxis.set_major_formatter(formatter)
plt.xlabel("Value in millions")
plt.ylabel("Frequency")
plt.show()
# plt.savefig("randomwalk.png")
