from termcolor import colored
import shutil

class Grid:
    COLOR_MAP = {
        0: "green",
        1: "red",
    }

    def __init__(self, rows=None, cols=None, mode="fit"):
        if mode != "fit" and (rows == None or cols == None):
            raise ValueError("Specify rows and columns if mode is custom")
        #TODO: ADD CUSTOM MODE
        if mode == "fit":
            self.cols, self.rows = shutil.get_terminal_size((40, 80))
        else:
            self.cols = cols
            self.rows = rows
        #TODO: ADD VALIDATION
        self.grid = self.gen_grid(self.rows, self.cols)

    def __str__(self):
        lines = []
        for row in self.grid:
            rendered_row = []
            for cell in row:
                color = self.COLOR_MAP.get(cell)
                if color:
                    rendered = colored(str(cell), color)
                else:
                    rendered = str(cell)
                rendered_row.append(rendered)
            lines.append("".join(rendered_row))
            #TODO: ADD SPACE BETWEEN LETTERS AS CHOICE
        return "\n".join(lines)

    def gen_blank_grid(self, rows, cols):
        res = []
        for _ in range(rows):
            res.append([' '] * cols)
        return res
    
    def get_cell(self, pos):
        return self.grid[pos[1]][pos[0]]
    
    def draw_cell(self, cell):
        self.grid[cell[1]][cell[0]] = cell[2]
        return self
    
    def clear(self):
        self.grid = self.gen_blank_grid(self.rows, self.cols)
        return self
    
    def redraw_frame(self, cells):
        self.clear()
        for cell in cells:
            y = cell[1]
            x = cell[0]
            symb = cell[2]
            try:
                self.grid[y][x] = symb
            except IndexError as e:
                raise IndexError(f"Cell ({x}, {y}) is out of bounds")
        return self
        