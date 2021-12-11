import copy
import sys

GRIDSIZE = 10

def adjacent(row, col):
    def bounds(pos):
        return range(max(pos - 1, 0), min(pos + 1, GRIDSIZE - 1) + 1)

    adj = [(r, c) for r in bounds(row) for c in bounds(col)]
    adj.remove((row, col))
    return adj

def step(g):
    flashes = 0

    # part 1
    for row in range(GRIDSIZE):
        for col in range(GRIDSIZE):
            g[row][col] += 1

    # part 2
    all_flash = set()
    while True:
        new_flash = set()
        for row in range(GRIDSIZE):
            for col in range(GRIDSIZE):
                if g[row][col] > 9 and (row, col) not in all_flash:
                    new_flash.add((row, col))
                    for r, c in adjacent(row, col):
                        g[r][c] += 1
        all_flash.update(new_flash)
        if len(new_flash) == 0:
            break

    # part 3
    for row, col in all_flash:
        g[row][col] = 0

    return len(all_flash)

def part1(g):
    total = 0
    for _ in range(100):
        total += step(g)
    print(total)

def part2(g):
    i = 1
    while True:
        flashed = step(g)
        if flashed == GRIDSIZE * GRIDSIZE:
            break
        i += 1
    print(i)

def main():
    grid = [[int(v) for v in line.strip()] for line in sys.stdin]
    part1(copy.deepcopy(grid))
    part2(copy.deepcopy(grid))

main()
