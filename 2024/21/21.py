from functools import cache
from random import random

N = "789|456|123| 0A"
NC = {c: (x,y) for y, r in enumerate(N.split('|')) for x, c in enumerate(r)}

R = " ^A|<v>"
RC = {c: (x,y) for y, r in enumerate(R.split('|')) for x, c in enumerate(r)}

@cache
def path_to(start, end, numpad):
    pad = NC if numpad else RC
    sx,sy = pad[start]
    ex,ey = pad[end]
    dx = ex-sx
    dy = ey-sy
    spacex, spacey = pad[" "]
    ri = up = ""
    if not (sx == spacex and sy+dy == spacey):
        up += ("^" if dy < 0 else "v") * abs(dy)
        up += ("<" if dx < 0 else ">") * abs(dx)

    if not (sx+dx == spacex and sy == spacey):
        ri += ("<" if dx < 0 else ">") * abs(dx)
        ri += ("^" if dy < 0 else "v") * abs(dy)

    if up and ri:
        s = up if random() < 0.5 else ri
    else:
        s = up or ri
    return s + "A"
    

@cache
def length(P, char, i):
    if i == 0: return 1
    s = 0
    prev = 'A'
    for c in path_to(P, char, i==G):
        s += length(prev, c, i-1)
        prev = c
    return s

def solve(code):
    path_to.cache_clear()
    length.cache_clear()
    prev = 'A'
    s = 0
    for c in code:
        s += length(prev, c, G)
        prev = c
    return int(code[:-1]) * s

def simulate(code):
    return min(solve(code) for _ in range(1000))

codes = open(0).read().split()
G = 3
print(sum(simulate(code) for code in codes))
G = 26
print(sum(simulate(code) for code in codes))
