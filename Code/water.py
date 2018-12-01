from freespacefast import houses

import numpy as np

matrix = np.zeros((360, 320))

print(matrix)

for house in houses:
    x = int(house.x * 2)
    y = int(house.y * 2)
    width = int(house.width * 2)
    depth = int(house.depth * 2)

    for i in range(x, x + width):
        for j in range(y, y + depth):
            matrix[i][j] = 1

print(matrix)
