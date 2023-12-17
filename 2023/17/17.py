from sys import stdin
from queue import PriorityQueue

lines = stdin.read().splitlines()
Y, X = len(lines), len(lines[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(min_straight, max_straight):
    q = PriorityQueue()
    q.put((0, 0, 0, 0, 0))
    visited = set()
    while not q.empty():
        dist, y, x, movedy, movedx = tup = q.get()
        if y == Y-1 and x == X-1:
            return dist
        if tup[1:] in visited:
            continue
        visited.add(tup[1:])
        for dy, dx in dirs:
            ay, ax = y+dy, x+dx
            if movedy * dy < 0 or movedx * dx < 0: 
                continue  # prevent reversing
            movedy2 = movedy + dy
            movedx2 = movedx + dx
            straight = max(abs(movedy2), abs(movedx2))
            if abs(movedy2) > 0 and abs(movedx2) > 0:
                if straight < min_straight:
                    continue  # prevent turning if not at least n straight
                movedy2 *= abs(dy)
                movedx2 *= abs(dx)

            new_tup = (ay, ax, movedy2, movedx2)
            if 0 <= ay < Y and 0 <= ax < X and straight <= max_straight and new_tup not in visited:
                q.put((dist+int(lines[ay][ax]), ay, ax, movedy2, movedx2))

print(solve(0, 3))
print(solve(4, 10))
