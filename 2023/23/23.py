import sys
sys.setrecursionlimit(1000000000)
from collections import deque

lines = open(0).read().splitlines()
Y, X = len(lines), len(lines[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

max_dist = 0
def dfs(y, x, dist, visited, part2=False):
    global max_dist
    if (y, x) == (Y-1, X-2):
        if dist > max_dist:
            # Prints all current largest paths. After a couple minutes it finds the correct answer
            # However it does not finish within half an hour.
            print(dist)  
            max_dist = dist

    adj = []
    for i, (dy, dx) in enumerate(dirs):
        ya, xa = y+dy, x+dx
        if 0 <= ya < Y and 0 <= xa < X and lines[ya][xa] != '#' and (ya, xa) not in visited:
            adj.append((ya, xa))
            if not part2 and lines[ya][xa] in '>v<^' and '>v<^'.index(lines[ya][xa]) == i:
                continue
    if len(adj) == 1:
        visited.add(adj[0])
        dfs(adj[0][0], adj[0][1], dist+1, visited)
    elif len(adj) > 1:
        for a in adj:
            dfs(a[0], a[1], dist+1, visited | {a})

dfs(0, 1, 0, {(0, 1)})
dfs(0, 1, 0, {(0, 1)}, part2=True)
