from sys import stdin

DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

lines = [list(line.strip()) for line in stdin]

Y, X = len(lines), len(lines[0])
coords = [(y, x) for y in range(Y) for x in range(X)]

def find_o_coords():
    return [(y, x) for y, x in coords if lines[y][x] == 'O']

seen = {}

for i in range(1, 10000):
    for yd, xd in DIRS:
        for y, x in find_o_coords():
            ybest, xbest = yo, xo = y, x
            while 0 <= y < Y and 0 <= x < X and lines[y][x] != '#':
                if lines[y][x] == '.':
                    ybest, xbest = y, x
                y, x = y+yd, x+xd
            lines[yo][xo], lines[ybest][xbest] = lines[ybest][xbest], lines[yo][xo]

        load_on_beams = sum(Y-y for y, _ in find_o_coords())
        if i == 1 and (yd, xd) == DIRS[0]:
            print(load_on_beams)

    if str(lines) in seen:
        repeat_interval = i - seen[str(lines)]
        if (1_000_000_000 - i) % repeat_interval == 0:
            print(load_on_beams)
            exit()
    seen[str(lines)] = i
