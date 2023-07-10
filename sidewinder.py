from random import randrange
from grid import Grid


def sidewinder(grid: Grid):
    for row in grid.grid:
        run = []
        for cell in row:
            run.append(cell)

            at_east_boundary = cell.east == None
            at_north_boundary = cell.north == None

            should_close_run = at_east_boundary or (
                not at_north_boundary and randrange(2) == 0
            )

            if should_close_run:
                member = run[randrange(len(run))]
                if member.north:
                    member.link(member.north)
                run.clear()
            elif cell.east:
                cell.link(cell.east)


if __name__ == "__main__":
    g = Grid(10, 10)
    sidewinder(g)
    print(g)
