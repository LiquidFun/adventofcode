import networkx as nx
coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

G = nx.DiGraph()
for c in coords:
    for d in [1, 1j, -1, -1j]:
        G.add_edge((c, d), (c, 0), weight=0)
        G.add_edge((c, 0), (c, d), weight=1000)
        if coords[c] != '#' != coords[c+d]:
            G.add_edge((c, d), (c+d, d), weight=1)

E, S = [c for c in coords if coords[c] in 'SE']

paths = list(nx.all_shortest_paths(G, (S, 1), (E, 0), "weight"))

print(sum(G.edges[e]["weight"] for e in zip(paths[0], paths[0][1:])))
print(len({p[0] for p in sum(paths, [])}))
