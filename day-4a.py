import sys

class Board(object):
    def __init__(self, lines):
        self.lines = lines

    @property
    def rows(self):
        return self.lines

    @property
    def cols(self):
        return [[line[i] for line in self.lines]
                for i in range(len(self.lines[0]))]

    def mark(self, search):
        self.lines = [[None if v == search else v for v in line]
                for line in self.lines]

    def has_won(self):
        def marked(line):
            return all([x is None for x in line])
        return any([marked(line) for line in self.cols + self.rows])

    def render(self):
        def fmt(val):
            return f"{'-':2s}" if val is None else f"{val:2d}"

        return "\n".join(
                [" ".join([fmt(v) for v in line]) for line in self.lines])

    def sum(self):
        return sum([sum([v for v in line if v is not None]) for line in self.lines])

boards = []

first = True
lines = []
for line in sys.stdin:
    line = line.strip()
    if first:
        drawn = [int(n) for n in line.split(",")]
        first = False
    elif line == "":
        pass
    else:
        lines.append([int(n) for n in line.split()])
        if len(lines) == 5:
            boards.append(Board(lines))
            lines = []

for i, draw in enumerate(drawn):
    print(f"==> {i}")
    for j, board in enumerate(boards):
        board.mark(draw)
        print(board.render())
        if board.has_won():
            print(f"==> draw {draw}, board {j} is WINNER")
            print(board.sum() * draw)
            sys.exit()
        print()
