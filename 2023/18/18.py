dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(instructions, s=0, y=0, x=0):
    for d, num in instructions:
        y2 = y + num * dirs[d][0]
        x2 = x + num * dirs[d][1]
        s += num + (y2*x - x2*y)  # Border + Shoelace formula
        y, x = y2, x2
    print(s // 2 + 1)

split = [line.split() for line in open(0)]
solve(("RDLU".index(d), int(num)) for d, num, _ in split)
solve((int(c[7]), int(c[2:7], 16)) for *_, c in split)
