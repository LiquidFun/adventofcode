import sys
sys.setrecursionlimit(10000000)

lines = sys.stdin.read().strip().split('\n')

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
Y, X = len(lines), len(lines[0])

def go(y, x, d, visited, return_energized=True):
    if 0 <= y < Y and 0 <= x < X and (y, x, d) not in visited:
        visited.add((y, x, d))
        go_dir = lambda d: go(y+d[0], x+d[1], d, visited, False)
        match lines[y][x]:
            case '/':
                go_dir((-d[1], -d[0]))
            case '\\':
                go_dir((d[1], d[0]))
            case '|':
                go_dir(dirs[1])
                go_dir(dirs[3])
            case '-':
                go_dir(dirs[0])
                go_dir(dirs[2])
            case _:
                go_dir(d)
    if return_energized:
        return len({(y, x) for y, x, _ in visited})

p2 = []
for y in range(Y):
    for x in range(X):
        for is_edge, (dy, dx) in zip((x == 0, y == 0, x == X-1, y == Y-1), dirs):
            if is_edge:
                p2 += [go(y, x, (dy, dx), set())]

print(go(0, 0, dirs[0], set()))
print(max(p2))
