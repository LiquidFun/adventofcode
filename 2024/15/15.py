from collections import *
from itertools import *
from functools import *
# import numpy as np
# import networkx as nx
# import z3
import re
import sys
sys.setrecursionlimit(1000000)

s1 = s2 = 0

# d4 = [1, 1j, -1, -1j]
d4 = {'>': 1, 'v':1j, '<':-1, '^':-1j}
# d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
# d4half = [i/2 for i in d4]
# d8half = [i/2 for i in d8]
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]


field, moves = open(0).read().split("\n\n")


if True:
    for r, r2 in [("#", "##"), ("O", "[]"), (".", ".."), ("@", "@.")]:
        field = field.replace(r, r2)

coords = {x+1j*y: c for y, r in enumerate(field.strip().splitlines()) for x, c in enumerate(r.strip())}

# field = [list(l) for l in field.strip().split("\n")]
s = 0
for c, char in coords.items():
    if char == "@":
        s = c
        coords[c] = "."

M = max(map(lambda c: c.real, coords))
for c, char in coords.items():
    print(end=char)
    if c.real == M:
        print()


def collect(s, d):
    if coords[s+d] in "[]":
        dn = (1 if coords[s+d] == '[' else -1) + d
        base = {s+d: coords[s+d], s+dn: coords[s+dn]} | collect(s+d, d)
        if d not in [1, -1]:
            base |= collect(s+dn, d)
        return base
    return {}

for m in moves.strip():
    if m not in d4:
        continue
    # print(s)
    d = d4[m]
    n = s + d
    i = 1

    
    ok = True
    if coords[s + d] in '[]':
        boxes = collect(s, d)
        # print(boxes)
        for x, char in boxes.items():
            if coords[x+d] == '#':
                ok = False
                break
        if ok:
            for x, char in boxes.items():
                coords[x] = '.'
            for x, char in boxes.items():
                coords[x+d] = char
            s = n
    elif coords[s+d] == '.':
        s = n
    
    # while coords[s + d * i] in '[]':
    #     i += 1
    # if coords[s+d*i] == '.':
    #     coords[s+d*i] = 'O'
    #     coords[n] = '.'
    #     s = n

    # print("\033[0;0H")
    # for c, char in coords.items():
    #     print(end=char if c != s else '@')
    #     if c.real == M:
    #         print()
    # import time
    # time.sleep(0.02)

for c, char in coords.items():
    if char == '[':
        s1 += c.imag * 100 + c.real
    

# for line in open(0):
    # n = [int(a) for a in line.split()]
    # re.findall(r"\d+", line)
    

print(int(s1), s2, sep="\n")
# not 6186250.0
