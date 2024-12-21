from functools import cache
from random import random

N = "789|456|123| 0A"
NC = {c: x+1j*y for y, r in enumerate(N.split('|')) for x, c in enumerate(r)}

R = " ^A|<v>"
RC = {c: x+1j*y for y, r in enumerate(R.split('|')) for x, c in enumerate(r)}

@cache
def path_to(start, end, numpad):
    pad = NC if numpad else RC
    diff = pad[end] - pad[start]
    dx, dy = int(diff.real), int(diff.imag)
    yy = ("^" if dy < 0 else "v") * abs(dy)
    xx = ("<" if dx < 0 else ">") * abs(dx)

    if pad[start] + dy*1j == pad[" "]:
        return xx + yy + "A"
    if pad[start] + dx == pad[" "]:
        return yy + xx + "A"
    return (xx+yy if random() < 0.5 else yy+xx) + "A"  # ¯\_(ツ)_/¯
    
@cache
def length(code, robot, first=False, s=0):
    if robot == 0: 
        return len(code)
    for i, c in enumerate(code):
        s += length(path_to(code[i-1], c, first), robot-1)
    return s

def solve(code, R):
    path_to.cache_clear()
    length.cache_clear()
    return int(code[:-1]) * length(code, R, True)

def simulate(code, R):
    return min(solve(code, R) for _ in range(1000))

codes = open(0).read().split()
print(sum(simulate(code, 3) for code in codes))
print(sum(simulate(code, 26) for code in codes))
