from collections import defaultdict
import random
import networkx as nx

g = nx.Graph()
for line in open(0):
    at, tos = line.split(":")
    for to in tos.strip().split(' '):
        g.add_edge(at, to, capacity=1)

while True:
    start = random.choice(list(g.nodes))
    end = random.choice(list(g.nodes))
    cut, part = nx.minimum_cut(g, start, end)
    if cut == 3:
        print(len(part[0])*len(part[1]))
        break
