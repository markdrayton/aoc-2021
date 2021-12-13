import sys


def pg(dots):
    mx = max(d[0] for d in dots)
    my = max(d[1] for d in dots)
    grid = [[0 for _ in range(mx + 1)] for _ in range(my + 1)]
    for x, y in dots:
        grid[y][x] = 1
    for y in grid:
        print("".join(["#" if x else " " for x in y]))
    print()


def fold(dots, axis, pivot):
    new = set()
    for x, y in dots:
        if axis == "x":
            new.add((x, y) if x < pivot else (pivot + (pivot - x), y))
        else:
            new.add((x, y) if y < pivot else (x, pivot + (pivot - y)))
    return new


def main():
    dots = set()
    folds = []
    for line in sys.stdin:
        line = line.strip()
        if line != "":
            if " " in line:
                axis, pivot = line.split(" ")[-1].split("=")
                folds.append((axis, int(pivot)))
            else:
                x, y = line.split(",")
                dots.add((int(x), int(y)))

    i = 0
    for axis, pivot in folds:
        dots = fold(dots, axis, pivot)
        if i == 0:
            print(f"Part 1: {len(dots)}")
        i += 1
    print("Part 2:")
    pg(dots)


main()
