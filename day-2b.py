import sys

horiz = 0
depth = 0
aim = 0

for line in sys.stdin:
    line = line.rstrip()
    fields = line.split(" ")
    assert len(fields) == 2
    direction, val = fields[0], int(fields[1])
    if direction == "forward":
        horiz += val
        depth += (aim * val)
    elif direction == "down":
        aim += val
    elif direction == "up":
        aim -= val
    else:
        raise Exception(f"unknown direction {direction}")

print(f"a={aim}, h={horiz}, d={depth}, answer={horiz * depth}")
