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
    yy = ("^" if dy < 0 else "v") * abs(dy)
    xx = ("<" if dx < 0 else ">") * abs(dx)
    if not (sx == spacex and sy+dy == spacey):
        s = up = yy + xx
    if not (sx+dx == spacex and sy == spacey):
        s = ri = xx + yy

    if up and ri:
        s = up if random() < 0.5 else ri
    return s + "A"
    
@cache
def length(code, robot, s=0):
    if robot == 0: return len(code)
    for i, c in enumerate(code):
        s += length(path_to(code[i-1], c, robot==G), robot-1)
    return s

def solve(code):
    path_to.cache_clear()
    length.cache_clear()
    return int(code[:-1]) * length(code, G)

def simulate(code):
    return min(solve(code) for _ in range(1000))

codes = open(0).read().split()
G = 3
print(sum(simulate(code) for code in codes))
G = 26
print(sum(simulate(code) for code in codes))
