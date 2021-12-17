import enum
import math
import sys


# icky thing to handle input
class Data(object):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def has_more(self):
        return self.pos < len(self.data) - 1

    def read(self, bits):
        data = self.data[self.pos : self.pos + bits]
        self.pos += bits
        return data

    def int(self, bits):
        return int(self.read(bits), 2)


class Packet(object):
    def __init__(self, version, typ, value=None, children=[]):
        self.version = version
        self.type = typ
        self.value = value
        self.children = children

    def can_solve(self):
        return all([sp.value is not None for sp in self.children])

    def __repr__(self):
        return (
            f"<Packet version={self.version} type={self.type.name} value={self.value}>"
        )


class PacketType(enum.IntEnum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQ = 7


def header(data):
    return (data.int(3), PacketType(data.int(3)))


def literal(data):
    i = 0
    accum = 0
    while True:
        val = data.int(5)
        more = val >> 4
        val &= ~0x10  # mask 5th bit
        accum <<= 4
        accum |= val
        if not more:
            break
        i += 1
    return accum


def subpackets(data):
    length_type = data.int(1)
    subp = []
    if length_type == 0:
        # 🤷‍♂️ not sure how to make this better
        tmp = Data(data.read(data.int(15)))
        while tmp.has_more():
            subp.append(packet(tmp))
    else:
        for _ in range(data.int(11)):
            subp.append(packet(data))
    return subp


def packet(data):
    ver, typ = header(data)
    if typ == PacketType.LITERAL:
        return Packet(ver, typ, value=literal(data))
    else:
        return Packet(ver, typ, children=subpackets(data))


def solve(p):
    for sp in p.children:
        solve(sp)
    if p.type == PacketType.SUM:
        p.value = sum(sp.value for sp in p.children)
    elif p.type == PacketType.PRODUCT:
        p.value = math.prod(sp.value for sp in p.children)
    elif p.type == PacketType.MINIMUM:
        p.value = min(sp.value for sp in p.children)
    elif p.type == PacketType.MAXIMUM:
        p.value = max(sp.value for sp in p.children)
    elif p.type == PacketType.GT:
        p.value = int(p.children[0].value > p.children[1].value)
    elif p.type == PacketType.LT:
        p.value = int(p.children[0].value < p.children[1].value)
    elif p.type == PacketType.EQ:
        p.value = int(p.children[0].value == p.children[1].value)
    assert Exception(f"unknown type {p.type}")


def main():
    # in an ideal world this would be less awful (i.e. maybe not strings?)
    data = Data(
        "".join([bin(int(v, 16))[2:].zfill(4) for v in sys.stdin.read().strip()])
    )

    def sum_versions(p):
        return p.version + sum(sum_versions(sp) for sp in p.children)

    msg = packet(data)
    print(f"Part 1: {sum_versions(msg)}")

    solve(msg)
    print(f"Part 2: {msg.value}")


main()
