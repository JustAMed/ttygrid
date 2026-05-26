import random
import os
import time
from termgrid import Cell, Grid
from termcolor import colored

def main():
    grid = Grid()
    while True:
        cells = grid.get_all_cells(empty=True)
        for cell in cells:
            cell.symb = random.choice([0, 1])
            grid.draw_cells(cell)
        print(grid)
        time.sleep(0.1)

if __name__ == "__main__":
    main()