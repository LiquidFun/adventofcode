import networkx as nx

def solve(obstacles, S=70):
    G = nx.DiGraph()
    for c in {x+1j*y for y in range(S+1) for x in range(S+1)}:
        for d in [1, 1j, -1, -1j]:
            if c not in obstacles and c+d not in obstacles:
                G.add_edge(c, c+d)

    return nx.has_path(G, 0, S+S*1j) and len(nx.shortest_path(G, 0, S+S*1j))

obstacles = [complex(line.replace(",", "+")+"j") for line in open(0)]
print(solve(obstacles[:1024]))

lo, hi = 1024, len(obstacles)-1
while lo < hi:
    mid = (lo + hi) // 2
    if solve(obstacles[:mid]): lo = mid+1
    else: hi = mid-1

print(str(obstacles[mid]).replace("+", ",")[1:-2])
