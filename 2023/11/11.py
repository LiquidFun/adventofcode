from sys import stdin
from itertools import combinations, product

lines = stdin.read().strip().split('\n')

Ys, Xs = len(lines), len(lines[0])
cols = [0] * Ys
rows = [0] * Xs

for y, line in enumerate(lines):
    if line.count('.') == len(line):
        rows[y] += 1
for x in range(Xs):
    if all(lines[y][x] != '#' for y in range(Ys)):
        cols[x] += 1

galaxies = [(y, x) for y, x in product(range(Ys), range(Xs)) if lines[y][x] == '#']

def solve(multiplier=1, s=0):
    for (y, x), (Y, X) in combinations(galaxies, r=2):
        y, Y = sorted([y, Y])
        x, X = sorted([x, X])
        s += Y - y + X - x + (sum(rows[y:Y]) + sum(cols[x:X])) * multiplier
    return s

print(solve())
print(solve(1000000-1))

