from collections import *
from itertools import *
from queue import *
from functools import *
import networkx as nx
import re
import sys
sys.setrecursionlimit(1000000)

s1 = s2 = 0
coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

d4 = [1, 1j, -1, -1j]
d8 = [1+1j, 1-1j, -1+1j, -1-1j]
d4half = [i/2 for i in d4]
d8half = [i/2 for i in d8]
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]

G = nx.DiGraph()

S = [c for c in coords if coords[c] == 'S'][0]
E = [c for c in coords if coords[c] == 'E'][0]

q = Queue()
# q.put((S, 1))
# for d in d4: 
#     q.put((S, d))
#     if coords[S+d] != '#':
#         G.add_edge(S, S+d, weight=1 if d==1 else 1002)

for c in coords:
    if coords[c] == '#': continue
    for d in d4:
        G.add_edge((c, d), c, weight=0)
        G.add_edge(c, (c, d), weight=1000)
        if coords[c+d] != '#':
            G.add_edge((c, d), (c+d, d), weight=1)
        # for D in d4:
        #     G.add_edge((c, d), (c, D), weight=1000 * (d != D))



# while not q.empty():
#     c, dir = q.get()
#     print(c, dir)
#     for d in d8 + ([dir] if c != S else d4):
#         if coords[c+d] != '#' and (c, c+d) not in G.edges:
#             G.add_edge(c, c+d, weight=1 if dir==d else 1002)
#             q.put((c+d, (d if d==dir else d-dir)))

all_paths = list(nx.all_shortest_paths(G, (S, 1), E, "weight"))
path = all_paths[0]
print(sum(G.edges[edge]["weight"] for edge in zip(path, path[1:])))

print("shortest path")
flat = sum(all_paths, [])
nodes = {(p[0] if isinstance(p, tuple) else p) for p in flat}
# print(len(nx.shortest_path(G, (S, 1), E, "weight")))
print(len(nodes))
exit(0)



best = 1e9
best_paths = {}

K = 0

def tie(curr, num=[0]):
    tie[0] += 1
    return tie[0] - 1e9 * (curr in best_paths)

for i in range(2):

    queue = PriorityQueue()
    queue.put((0, 0, 0, 0, S.real, S.imag, (K:=K+1), {(S,1):0}))

    visited = {S}


    while queue.not_empty:
        cost, forward, turns, dir, real, imag, _, path = queue.get()
        dir = d4[dir]
        curr = real + 1j * imag
        if coords[curr] == 'E':
            # visited.remove(curr)
            best = cost
            best_paths |= path
            print(len(best_paths))
            print(cost)

        if cost > best:
            if i == 1: exit(0)
            else: break
        for d in d4:
            n = curr+d
            is_f = dir==d 
            forward2 = forward + 1
            turns2 = turns + (not is_f)
            cost2 = forward2 + turns2 * 1000
            path2 = path | {(n, d): cost2}
            if best_paths.get((n, d)) == cost2:
                print(n, cost2, "!=", best_paths.get((n, d)))
                best_paths |= path2
                print(len(best_paths))
            if coords[n] != '#' and (n not in visited or i == 1 and (n, d) not in path):
                visited.add(n)
                queue.put((cost2, forward2, turns2, d4.index(d), n.real, n.imag, (K:=K+1), path2))
                






# for line in open(0):
#     n = [int(a) for a in line.split()]
    # re.findall(r"\d+", line)
    

print(s1, s2, sep="\n")
