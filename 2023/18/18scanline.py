from sys import stdin
from collections import defaultdict

lines = stdin.read().splitlines()
dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}

def solve(instructions):
    y = x = s = 0
    y_vis = defaultdict(list)
    x_vis = defaultdict(list)
    for d, num in instructions:
        if d in "RL":
            x_prev = x
            x += num * dirs[d][1]
            s += abs(x_prev - x) - 1
            x_vis[y].append(sorted([x_prev, x]))
        else:
            ynext = y + num * dirs[d][0]
            for ya in range(min(ynext, y), max(ynext, y)+1):
                y_vis[ya].append((x, d))
            y = ynext

    for y, xs in y_vis.items():
        xs.sort()
        curr, d = xs[0]
        indices = [0]
        for i, ((_, d1), (_, d2)) in enumerate(zip(xs, xs[1:])):
            if d1 != d2 and d2 == xs[0][1]:
                indices.append(i+1)
        indices.append(len(xs))
        for i1, i2 in zip(indices, indices[1:]):
            x1, d1 = xs[i1]
            x2, d2 = xs[i2-1]
            for a1, a2 in x_vis[y]:
                if x1 <= a1 < a2 <= x2:
                    s -= a2 - a1 - 1  # Remove x line which were counted twice
            s += x2 - x1 + 1
    return s


split = [line.split() for line in lines]
print(solve([(d, int(num)) for d, num, _ in split]))
print(solve([("RDLU"[int(c[-2])], int(c[2:-2], 16)) for *_, c in split]))
