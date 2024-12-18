from collections import *
from itertools import *
from functools import *
import networkx as nx
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


all_obstacles = []

for line in open(0):
    x,y = map(int, line.split(","))
    all_obstacles.append(x+y*1j)

for limit in range(3000, 99999999):
    G = nx.DiGraph()
    try:
        obstacles = all_obstacles[:limit]
        S = 70

        coords = {x+1j*y: '#' if x+1j*y in obstacles else '.'  for y in range(S+1) for x in range(S+1)}

        # print(coords)
        # print(coords.get(0+0j))
        # print(coords.get(S+S*1j))

        for c in coords:
            for adj in adjacent(c):
                if coords[c] == '.' and coords.get(adj) == '.':
                    G.add_edge(c, adj)

#         for y in range(S+1):
#             for x in range(S+1):
#                 print(end=coords.get(x+y*1j))
#             print()

        print(len(nx.shortest_path(G, 0, S+S*1j)))
    except:
        print(limit, obstacles[limit-1])
        exit(0)



# for line in open(0):
#     n = [int(a) for a in line.split()]
    # re.findall(r"\d+", line)
    

# print(s1, s2, sep="\n")
