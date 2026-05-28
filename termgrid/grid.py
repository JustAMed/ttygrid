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

    def __init__(self, rows=80, cols=40, mode="fit", grid=None):
        if mode not in ['fit', 'custom']:
            raise ValueError(f"Mode must be 'custom' or 'fit', '{mode}' is not a valid mode")
        if not self.are_positive_ints(rows, cols):
            raise ValueError("rows and cols must be a positive integer")
        if mode == "fit":
            self.cols, self.rows = shutil.get_terminal_size((cols, rows))
        elif mode == "custom":
            self.cols = cols
            self.rows = rows
        
        self.cell_map = self.gen_cell_map(self.rows, self.cols, grid)

    def get_color(self, symb):
        return self.COLOR_MAP.get(symb)

    def __str__(self): #TODO
        lines = []
        for y in range(self.rows):
            line = []
            for x in range(self.cols):
                cell = self.cell_map[(x, y)]
                color = self.get_color(cell.symb)
                if color:
                    line.append(colored(cell.symb, color))
                else:
                    line.append(cell.symb or " ")
            lines.append("".join(line))
        return "\n".join(lines)
                                

    def show_size(self):
        print(f"Lines: {self.rows}\nColumns: {self.cols}")

    @staticmethod
    def clear_term():
        print("\033[H\033[J", end="")

    @staticmethod
    def are_positive_ints(*values):
        for value in values:
            if not isinstance(value, int) or isinstance(value, bool) or value < 1:
                return False
        return True        

    def get_cell(self, x, y):
        if (x, y) not in self.cell_map:
            raise ValueError(f"x:{x}, y:{y} is out of bounds")
        return self.cell_map[(x, y)]
    
    def validate_cell(self, cell):
        if (cell.x, cell.y) not in self.cell_map:
            raise ValueError(f"x:{cell.x}, y:{cell.y} is out of bounds")

    def get_all_cells(self, empty=True):
        cells = []
        for y in range(self.rows):
            for x in range(self.cols):
                cell = self.cell_map[(x, y)]
                if empty or cell.symb is not None:
                    cells.append(cell)
        return cells
    
    def draw_cells(self, *cells):
        for cell in cells:
            self.validate_cell(cell)
            self.cell_map[(cell.x, cell.y)] = cell
        return self
    
    def clear(self):
        self.cell_map = self.gen_cell_map(self.rows, self.cols, None)
        return self
    
    def redraw_frame(self, cell_map):
        self.cell_map = cell_map
        return self
    
    def gen_cell_map(self, rows, cols, grid=None):
        if grid is not None:
            return grid
        
        cell_map = {}
        for y in range(rows):
            for x in range(cols):
                cell_map[(x, y)] = Cell(x, y, None)

        return cell_map