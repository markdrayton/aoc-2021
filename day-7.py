import operator
import sys

crabs = [int(v) for v in sys.stdin.read().strip().split(",")]

def cost1(crab, pos):
    return abs(crab - pos)

def cost2(crab, pos):
    n = abs(crab - pos)
    return n * (n + 1) // 2

def compute(fn):
    return [sum(fn(crab, pos) for crab in crabs)
        for pos in range(min(crabs), max(crabs) + 1)]

print(f"Part 1: {min(compute(cost1))}")
print(f"Part 2: {min(compute(cost2))}")
