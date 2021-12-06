import sys
from collections import Counter

vals = [int(line.rstrip(), 2) for line in sys.stdin]

def find_msb(n):
    i = 0
    while 2 ** i <= n:
        i += 1
    return i

def bit_set(val, n):
    return 1 if (val & (0x1 << n)) > 0 else 0

msb = find_msb(max(vals))
freqs = [[bit_set(val, n) for val in vals] for n in range(msb)]

gamma = 0
for i, bits in enumerate(freqs):
    most_common = Counter(bits).most_common(1)[0][0]
    gamma ^= (most_common << i)

print(f"{gamma:016b}")
mask = (1 << msb) - 1
epsilon = gamma ^ mask
print(f"{epsilon:016b}")
print(gamma * epsilon)
