import networkx as nx

G = nx.Graph(line.strip().split("-") for line in open(0))
cliques = list(nx.enumerate_all_cliques(G))

has_t0 = lambda clique: any(a[0]=='t' for a in clique)
print(sum(has_t0(c) for c in cliques if len(c) == 3))
print(','.join(sorted(cliques[-1])))
