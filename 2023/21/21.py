import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, product, combinations_with_replacement
from queue import PriorityQueue

lines = open(0).read().splitlines()
Y, X = len(lines), len(lines[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = deque()

dists = {}
for y, line in enumerate(lines):
    if 'S' in line:
        q.append((y, line.index('S')))
        dists[(y, line.index('S'))] = (0, 0)

s = 0
# for i in range(64):
# nextq = deque()
visited = set()
nextq = deque()
while q:
    y, x = q.popleft()
    dist_inner, dist_outer = dists[(y, x)]
    for dy, dx in dirs:
        ya, xa = y + dy, x + dx
        in_inner = 0 <= ya < Y and 0 <= xa < X
        in_outer = -Y*2 <= ya < Y*3 and -X*2 <= xa < X*3
        if in_outer and lines[ya%Y][xa%X] != '#':  # and (ya, xa) not in visited:
            # ok = True
            # if (ya, xa) in dists:
            #     di, do = dists[(ya, xa)]
            #     ok = dist_outer+(not in_inner) < do
            # if ok:
            if (ya, xa) not in visited:
                dists[(ya, xa)] = (dist_inner + in_inner, dist_outer + (not in_inner))
                if in_inner:
                    q.append((ya, xa))
                else:
                    nextq.append((ya, xa))
            visited.add((ya, xa))
    if not q:
        q = nextq

    # q = nextq

print(dists)
print(len(dists))

for y in range(-Y, Y*2):
    for x in range(-X, X*2):
        v = '#'
        if (y, x) in dists:
            di, do = dists[(y, x)]
            yadd = 0 if (y == y%Y) else (Y if (y > y%Y) else -Y)
            xadd = 0 if (x == x%X) else (X if (x > x%X) else -X)
            _, veryouter_do = dists[(y+yadd, x+xadd)]
            repeat = veryouter_do - do
            # repeat = do
            v = str((di, repeat))
            v = v.replace("(", "").replace(",", "").replace(")", "").replace(" ", "-")
        print(end=f"{v:8}")
    print()


target = 26501365
target = 1000
for y in range(-Y, Y*2):
    for x in range(-X, X*2):
        if (y, x) in dists:
            # print(lines[y%Y][x%X])
            in_inner = 0 <= y < Y and 0 <= x < X
            di, do = dists[(y, x)]
            inner_di, _ = dists[(y%Y, x%X)]
            if in_inner:
                if di % 2 == 1:
                    s += 1
            else:
                new = (target - di)
                if new % 2 == 1:
                    repeat = (di - inner_di) + do
                    s += new // repeat

print(s)
