import sys

elves = sorted([sum(map(int, line.split("\n"))) for line in sys.stdin.read().strip().split("\n\n")])

print(elves[-1])
print(sum(elves[-3:]))
