from functools import cache
from random import random

N = {'7':0, '8':1, '9':2, '4':1j, '5':1+1j, '6':2+1j, 
      '1':2j, '2':1+2j, '3':2+2j, ' ':3j, '0':1+3j, 'A':2+3j}
R = {' ':0, '^':1, 'A':2, '<':1j, 'v':1+1j, '>':2+1j}

@cache
def path(start, end):
    pad = N if (start in N and end in N) else R
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
def length(code, depth, s=0):
    if depth == 0: return len(code)
    for i, c in enumerate(code):
        s += length(path(code[i-1], c), depth-1)
    return s

def solve(code, max_depth):
    path.cache_clear()
    length.cache_clear()
    return int(code[:-1]) * length(code, max_depth)

def simulate(code, max_depth):
    return min(solve(code, max_depth) for _ in range(1000))

codes = open(0).read().split()
print(sum(simulate(code, 3) for code in codes))
print(sum(simulate(code, 26) for code in codes))
