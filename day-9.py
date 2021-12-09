import collections
import sys

Point = collections.namedtuple("Point", ["x", "y"])

grid = [[int(v) for v in line.strip()] for line in sys.stdin]

def adjacent(p):
    adjacent = []
    if p.x > 0:
        adjacent.append(Point(p.x - 1, p.y))
    if p.x < len(grid[y]) - 1:
        adjacent.append(Point(p.x + 1, p.y))
    if p.y > 0:
        adjacent.append(Point(p.x, p.y - 1))
    if p.y < len(grid) - 1:
        adjacent.append(Point(p.x, p.y + 1))
    return adjacent

low_points = []
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val < min([grid[p.y][p.x] for p in adjacent(Point(x, y))]):
            low_points.append(Point(x, y))

print(sum([grid[lp.y][lp.x] + 1 for lp in low_points]))

def probe(p, basin=None, indent=0):
    val = grid[p.y][p.x]
    if basin is None:
        basin = set()
    for a in adjacent(p):
        if grid[a.y][a.x] > val and grid[a.y][a.x] != 9:
            basin.add(a)
            probe(a, basin, indent + 1)
    return len(basin)

basins = sorted([probe(lp) + 1 for lp in low_points], reverse=True)
print(basins[0] * basins[1] * basins[2])
