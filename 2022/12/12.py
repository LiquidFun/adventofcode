import sys, collections

field = sys.stdin.read().strip().split("\n")
S = next((i, f.index('S')) for i, f in enumerate(field) if "S" in f)
E = next((i, f.index('E')) for i, f in enumerate(field) if "E" in f)
field = ' '.join(field).replace("S", "a").replace("E", "z").split()
best_from_start = {}
is_valid = lambda y, x: 0 <= y < len(field) and 0 <= x < len(field[0])
for sy, sx in [(sy, sx) for sy in range(len(field)) for sx in range(len(field[0]))]:
    if field[sy][sx] == 'a':
        queue = collections.deque([(sy, sx)])
        dist = {(sy, sx): 0}
        while queue:
            y, x = queue.popleft()
            for y2, x2 in [(y+ya, x+xa) for ya, xa in [(1, 0), (-1, 0), (0, 1), (0, -1)]]:
                if is_valid(y2, x2) and (y2, x2) not in dist:
                    if ord(field[y2][x2]) <= ord(field[y][x]) + 1:
                        dist[(y2, x2)] = dist[(y, x)] + 1
                        queue.append((y2, x2))
        best_from_start[(sy, sx)] = dist.get(E, 1e9)
print(best_from_start[S])
print(min(best_from_start.values()))

