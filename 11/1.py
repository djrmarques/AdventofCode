import pandas as pd
import numpy as np

def powerlevel(x, y, inp=6042):
    ''' Calculate the power level of a cell '''
    # Find the fuel cell's rack ID, which is its X coordinate plus 10.
    rackid = x + 10
    # Begin with a power level of the rack ID times the Y coordinate.
    power  = rackid * y
    # Increase the power level by the value of the grid serial number (your puzzle input).
    power  += inp
    # Set the power level to itself multiplied by the rack ID.
    power  = power * rackid
    # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    # Subtract 5 from the power level.
    power = power // 100 % 10

    return power - 5

grid_size, inp = 300, 6042

grid = np.fromfunction(powerlevel, (300, 300))

def search3x3(grid, grid_size):
    maxp = 0

    for size_cell in range(1, grid_size + 1):
        print(size_cell)
        for i in range(size_cell, grid_size+1):
            for j in range(size_cell, grid_size+1):
                power_level = grid[i-size_cell:i, j-size_cell:j].sum()
                if power_level > maxp:
                    maxp = power_level
                    max_coords = i-size_cell, j-size_cell
                    max_size = size_cell

    return maxp, max_coords, max_size

search3x3(grid, grid_size)
