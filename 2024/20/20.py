import networkx as nx
from collections import *


coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip().replace(".", " "))}

d4 = [1, 1j, -1, -1j]

G = nx.Graph()
for c in coords:
    for d in [1, 1j, -1, -1j]:
        if coords[c] != '#' != coords[c+d]:
            G.add_edge(c, c+d)
            # G.add_edge((c, 1), (c+d, 1))

S = [c for c in coords if coords[c] in 'S'][0]
E = [c for c in coords if coords[c] in 'E'][0]
# EL = nx.shortest_path_length(G, target=E)
SL = nx.shortest_path_length(G, source=S)
print(SL)
# print(EL)
C= Counter()

sl = list(SL.items())
seen = set()
s2 = 0
for i, (c1, dist1) in enumerate(sl):
    for c2, dist2 in sl[i+1:]:
        diff = c2-c1
        diff = int(abs(diff.real) + abs(diff.imag))
        if diff <= 20:
            D = dist2 - dist1 - diff
            if D > 0:
                C[D] += 1
            if D >= 100:
                s2 += 1

for asd in sorted(C.items()):
    print(asd)

print(s2)
exit()
# L = {l: max(EL[l], SL[l]) for l in EL}

for c in coords:
    for d in [1, 1j, -1, -1j]:
        if coords[c] != '#' != coords[c+d]:
            G.add_edge(c, c+d)
            G.add_edge((c, 1), (c+d, 1))

# L = [el+sl for ]

# print(L)
# print(L[S])
# exit(0)

C = Counter()

s1 = 0
seen= set()
for c in coords:
    for d in [1, 1j, -1, -1j]:
        for d2 in [d]:
            diff = 0
            for d3 in [0]:
                c2 = c+d+d2+d3
                if c2 in coords and coords[c] != '#' != coords[c2] and c != c2:
                    delta = d+d2+d3
                    new = SL[c2] - SL[c] - int(abs(delta.imag) + abs(delta.real))
                    print("\t", d3, new)
                    diff = max(diff, new)
            if (c, c+d+d2) not in seen and diff > 0:
                seen.add((c, c+d+d2))
                seen.add((c+d+d2, c))
                if diff > 0:
                    # print(c, c2)
                    C[diff] += 1
                if diff >= 30:
                    print(diff)
                    for y in range(15):
                        for x in range(15):
                            X=x+y*1j
                            print(end=coords[X] if X not in [c, c+d+d2] else "!")
                            print(end=f"{SL.get(X, '##'):2}")
                        print()
                    print()
                if diff >= 100:
                    s1 += 1


for asd in sorted(C.items()):
    print(asd)

# 536
# 677
# 1923


# for path in nx.all_simple_paths(G, S, (E, 1), cutoff=L):
#     if L - len(path) >= 100:
#         s1 += 1
print(s1)
# paths = list(nx.all_shortest_paths(G, S, (E, 0), "weight"))

# print(sum(G.edges[e]["weight"] for e in zip(paths[0], paths[0][1:])))
# print(len({p[0] for p in sum(paths, [])}))
