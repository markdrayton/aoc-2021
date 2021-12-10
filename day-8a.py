import sys

# number of segments -> corresponding digit
unique = {2: 1, 3: 7, 4: 4, 7: 8}

count = 0
for line in sys.stdin:
    line = line.strip()
    patterns, _, digits = line.partition(" | ")
    for digit in digits.split():
        if len(digit) in unique:
            count += 1
print(count)
