from termcolor import colored
import shutil

class Cell:
    def __init__(self, x, y, symb=None):
        self.x = x
        self.y = y
        self.symb = symb
    
    def __str__(self):
        return f"{self.symb} at ({self.x}, {self.y})"

    
# Y = rows
# X = cols

class Grid:
    COLOR_MAP = {
        '0': "green",
        '1': "black",
        '2': "yellow",
        '3': "blue",
        '4': "light_yellow",
    }

    def __init__(self, rows=80, cols=40, mode="fit", color_map=COLOR_MAP, grid=None):
        if mode not in ['fit', 'custom']:
            raise ValueError(f"Mode must be 'custom' or 'fit', '{mode}' is not a valid mode")
        if not self.are_positive_ints(rows, cols):
            raise ValueError("rows and cols must be a positive integer")
        if mode == "fit":
            self.cols, self.rows = shutil.get_terminal_size((cols, rows))
        elif mode == "custom":
            self.cols = cols
            self.rows = rows

        if grid == None:
            self.grid = self.gen_blank_grid(self.rows, self.cols)
        else:
            self.grid = grid

        self.cell_map = self.gen_cell_map(self.grid)

    def __str__(self): #TODO
        lines = []
        for row in self.grid:
            rendered_row = []
            for cell in row:
                color = self.COLOR_MAP.get(cell)
                if cell is None:
                        rendered = ' '
                elif color:
                    rendered = colored(str(cell), color)
                else:
                    rendered = str(cell)
                rendered_row.append(rendered)
            lines.append("".join(rendered_row))
            #TODO: ADD SPACE BETWEEN LETTERS AS CHOICE
        return "\n".join(lines)

    def show_size(self):
        print(f"Lines: {self.rows}\nColumns: {self.cols}")

    @staticmethod
    def are_positive_ints(*values):
        for value in values:
            if not isinstance(value, int) or isinstance(value, bool) or value < 1:
                return False
        return True        

    def gen_blank_grid(self, rows, cols):
        res = []
        for y in range(rows):
            for x in range(cols):
                res.append(Cell(x, y, None))
        return res
    
    def get_cell(self, x, y):
        self.check_xy_bounds(x, y)
        return self.grid[y][x]
    
    def get_all_cells(self, empty=True):
        cells = []
        for y in range(self.rows):
            for x in range(self.cols):
                symb = self.grid[y][x]
                if empty or symb is not None:
                    cells.append(Cell(x, y, symb))
        return cells
    
    def check_xy_bounds(self, cell):
        if not (0 <= cell.x < self.cols and 0 <= cell.y < self.rows):
            raise ValueError(f"x:{cell.x}, y:{cell.y} is out of bounds")
    
    def draw_cells(self, *cells):
        for cell in cells:
            self.check_xy_bounds(cell)
            self.grid[cell.y][cell.x] = cell.symb
        return self
    
    def clear(self):
        self.grid = self.gen_blank_grid(self.rows, self.cols)
        return self
    
    def redraw_frame(self, cells):
        self.clear()
        self.draw_cells(*cells)
        return self
    
    def gen_cell_map(self, grid):
        ...
        