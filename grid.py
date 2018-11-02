import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import colors
import matplotlib
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)
rect1 = matplotlib.patches.Rectangle((0, 0), 3, 2, color='yellow')
ax.add_patch(rect1)

plt.ylim(0, 180)
plt.xlim(0, 160)

major_xticks = np.arange(0, 160, 1)
# minor_xticks = np.arange(0, 160, 1)
major_yticks = np.arange(0, 180, 1)
# minor_yticks = np.arange(0, 180, 1)

plt.xticks(major_xticks)
# plt.xticks(minor_xticks, minor=True)
plt.yticks(major_yticks)
# plt.yticks(minor_yticks, minor=True)

plt.title("Plattegrond AmstelHaege")
plt.grid()
plt.show()
