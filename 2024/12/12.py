from collections import *
from itertools import *
from functools import *
import sys
import re

sys.setrecursionlimit(1000000)

coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

d4 = [1, 1j, -1, -1j]
dc = [i/2 for i in [1+1j, 1-1j, -1+1j, -1-1j]]
# print(dc)
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]




# for line in open(0):
#     n = [int(a) for a in line.split()]
    # re.findall(r"\d+", line)

regions = []

visited = set()

def collect(c, char, region):
    visited.add(c)
    region.append(c)
    for adj in adjacent(c):
        if coords.get(adj) == char:
            if adj not in visited:
                collect(adj, char, region)
    return region


for c in coords:
    char = coords[c]
    if c not in visited:
        regions.append((char, collect(c, char, [])))


s = 0
s2 = 0
for char, region in regions:
    perimeter = 0
    # # # sides = 0
    for r in region:
        for adj in adjacent(r):
            if coords.get(adj) != char and adj not in region:
                # sides.add(adj)
                perimeter += 1
    corners = set()
    for c in region:
        for delta in adjacent(c, dc):
            k = 0
            ks = []
            for adj in adjacent(delta, dc):
                adj = round(adj.real) + round(adj.imag) * 1j
                k += adj in region
                if adj in region:
                    ks.append(adj)
            if k in [1,3]:
                corners.add(delta)
            if k == 2 and (ks[0] - ks[1]).real and (ks[0] - ks[1]).imag:
                corners.add(delta)
                corners.add(delta + 0.001)
    # print(char, corners, len(corners) * len(region), len(corners))

    s += perimeter * len(region)
    s2 += len(corners) * len(region)


print(s)

print(s2)
