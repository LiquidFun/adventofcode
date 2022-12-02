import sys

points = {"A Y": 6, "B Z": 6, "C X": 6, "A X": 3, "B Y": 3, "C Z": 3}

def score(moves: str):
    return points.get(moves, 0) + "-XYZ".index(moves[2])

def change(moves: str):
    index = ("ABC".index(moves[0]) + "YZX".index(moves[2])) % 3
    return moves[:2] + "XYZ"[index]

lines = sys.stdin.read().strip().split("\n")

print(sum(map(score, lines)))
print(sum(map(score, map(change, lines))))
