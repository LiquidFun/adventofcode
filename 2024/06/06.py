from collections import *
from itertools import *
from functools import *
import re

d4 = [-1j, 1, 1j, -1]
d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]


coords = {x+1j*y: c for y, r in enumerate(open(0).read().splitlines()) for x, c in enumerate(r)}
# field = open(0).read().splitlines()

for pos, c in coords.items():
    if c == "^":
        start = pos

def solve(obstruction, s=start):
    dir = d4[0]

    # seen_with_dir = set()
    print(obstruction, s2)

    turn = defaultdict(list)
    seen = {s, (s, dir)}
    while s in coords:
        # print(s, dir)
        while s + dir in coords and coords[s + dir] != '#' and s + dir != obstruction:
            # print("\t", s)
            seen.add(s)
            seen.add((s, dir))
            s += dir
        if s + dir not in coords:
            return False
        turn[s.real].append(s.imag)
        dir *= 1j
        if (s, dir) in seen:
            return True

    # print(turn)
    # turns = set()
    # s2 = 0
    # for y, row in turn.items():
    #     if len(row) < 2: continue
    #     for x in row:
    #         for y2, row2 in turn.items():
    #             if y2 != y and x in row2:
    #                 for x2 in row:
    #                     if x2 == x: continue
    #                     turns.add(tuple(sorted(((y, x), (y2, x), (y, x2)))))
    #                 s2 += 1
    # for t in sorted(turns):
    #     print(t)
    # print(len(turns))
    # print(s2)
    # exit(0)



    # for y in range(100):
    #     some = False
    #     for x in range(100):
    #         p = x + 1j * y
    #         if p in coords:
    #             print(end=coords[p] if p not in seen else "o")
    #             some = True
    #     if some:
    #         print()

    # print(len(seen))

s2 = 0
for coord in coords:
    s2 += solve(coord)
print(s2)
