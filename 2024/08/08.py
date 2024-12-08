from itertools import *

coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

by = lambda v: v[1]
order = groupby(sorted(coords.items(), key=by), by)

p1, p2 = set(), set()

for char, coord in order:
    if char == '.': continue
    for (a, _), (b, _) in combinations(coord, r=2):
        diff = a - b
        p1 |= {a + diff*i for i in (-2, 1)}
        p2 |= {a + diff*i for i in range(-100, 100)}

print(len(p1 & coords.keys()))
print(len(p2 & coords.keys()))
