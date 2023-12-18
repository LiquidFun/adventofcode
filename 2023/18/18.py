from sys import stdin

lines = stdin.read().splitlines()
dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

def solve(instructions, s=0):
    ys, xs = [0], [0]
    for d, num in instructions:
        s += num
        ys.append(ys[-1] + num * dirs[d][0])
        xs.append(xs[-1] + num * dirs[d][1])

    # Polygon area: Shoelace algorithm
    for i in range(len(ys)-1, -1, -1):
        s += ys[i] * xs[i-1] - xs[i] * ys[i-1]
    return s // 2 + 1

split = [line.split() for line in lines]
print(solve([(d, int(num)) for d, num, _ in split]))
print(solve([("RDLU"[int(c[-2])], int(c[2:-2], 16)) for *_, c in split]))
