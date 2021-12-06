import sys

prev = None
count = 0

for line in sys.stdin:
    val = int(line.strip())
    if prev and val > prev:
        count += 1
    prev = val

print(count)
