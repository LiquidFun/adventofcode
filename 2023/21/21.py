from collections import deque

lines = open(0).read().splitlines()
Y, X = len(lines), len(lines[0])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = deque()
dists = {}

for y, line in enumerate(lines):
    if 'S' in line:
        q.append((y, line.index('S')))

while q:
    y, x = q.popleft()
    for dy, dx in dirs:
        ya, xa = y + dy, x + dx
        if 0 <= ya < Y and 0 <= xa < X and lines[ya][xa] != '#' and (ya, xa) not in dists:
            dists[(ya, xa)] = dists.get((y, x), 0)+1
            q.append((ya, xa))

n = 26501365 // X

even_full = sum(d % 2 == 0 for d in dists.values())
odd_full = sum(d % 2 == 1 for d in dists.values())
even_edges = sum(d % 2 == 0 and d > 65 for d in dists.values())
odd_edges = sum(d % 2 == 1 and d > 65 for d in dists.values())

print(even_full - even_edges)

p2 = (n+1)**2 * odd_full + n**2 * even_full - (n+1) * odd_edges + n * even_edges
print(p2)
