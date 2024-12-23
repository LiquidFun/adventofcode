import networkx as nx

G = nx.Graph(line.strip().split("-") for line in open(0))
cliques = list(nx.enumerate_all_cliques(G))

print(sum(any(a[0]=='t' for a in c) for c in cliques if len(c) == 3))
print(','.join(sorted(cliques[-1])))
