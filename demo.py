from binary_tree import binary_tree
from sidewinder import sidewinder
from grid import Grid

g1 = Grid(10, 10)
g2 = Grid(10, 10)

binary_tree(g1)
sidewinder(g2)

print("Binary Tree:")
print("Notable Characteristics")
print("- contiguous top and right corridors")
print("- easy to navigate when going bottom-left to top-right")
print(f"{g1}\n")

print("Sidewinder:")
print("Notable Characteristics")
print("- contiguous top corridor")
print("- easy to navigate when going bottom to top")
print(f"{g2}\n")
