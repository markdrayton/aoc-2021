import collections
import sys

unencoded = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]

# segments set in the digit 4 disambiguate g/d and a/c
def decode_segments(patterns, four):
    # {"f": 9, "a": 8, "c": 8, "g": 7, "d": 7, "b": 6, "e": 4}
    segs = [seg for pattern in patterns for seg in pattern]
    out = {}
    for segment, freq in collections.Counter(segs).items():
        if freq == 4:
            out[segment] = "e"
        elif freq == 6:
            out[segment] = "b"
        elif freq == 7:
            # can only be segment g or d
            out[segment] = "d" if set(segment) & set(four) else "g"
        elif freq == 8:
            # can only be segment a or c
            out[segment] = "c" if set(segment) & set(four) else "a"
        elif freq == 9:
            out[segment] = "f"
    assert "".join(sorted(out.values())) == "abcdefg"
    return out

total = 0
for line in sys.stdin:
    line = line.strip()
    patterns, _, digits = line.partition(" | ")

    four = None
    for pattern in patterns.split():
        if len(pattern) == 4:  # digit 4
            four = pattern
            break
    mapping = decode_segments(patterns.split(), four)

    val = ""
    for digit in digits.split():
        decoded = "".join(sorted([mapping[s] for s in digit]))
        n = None
        for i, d in enumerate(unencoded):
            if d == decoded:
                n = str(i)
        assert n is not None, f"coudln't find {decoded}"
        val += n
    total += int(val)
print(total)
