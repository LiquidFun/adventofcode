from sys import stdin
lines = [[list(map(int, c.split(','))) for c in l.strip().split(" -> ")] for l in stdin.readlines()]
width = max(x+200 for x, _ in sum(lines, []))
height = max(y for _, y in sum(lines, []))

def solve(floor='.'):
    field = [['.'] * width for _ in range(height + 2)] + [[floor] * width]
    for walls in lines:
        for (x1, y1), (x2, y2) in zip(walls, walls[1:]):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    field[y][x] = '#'

    while True:
        sx, sy = 500, 0
        while sy+1 < len(field):
            for xa in (0, -1, 1):
                if field[sy+1][sx+xa] == '.':
                    sy, sx = sy+1, sx+xa
                    break
            else:
                field[sy][sx] = 'o'
                break
        if sy+1 >= len(field) or field[0][500] == 'o':
            return sum(field, []).count("o")

print(solve(floor='.'))
print(solve(floor='#'))
