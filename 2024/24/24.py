from collections import *
from itertools import *
from functools import *
import numpy as np
import networkx as nx
from operator import *
import operator
import z3
import re
import sys
sys.setrecursionlimit(1000000)

s1 = s2 = 0
# coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

# d4 = [1, 1j, -1, -1j]
# d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
# d4half = [i/2 for i in d4]
# d8half = [i/2 for i in d8]
# def adjacent(coord, dirs=d4):
#     return [coord + d for d in dirs]



initial, instructions = open(0).read().split("\n\n")
initial = initial.split("\n")
instructions = instructions.strip().splitlines()
instructions = [a.split() for a in instructions]
import random
# random.seed(42)

def solve(modify=None):
    states = {}
    XX = []
    YY = []
    for line in sorted(initial):
        a,b = line.split(":")
        # b = "0" if a[0] == "x" else "1"
        # b = "1"
        if modify == "flip":
            b = str(1-int(b))
        if modify == "one":
            b = "1"
        if modify == "random":
            b = str(random.randint(0, 1))
        states[a] = int(b)
        if line[0] == 'x':
            XX.append(b.strip())
        if line[0] == 'y':
            YY.append(b.strip())

    XX = ''.join(XX[::-1])
    YY = ''.join(YY[::-1])
    X = int(XX, 2)
    Y = int(YY, 2)
    Z = bin(X + Y)[2:]

    to_op = {
        "AND": and_,
        "XOR": xor,
        "OR": or_,
    }

    target_to_op = defaultdict(list)
    G = nx.DiGraph()

    prev_z = set()
    for a, op, b, _, target in instructions:
        if target in swap:
            target = swap[target]
        target_to_op[target].append((a,op,b))
        G.add_edge(a, target)
        G.add_edge(b, target)
        if target[0] == 'z':
            prev_z |= {a,b}

        # G.add_edge(a, (a, op, b))
        # G.add_edge(b, (a, op, b))
        # G.add_edge((a, op, b), target)
        # if a in states and b in states and target not in seen:
        #     assert target not in states
        #     states[target] = to_op[op](states[a], states[b])
        #     print(target, len(seen))
        #     seen.add(target)



    # "kth", "tgs", 

    seen = set()
    last = 0
    while len(seen) != len(instructions):
        for a, op, b, _, target in instructions:
            if target in swap:
                target = swap[target]
            if a in states and b in states and target not in states:
                # assert target not in states
                states[target] = to_op[op](states[a], states[b])
                # print(target, len(seen))
                seen.add(target)
        if last == len(seen):
            return list(range(46))
        last = len(seen)

    # print(states)
    z = []
    for var, state in sorted(states.items()):
        if var.startswith("z"):
            # print(var, state)
            z.append(str(int(state)))


    #70364449079294 too high
    Z_real = ''.join(z[::-1])
    ans = int(Z_real, 2)
    # print(ans)


    wrong = []
    for i, (z1, z2) in enumerate(zip(Z[::-1], Z_real[::-1])):
        if z1 != z2:
            # print(i)
            wrong.append(i)


    if True:

        xy = sorted({i.split(":")[0] for i in initial}, key=lambda x: 1000*int(x[1:])+ord(x[0]))
        print(xy)
        pos = nx.bfs_layout(G, xy)
        print(pos)

        colors = []
        for node in G.nodes:
    
            if node in "fgt,fpq,nqk,pcp,srn,z07,z24,z32".split(","):
                colors.append("red")
                # G.nodes[node]["color"] = "red"
                # G.nodes[node]["c"] = "red"
            else:
                colors.append("blue")

        for key, p in pos.items():
            if key[0] in "xyz":
                p += np.array([0.001, 0])

            if key in prev_z:
                p -= np.array([0.001, 0])

        print(len(colors))
        print(len(G.nodes))
        nx.draw_networkx(G, pos=pos, node_color=colors)
        from matplotlib import pyplot as plt
        plt.show()
        exit(0)
    return wrong

    # for line in open(0):
    #     n = [int(a) for a in line.split()]
        # re.findall(r"\d+", line)
        

    print(s1, s2, sep="\n")




nodes = set()
for a, op, b, _, target in instructions:
    nodes |= {a, b, target}

nodes = list(nodes)
for n in list(nodes):
    if n[0] in 'xy':
        nodes.remove(n)
# print(nodes)
best = []
from tqdm import tqdm
for a,b in tqdm(list(combinations(nodes, r=2))):
    # (0, 0, 0, 0, ('btq', 'jss')), 
    # (0, 0, 0, 0, ('nqk', 'jss')), 
    # (0, 0, 0, 0, ('nqk', 'z07'))
    swap = {
        "fpq": "z24", # GOOD
        "srn": "z32", # PROBABLY
        'nqk': 'z07', # MAYBE
        "pcp": "fgt",
        # a: b,
        # "nmq": "pcp",
        # 'jnv': 'dpm',
    }
    swap = {}
    ans = []

    for a_,b_ in list(swap.items()):
        ans.append(a)
        ans.append(b)
        swap[b_] = a_
    print(','.join(sorted(swap)))
    s = solve()
    s2 = solve("flip")
    s3 = solve("one")
    s4 = max([solve("random")] for _ in range(50))
    print(a,b, s, s2, s3, s4)
    exit()
    if len(s) > 10: continue
    best.append((len(s), len(s2), len(s3), len(s4), (a,b)))
    best.sort()
    print(best[:10])

print(sorted(best)[:20])

