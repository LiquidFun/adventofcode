from sys import stdin
from collections import deque

lines = stdin.read().strip().split('\n')

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
allowed = ["-7J", "|JL", "|F7", "-FL"]

def is_valid(y, x):
    return -0.5 <= y < len(lines) and -0.5 <= x < len(lines[0])

q = deque()
for y, line in enumerate(lines):
    if 'S' in line:
        q.append((y, line.index('S'), 0))

# Part 1: use BFS with allow_from and allow_to to check whether there is a connection
inside = {(y, x) for y in range(len(lines)) for x in range(len(lines[0]))}
visited = set()
max_dist = 0

while q:
    y, x, dist = q.popleft()
    max_dist = max(max_dist, dist)
    visited.add((y, x))
    inside.discard((y, x))

    for (dy, dx), allow_to, allow_from in zip(dirs, allowed, allowed[::-1]):
        ya, xa = y+dy, x+dx
        if is_valid(ya, xa) and lines[ya][xa] in allow_to and lines[y][x] in allow_from+"S":
            if (ya, xa) not in visited:
                q.append((ya, xa, dist+1))
            visited.add((y+dy/2, x+dx/2))


# Part 2: use a 0.5 grid to find all non-visited spaces, using the same visited set as in P1.
# Since we start outside of the grid, any cells inside will not be reached.
q.append((-0.5, -0.5))

while q:
    y, x = q.popleft()
    inside.discard((y, x))

    for dy, dx in dirs:
        ya, xa = y+dy/2, x+dx/2
        if is_valid(ya, xa) and (ya, xa) not in visited:
            q.append((ya, xa))
            visited.add((ya, xa))

print(max_dist)
print(len(inside))
