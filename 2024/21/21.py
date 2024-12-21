from collections import *
from random import *
from itertools import *
from functools import *
import numpy as np
import networkx as nx
# import z3
import re
import sys
sys.setrecursionlimit(1000000)

s1 = s2 = 0

d4 = [1, 1j, -1, -1j]
d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
d4half = [i/2 for i in d4]
d8half = [i/2 for i in d8]
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]

N = """
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""
N = """
789
456
123
 0A
"""
NC = {c: (x,y) for y, r in enumerate(N.splitlines()) for x, c in enumerate(r)}

R = """
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
R = """
 ^A
<v>
"""
RC = {c: (x,y) for y, r in enumerate(R.splitlines()) for x, c in enumerate(r)}
print(NC)

@cache
def path_to(start, end, numpad):
    pad = NC if numpad else RC
    sx,sy = pad[start]
    ex,ey = pad[end]
    dx = ex-sx
    dy = ey-sy
    spacex, spacey = pad[" "]
    # print(dx, dy)
    ri = ""
    up = ""
    if not (sx == spacex and sy+dy == spacey):
    # if sx+dx == spacex and sy == spacey:
        up += ("^" if dy < 0 else "v") * abs(dy)
        up += ("<" if dx < 0 else ">") * abs(dx)

    if not (sx+dx == spacex and sy == spacey):
    # else:
        ri += ("<" if dx < 0 else ">") * abs(dx)
        ri += ("^" if dy < 0 else "v") * abs(dy)

    if up and ri:
        s = up if random() < 0.5 else ri
    else:
        s = up or ri
    return s + "A"
    
# print(path_to("<", "A", RC))
# print(path_to("A", "<", RC))
# exit()
G = 26
# G = 3

# for r in R.replace("\n", "").strip():
#     for r2 in R.replace("\n", "").strip():
#         length(r, r2, 1)
# exit()
@cache
def length(P, char, i):
    if i == 0: return 1
    s = 0
    prev = 'A'
    for c in path_to(P, char, i==G):
        s += length(prev, c, i-1)
        prev = c
    # print(i, " : ", P, char, "  =  ", s, "   path: ", path_to(P, char, i==G))
    return s

def solve(code):
    path_to.cache_clear()
    length.cache_clear()
    prev = 'A'
    seq = code



    # for i in range(len(state)-1, -1, -1):
    #     pad = i == len(state)-1
    #     # print(i, pad)
    #     new_seq = ""
    #     for char in seq:
    #         new_seq += path_to(prev, char, pad)
    #         prev = char
    #     seq = new_seq
    #     print(i, len(seq))
        # print()
    s = 0
    for c in seq:
        s += length(prev, c, G)
        prev = c
    # print(int(code[:-1]) * s)
    return int(code[:-1]) * s

print(68 * 29, 60 * 980, 68 * 179, 64 * 456, 64 * 379)

def simul(code):
    robots = 26
    return min(solve(code) for _ in range(10000))

# re.findall(r"\d+", line)
for line in open(0):
    # s = solve(line.strip(), list("AAA"))
    s = simul(line.strip())
    print(line.strip(), s)
    s1 += s
    # exit()
    

print(s1, s2, sep="\n")
# 211930
# 217398
# 215546
# 990957
