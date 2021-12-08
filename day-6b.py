import functools
import sys
from collections import Counter

fish = Counter([int(v) for v in sys.stdin.read().strip().split(",")])
initial_days = int(sys.argv[1])

@functools.cache
def spawn(days):
    out = 1
    for day in range(days, 0, -7):
        out += spawn(day - 9)
    return out

print(sum(spawn(initial_days - age) * count for age, count in fish.items()))
