from sys import stdin
import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, product, combinations_with_replacement
from queue import PriorityQueue

lines = stdin.read().strip().split('\n')
Y, X = len(lines), len(lines[0])
# dirs = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
dirs = {"0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}

s = 0
y = x = 0
visited = {(y, x)}
y_vis = defaultdict(list)
x_vis = defaultdict(list)
# y_vis[y].append(x)
for line in lines:
    _, _, color = line.split()
    _, _, *five, d, _ = color
    num = int(''.join(five), 16)
    print(line)
    print(num, d)
    if d in "02":
        x_prev = x
        # x_vis[y].append(x)
        x += num * dirs[d][1]
        # y_vis[y].append(x)
        s += abs(x_prev - x) - 1
        x_vis[y].append(sorted([x_prev, x]))
        if y == 56407:
            print(f'\t LR {num=} {d=} {x=} {y=}')
    else:
        ynext = y + num * dirs[d][0]
        if d == "1":
            assert y < ynext
            r = range(ynext, y-1, -1)
            # r = range(ynext-1, y, -1)
        else:
            assert y > ynext
            r = range(ynext, y+1)
            # r = range(ynext+1, y)
        for ya in r:
            # assert ya != y
            y_vis[ya].append((x, d))
            if ya == 56407:
                print(f'\t UD {num=} {d=} {x=} {ynext=} {ya=} {y=}')
        y = ynext
        #y_vis
    print()
    # num = int(num)
    # for i in range(num):
    #     y += dirs[d][0]
    #     x += dirs[d][1]
    #     visited.add((y, x))

    # line

for y, xs in y_vis.items():
    # print(y, xs)
    # assert len(xs) % 2 == 0, xs
    # assert len(xs) % 2 == 0 and len(xs) >= 5, xs
    xs.sort()
    curr, d = xs[0]
    skip = False
    new = []
    last_d = None
    # for curr, d in reversed(xs):
    #     if d != last_d:
    #         new.append(curr)
    #         last_d = d
    d_first = xs[0][1]
    # is_split = [False] * len(xs)
    indices = [0]
    if len(xs) % 2 != 0:
        print(y, xs)
    for x, ((_, d1), (_, d2)) in enumerate(zip(xs, xs[1:])):
        if d1 != d2 and d2 == d_first:
            indices.append(x+1)
    indices.append(len(xs))
    for i1, i2 in zip(indices, indices[1:]):
        x1, d1 = xs[i1]
        x2, d2 = xs[i2-1]
        for a1, a2 in x_vis[y]:
            print("AAAAA", a1, a2)
            if x1 <= a1 < a2 <= x2:
                print("AAAAAAAAAAAA", a1, a2)
                s -= a2 - a1 - 1
        if len(xs) % 2 != 0:
            print(f"{x1=} {x2=} {d1=} {d2=}")
        assert d1 != d2, xs
        s += x2 - x1 + 1
    # for nex, d2 in xs[1:]:
    #     if skip:
    #         skip = False
    #         continue
    #     if d2 != d:
    #         s += nex - curr + 1

    # xs = list(reversed(new))
    # print(y, xs)
    # assert xs == sorted(xs)
    # assert len(xs) % 2 == 0, xs
    # for x1, x2 in zip(xs[::2], xs[1::2]):
    #     s += x2 - x1 + 1

    #for x1, x2 in zip(xs[::2], xs[1::2]):
    #    s += x2 - x1 + 1

# y = x = 0
# q = deque([(y-1, x)])
# while q:
#     y, x = q.popleft()
#     visited.add((y, x))
#     for dy, dx in dirs.values():
#         ya, xa = y+dy, x+dx
#         if (ya, xa) not in visited:
#             visited.add((ya, xa))
#             q.append((ya, xa))
# 
# print(len(visited))

print(s)
