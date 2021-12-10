import sys

lines = [line.strip() for line in sys.stdin]

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

corrupt_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

completion_score = {c: i + 1 for i, c in enumerate(")]}>")}

def score_completion(stack):
    score = 0
    for c in reversed(stack):
        score *= 5
        score += completion_score.get(pairs[c])
    return score

def score_line(line):
    stack = []
    for i, c in enumerate(line):
        if c in pairs:
            stack.append(i)
        else:
            if not stack:
                raise Exception("started with chunk closing")
            opening = line[stack[-1]]
            expect = pairs[opening]
            if c != expect:
                return (corrupt_score[c], 0)
            stack.pop()
    # getting here means the line is not corrupt and presumably incomplete
    return (0, score_completion([line[i] for i in stack]))

scores = [score_line(line) for line in lines]
corrupt_scores = [s[0] for s in scores]
completion_scores = [s[1] for s in scores if s[1] > 0]

print("part 1: " + str(sum(corrupt_scores)))
print("part 2: " + str(sorted(completion_scores)[len(completion_scores) // 2]))
