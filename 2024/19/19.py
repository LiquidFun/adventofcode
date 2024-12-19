from collections import *
from itertools import *
from functools import *
import numpy as np
import networkx as nx
# import z3
import re
import sys
sys.setrecursionlimit(1000000)

s1 = s2 = 0
# coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

d4 = [1, 1j, -1, -1j]
d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
d4half = [i/2 for i in d4]
d8half = [i/2 for i in d8]
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]


patterns, designs = open(0).read().split("\n\n")
patterns = set(patterns.strip().split(", "))
designs = designs.strip().split("\n")
# print(sorted(patterns, key=len))

patterns_regex = set(patterns)

for pattern in list(patterns):
    if len(pattern) > 1 and "r" not in pattern:
        patterns_regex.remove(pattern)

# print(sorted(patterns, key=len))
# exit(0)
M = max(map(len, patterns))

g = '|'.join(sorted(patterns_regex, key=len))
# print(g)
reg = re.compile(rf"^({g})+$")
# print(reg)

def find3(design):
    dp = [0] * (len(design)+1)
    dp[0] = 1
    for i in range(len(design)):
        d = design[i:]
        for pattern in patterns:
            if d.startswith(pattern):
                # print(d, pattern, dp)
                dp[i+len(pattern)] += dp[i]
    print(dp)
    return dp[-1]

def find2(design):
    b = bool(reg.fullmatch(design))
    print(b)
    return b

def find(design, j=0):
    # global s1
    if j == len(design):
        # s1 += 1
        print(design)
        return True
    # for i in range(M, 0, -1):
    for i in range(M):
        if design[j:j+i] in patterns:
            # print(design[j:], design[j:j+i])
            if f := find(design, j+i):
                return f
    return False
from concurrent.futures import ProcessPoolExecutor

# print(find3(designs[0]))
# print(find2(designs[0]))
# exit(0)

with ProcessPoolExecutor() as executor:
    for good in executor.map(find3, designs):
        s1 += bool(good)
        s2 += good

# import multiprocessing as mp
# print(mp.cpu_count())

# pool = mp.Pool(mp.cpu_count())

# results = pool.map(find, designs)
# pool.close()

# for design in designs):
#     s1 += find(design)
#     print(s1, design)

# print(sum(results))

# for line in open(0):
#     n = [int(a) for a in line.split()]
    # re.findall(r"\d+", line)
    

print(s1, s2, sep="\n")
