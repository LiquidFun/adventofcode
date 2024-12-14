from collections import *
import time
from itertools import *
from functools import *
# import networkx as nx
import re
import sys
sys.setrecursionlimit(1000000)

s1 = s2 = 0
# coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

d4 = [1, 1j, -1, -1j]
d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
d4half = [i/2 for i in d4]
d8half = [i/2 for i in d8]
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]




X = 101
Y = 103
# X = 11
# Y = 7
maps = []
for line in open(0):
    x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
    maps.append((x, y, vx, vy))
8
70
284

seen = set()

for i in range(0, X * Y, 1):
    counts = {}
    quadrant = [0, 0, 0, 0]
    nines = [0] * 9
    rows = Counter()
    for x, y, vx, vy in maps:
        nx = (x + vx * i) % X
        ny = (y + vy * i) % Y
        if (nx, ny) not in counts:
            counts[(nx, ny)] = 0
        counts[(nx, ny)] += 1
        rows[ny] += 1
        # print(x, y, nx, ny)
        # print(nx, (nx >= 55) + (ny >= 56) * 2)
        # print(X // 2, Y // 2)
        if nx != X // 2 and ny != Y // 2:
            q = (nx > X//2) + (ny > Y//2) * 2
            #print(q)
            quadrant[q] += 1
            n = (nx // (X//3+1)) + (ny // (Y//3+1)) * 3
            # print(n)
            nines[n] += 1
    seen.add((tuple(sorted(quadrant)), i))


    # key = tuple(counts.items())
    # if key in seen:
    #     break
    # seen.add(key)

    s = quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3]
    # if any(q <= 10 for q in nines):
    if rows[40] > 30:
        for yy in range(Y):
            print(end=str(yy))
            for xx in range(X):
                print(end="#" if (xx, yy) in counts else " ")
                # print(end=str(counts.get((xx, yy), " ")))
            print()

        print(quadrant)
        print(i)
        print()
    # time.sleep(0.1)

        # print(quadrant)

# print(sorted(seen, reverse=True))

print(quadrant)

print(s1, s2, sep="\n")
