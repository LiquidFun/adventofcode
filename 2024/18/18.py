import networkx as nx

def solve(obstacles, S=70):
    G = nx.grid_graph((S+1, S+1))
    G.remove_nodes_from(obstacles)
    return nx.has_path(G, (0,0), (S,S)) \
           and len(nx.shortest_path(G, (0,0), (S,S)))

obstacles = [tuple(map(int, line.split(","))) for line in open(0)]
print(solve(obstacles[:1024])-1)

lo, hi = 1024, len(obstacles)-1
while lo < hi:
    mid = (lo + hi) // 2
    if solve(obstacles[:mid]): lo = mid+1
    else: hi = mid-1

print(*obstacles[mid], sep=",")
