import networkx as nx
from bisect import bisect

def solve(bad, S=70):
    G = nx.grid_graph((S+1, S+1))
    G.remove_nodes_from(bad)
    return nx.has_path(G, (0,0), (S,S)) \
       and nx.shortest_path_length(G, (0,0), (S,S))

bad = [tuple(map(int, line.split(","))) for line in open(0)]
print(solve(bad[:1024]))

i = bisect(range(len(bad)), 0, key=lambda x: not solve(bad[:x]))
print(*bad[i-1], sep=",")
