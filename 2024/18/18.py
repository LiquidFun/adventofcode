import networkx as nx
from bisect import bisect

def solve(obstacles, S=70):
    G = nx.grid_graph((S+1, S+1))
    G.remove_nodes_from(obstacles)
    return nx.has_path(G, (0,0), (S,S)) \
           and len(nx.shortest_path(G, (0,0), (S,S)))

obstacles = [tuple(map(int, line.split(","))) for line in open(0)]
print(solve(obstacles[:1024])-1)

index = bisect(range(len(obstacles)), 0, key=lambda x: not solve(obstacles[:x]))
print(*obstacles[index-1], sep=",")
