import sys

horiz = 0
depth = 0

for line in sys.stdin:
    line = line.rstrip()
    direction, _, val = line.partition(" ")
    val = int(val)
    if direction == "forward":
        horiz += val
    elif direction == "down":
        depth += val
    elif direction == "up":
        depth -= val
    else:
        raise Exception(f"unknown direction {direction}")

print(f"h={horiz}, d={depth}, answer={horiz * depth}")
