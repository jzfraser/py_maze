from cell import Cell
from random import randrange


class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = self.prepare_grid()
        self.configure_cells()

    def __repr__(self):
        output = "+" + "---+" * self.cols + "\n"
        for r, row in enumerate(self.grid):
            top = "|"
            bottom = "+"
            for cell in row:
                east_boundary = " " if cell.linked(cell.east) else "|"
                top += "   " + east_boundary

                south_boundary = "   " if cell.linked(cell.south) else "---"
                bottom += south_boundary + "+"
            output += top + "\n"
            output += bottom
            if r < self.rows - 1:
                output += "\n"

        return output

    # safely get cell at row, col
    # returns None if coords are invalid
    def get_cell(self, row, col):
        if row < 0 or row >= self.rows:
            return None
        elif col < 0 or col >= self.cols:
            return None
        return self.grid[row][col]

    def size(self):
        return self.rows * self.cols

    def prepare_grid(self):
        return [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]

    def configure_cells(self):
        r = 0
        c = 0
        for row in self.grid:
            for cell in row:
                cell.north = self.get_cell(r - 1, c)
                cell.south = self.get_cell(r + 1, c)
                cell.east = self.get_cell(r, c + 1)
                cell.west = self.get_cell(r, c - 1)
                c += 1
            r += 1
            c = 0

    def random_cell(self):
        row = randrange(0, self.rows)
        col = randrange(0, self.cols)
        return self.get_cell(row, col)


if __name__ == "__main__":
    g = Grid(2, 2)
    print(f"{g.size()} cells in grid")
    print(g)
    print()

    for row in g.grid:
        for cell in row:
            print(f"{cell}'s neighbors: {cell.neighbors()}")

    print(f"A random cell is: {g.random_cell()}")
