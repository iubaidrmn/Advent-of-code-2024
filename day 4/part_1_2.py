import re
import numpy as np

lines = []

with open('input.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

# Part 1
def find_horizontal():
    n = 0
    for x in lines:
        n += len(re.findall(r'XMAS', x))
        n += len(re.findall(r'SAMX', x))
    return n

def find_vertical():
    grid = []
    n = 0
    for x in lines:
        grid.append(list(x))
    np_grid = np.array(grid)
    new_grid = np_grid.transpose()
    for x in new_grid:
        n += len(re.findall(r'XMAS', ''.join(x)))
        n += len(re.findall(r'SAMX', ''.join(x)))
    return n

def find_diagonal():
    def get_diagonals_2d(arr):
        rows = len(arr)
        cols = len(arr[0])
        diagonals = []
        
        for i in range(rows + cols - 1):
            diagonal = []
            for row in range(max(0, i - cols + 1), min(i + 1, rows)):
                col = i - row
                diagonal.append(arr[row][col])
            diagonals.append(diagonal)

        for i in range(rows + cols - 1):
            diagonal = []
            for row in range(max(0, i - cols + 1), min(i + 1, rows)):
                col = cols - 1 - (i - row)
                diagonal.append(arr[row][col])
            diagonals.append(diagonal)
        
        return diagonals
    
    grid = []
    n = 0
    for x in lines:
        grid.append(list(x))
    
    for x in get_diagonals_2d(grid):
        n += len(re.findall(r'XMAS', ''.join(x)))
        n += len(re.findall(r'SAMX', ''.join(x)))
    
    return n

total1 = find_horizontal() + find_vertical() + find_diagonal()
print("Total 1: " + str(total1))

# Part 2
total2 = 0
grid = []
for x in lines:
    grid.append(list(x))

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] == 'A':
            if (
                (grid[i - 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'S')
                or 
                (grid[i - 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S')
                or 
                (grid[i - 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'M') 
                or 
                (grid[i - 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M')
                ):
                total2 += 1

print("Total 2: " + str(total2))