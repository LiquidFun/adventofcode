from collections import *
from itertools import *
from functools import *
import re

coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

# d4 = [1, 1j, -1, -1j]
# d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
# def adjacent(coord, dirs=d4):
#     return [coord + d for d in dirs]


order = defaultdict(list)

for coord, char in coords.items():
    if char != '.':
        order[char].append(coord)

antinodes = set()
# print(order)

for char, coord in order.items():
    for a, b in combinations(coord, r=2):
        diff = a - b
        i = 0
        while (new := a + diff * i) in coords:
            antinodes.add(new)
            i += 1 
        i = 0
        while (new := b - diff * i) in coords:
            antinodes.add(new)
            i += 1 
# print()
antinodes &= coords.keys()
# print(antinodes)

for y in range(12):
    for x in range(12):
        c= y*1j+x
         
        print(end='#' if c in antinodes else coords[c])
    print()
    
print(len(antinodes))



# for line in open(0):
#     n = [int(a) for a in line.split()]
    # re.findall(r"\d+", line)
