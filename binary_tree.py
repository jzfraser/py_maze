from grid import Grid
from random import randrange


def binary_tree(grid: Grid):
    for row in grid.grid:
        for cell in row:
            nbrs = []
            if cell.north:
                nbrs.append(cell.north)
            if cell.east:
                nbrs.append(cell.east)

            if len(nbrs):
                idx = randrange(len(nbrs))
                nbr = nbrs[idx]
                cell.link(nbr)


if __name__ == "__main__":
    grid = Grid(15, 15)
    binary_tree(grid)
    print(grid)
