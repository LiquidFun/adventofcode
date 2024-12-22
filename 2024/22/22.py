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

# G = nx.Graph()
# for c in coords:
#     for d in [1, 1j, -1, -1j]:
#         if coords[c] != '#' != coords[c+d]:
#             G.add_edge(c, c+d)

# S = [c for c in coords if coords[c] in 'S'][0]
# coord_to_dist = nx.shortest_path_length(G, S).items()


    # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

def secret(num):
    mod10 = []
    price = []
    print(num)
    for i in range(2000):
        prev = num
        num ^= num * 64
        num %= 16777216
        num ^= num // 32
        num %= 16777216
        num ^= num * 2048
        num %= 16777216
        mod10.append((num%10 - prev%10))
        price.append(num%10)
        # print(f"{num}   {num%10=}   {num%10-prev%10=}")
    return mod10, price


c = Counter()
for line in open(0):
    n = int(line)
    # s1 += secret(n)
    a, price = secret(n)
    # print(a[:20])
    # print(price[:20])
    seen = set()
    for i, (t, p) in enumerate(zip(zip(a, a[1:], a[2:], a[3:]), price[3:])):
        if t not in seen:
            seen.add(t)
            c[t] += p
    # exit()
print(c.most_common(20))
print(c[(-2,1,-1,3)])


    # re.findall(r"\d+", line)
    

print(s1, s2, sep="\n")
