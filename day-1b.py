import sys

prev = None
count = 0

vals = [int(line.strip()) for line in sys.stdin]

i = 0
while True:
    win = vals[i:i+3]
    if len(win) < 3:
        break
    val = sum(win)
    if prev and val > prev:
        count += 1
    prev = val
    i += 1

print(count)
