dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(instructions, s=0):
    ys, xs = [0], [0]
    for d, num in instructions:
        s += num
        ys.append(ys[-1] + num * dirs[d][0])
        xs.append(xs[-1] + num * dirs[d][1])

    for i in range(len(ys)):  # Shoelace formula
        s += ys[i] * xs[i-1] - xs[i] * ys[i-1]
    print(s // 2 + 1)

split = [line.split() for line in open(0)]
solve([("RDLU".index(d), int(num)) for d, num, _ in split])
solve([(int(c[-2]), int(c[2:-2], 16)) for *_, c in split])
