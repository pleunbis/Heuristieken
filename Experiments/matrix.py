import numpy as np

matrix = np.zeros((10, 10))

for i in range(3,6):
    for j in range(3, 6):
        matrix[i][j] = 1

matrix[7][3] = 1

print(matrix)
print(np.argwhere(matrix==0))
joe = np.argwhere(matrix==0)
for joetje in joe:
    print(joetje)

x = 0
y = 0
for i in range(10):
    for j in range(10):
        if matrix[i][j] == 0:
            x += 1
        if matrix[j][i] == 0:
            y += 1
        else:
            break
print(x, y)
