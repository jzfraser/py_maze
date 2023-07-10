from typing import Optional


class Cell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.north: Optional[Cell] = None
        self.east: Optional[Cell] = None
        self.south: Optional[Cell] = None
        self.west: Optional[Cell] = None
        self.links: dict = {}

    def __repr__(self):
        return f"({self.row}, {self.col})"

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)

    def linked(self, cell) -> bool:
        return cell in self.links

    def neighbors(self):
        nbrs: list[Cell] = []
        if self.north:
            nbrs.append(self.north)
        if self.south:
            nbrs.append(self.south)
        if self.east:
            nbrs.append(self.east)
        if self.west:
            nbrs.append(self.west)
        return nbrs


if __name__ == "__main__":
    c1 = Cell(0, 0)
    c2 = Cell(1, 1)
    print(f"Current cells:\n{c1}\n{c2}")

    c1.link(c2)
    print("\nLinking cells c1, c2")
    print("c1 links:")
    for l in c1.links:
        print(f"{l} is linked: {c1.linked(l)}")
    print("c2 links:")
    for l in c2.links:
        print(f"{l} is linked: {c2.linked(l)}")

    print("\nUnlinking cells c1, c2")
    c1.unlink(c2)
    print(f"{c2} is linked to {c1}: {c1.linked(c2)}")
    print(f"{c1} is linked to {c2}: {c2.linked(c1)}")
