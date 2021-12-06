import sys

def coords(text):
    c1, _, c2 = text.partition(",")
    return int(c1), int(c2)

def print_grid(grid):
    for line in grid:
        print(" ".join([str(y) if y else "." for y in line]))

def read_input():
    vents = []
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        x1, y1 = coords(parts[0])
        x2, y2 = coords(parts[2])
        vents.append((x1, y1, x2, y2))
    return vents

vents = read_input()
max_x = max([max(x1, x2) for x1, y1, x2, y2 in vents])
max_y = max([max(y1, y2) for x1, y1, x2, y2 in vents])

grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for x1, y1, x2, y2 in vents:
    if x1 == x2:
        for y in range(y1, y2, 1 if y2 > y1 else -1):
            grid[y][x1] += 1
    elif y1 == y2:
        for x in range(x1, x2, 1 if x2 > x1 else -1):
            grid[y1][x] += 1
    else:
        yr = range(y1, y2, 1 if y2 > y1 else -1)
        xr = range(x1, x2, 1 if x2 > x1 else -1)
        for y, x in (list(zip(yr, xr))):
            grid[y][x] += 1
    grid[y2][x2] += 1

count = 0
for col in grid:
    for cell in col:
        if cell > 1:
            count += 1
print(count)
