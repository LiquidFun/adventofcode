import networkx as nx

coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

G = nx.Graph()
for c in coords:
    for d in [1, 1j, -1, -1j]:
        if coords[c] != '#' != coords[c+d]:
            G.add_edge(c, c+d)

S = [c for c in coords if coords[c] in 'S'][0]
coord_to_dist = nx.shortest_path_length(G, S).items()

s1 = s2 = 0
for c1, dist1 in coord_to_dist:
    for c2, dist2 in coord_to_dist:
        diff = int(abs((c2-c1).real) + abs((c2-c1).imag))
        if dist2 - dist1 - diff >= 100:
            s1 += diff <= 2
            s2 += diff <= 20

print(s1, s2, sep="\n")  # use pypy instead of python
