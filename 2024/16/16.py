import networkx as nx
coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

G = nx.DiGraph()

for c in coords:
    if coords[c] == '#': continue
    for d in [1, 1j, -1, -1j]:
        G.add_edge((c, d), c, weight=0)
        G.add_edge(c, (c, d), weight=1000)
        if coords[c+d] != '#':
            G.add_edge((c, d), (c+d, d), weight=1)

S = [c for c in coords if coords[c] == 'S'][0]
E = [c for c in coords if coords[c] == 'E'][0]

all_paths = list(nx.all_shortest_paths(G, (S, 1), E, "weight"))
path = all_paths[0]
print(sum(G.edges[edge]["weight"] for edge in zip(path, path[1:])))

flat = sum(all_paths, [])
nodes = {(p[0] if isinstance(p, tuple) else p) for p in flat}
print(len(nodes))
