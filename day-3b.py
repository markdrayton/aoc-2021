import copy
import sys
from collections import Counter

vals = [int(line.rstrip(), 2) for line in sys.stdin]

def find_msb(n):
    i = 0
    while 2 ** i <= n:
        i += 1
    return i

def bit(val, n):
    return 1 if (val & (0x1 << n)) > 0 else 0

def most_common(bits):
    c = Counter(bits)
    return 1 if c.get(1, 0) >= c.get(0, 0) else 0

def least_common(bits):
    c = Counter(bits)
    return 0 if c.get(0, 0) <= c.get(1, 0) else 1

def format_vals(vals, msb):
    return ", ".join([f"{v:0{msb}b}" for v in vals])

msb = find_msb(max(vals))
freqs = [[bit(val, n) for val in vals] for n in range(msb)]

def extract(vals, msb, fn):
    vals = copy.copy(vals)
    print(f"=> {format_vals(vals, msb)}")
    for pos in reversed(range(msb)):
        comp = fn([bit(val, pos) for val in vals])
        vals = [val for val in vals if bit(val, pos) == comp]
        print(format_vals(vals, msb))
        if len(vals) == 1:
            return vals[0]
    assert False

oxygen = extract(vals, msb, most_common)
co2 = extract(vals, msb, least_common)

print(oxygen * co2)
