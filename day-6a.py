import sys

fish = [int(v) for v in sys.stdin.read().strip().split(",")]

day = 0
while day < int(sys.argv[1]):
    print(day)
    nfish = len(fish)
    i = 0
    while i < nfish:
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
        i += 1
    day += 1

print(f"result {len(fish)}")
