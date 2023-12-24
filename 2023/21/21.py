import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, product, combinations_with_replacement
from queue import PriorityQueue

lines = open(0).read().splitlines()
Y, X = len(lines), len(lines[0])
S = Y
assert Y == X
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirs_diag = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

q = deque()

dists = {}
for y, line in enumerate(lines):
    if 'S' in line:
        q.append((y, line.index('S')))
        dists[(y, line.index('S'))] = 0

s = 0
# for i in range(64):
# nextq = deque()
visited = set()
nextq = deque()
while q:
    y, x = q.popleft()
    for dy, dx in dirs:
        ya, xa = y + dy, x + dx
        in_inner = 0 <= ya < Y and 0 <= xa < X
        in_outer = -Y*2 <= ya < Y*3 and -X*2 <= xa < X*3
        if in_outer and lines[ya%Y][xa%X] != '#':  # and (ya, xa) not in visited:
            # ok = True
            # if (ya, xa) in dists:
            #     di, do = dists[(ya, xa)]
            #     ok = dist_outer+(not in_inner) < do
            # if ok:
            if (ya, xa) not in visited:
                # dists[(ya, xa)] = (dist_inner + in_inner, dist_outer + (not in_inner))
                dists[(ya, xa)] = dists[(y, x)]+1
                if in_inner:
                    q.append((ya, xa))
                else:
                    nextq.append((ya, xa))
            visited.add((ya, xa))
    if not q:
        q = nextq

    # q = nextq

# print(dists)
# print(len(dists))

for y in range(-Y*2, Y*3):
    if y % Y == 0:
        print('-' * (15*S))
    # for x in range(-X*2, X*3):
    for x in range(0, X):
        v = '#'
        if (y, x) in dists:
            dist = dists[(y, x)]
            # yadd = 0 if (y == y%Y) else (Y if (y > y%Y) else -Y)
            # xadd = 0 if (x == x%X) else (X if (x > x%X) else -X)
            # veryouter_dist = dists[(y+yadd, x+xadd)]
            # repeat = veryouter_dist - dist
            # repeat = do
            # v = str('Y' if dist % 2== 1 else ' ')
            v = str(dist)
            v = v.replace("(", "").replace(",", "").replace(")", "").replace(" ", "-")
        print(end=f"{v:3}" + ('| ' if x in (-X-1, -1, X-1, 2*X-1) else ''))
    print()


# for direction in dirs:
# for y in range(-Y, Y*2):
#     for x in range(-X, X*2):
#         if (y, x) in dists:
#             in_inner = 0 <= y < Y and 0 <= x < X
#             dist = dists[(y, x)]
#             # inner_di, _ = dists[(y%Y, x%X)]
#             if in_inner:
#                 if dist % 2 == mod and dist <= target:
#                     s += 1
#             else:
#                 new = max(-1, (target - dist))
#                 if new >= 0:
#                     print(y, x, new, target, dist)
#                     if new % 2 == mod:
#                         if not (0 <= y < Y or 0 <= x < X):
#                             div = S*2
#                             s += new // (S*2) + 1
#                         else:
#                             div = S
#                             s += new // S + 1
#             if not (0 <= y < Y or 0 <= x < X):
#                 for side in [-1, 1]:
#                     for i, rem in enumerate(range(target - S * 1, -S*2, -S*2)):
#                         new = max(-1, (rem - dist))
#                         if new >= 0:
#                             if new % 2 == mod:
#                                 # print(f"add {new=} {S=} {dist=} {new // S=}")
#                                 s += (new) // S // 2 + 1
#                             if new % 2 == (not mod):
#                                 # print(f"add {new=} {S=} {dist=} {new // S=}")
#                                 s += (new) // S // 2

#     In exactly 6 steps, he can still reach 16 garden plots.
#     In exactly 10 steps, he can reach any of 50 garden plots.
#     In exactly 50 steps, he can reach 1594 garden plots.
#     In exactly 100 steps, he can reach 6536 garden plots.
#     In exactly 500 steps, he can reach 167004 garden plots.
#     In exactly 1000 steps, he can reach 668697 garden plots.
#     In exactly 5000 steps, he can reach 16733044 garden plots.

target = 26501365
# target = 100
mod = target % 2

curr_sum = 0
next_sum = 0
for y in range(0, Y):
    for x in range(0, X):
        if (y, x) in dists:
            curr_sum += dists[(y, x)] % 2 == mod
            next_sum += dists[(y, x)] % 2 == (not mod)

print(curr_sum, next_sum)
# s = next_sum * sum(range(1, target // S, 2)) * 4 + curr_sum * ((sum(range(0, target // S, 2))) * 4 + 1)
# s = curr_sum * sum(range(1, target // S, 2)) * 4 + next_sum * ((sum(range(0, target // S, 2))) * 4 + 1)

s += next_sum * 4
s += curr_sum * 4
s += next_sum * 8

# Visited is a HashMap<Coord, usize> which maps tiles in the input-square to their distance from the starting tile
# So read this as "even_corners is the number of tiles which have a distance that is even and greater than 65"
let even_corners = visited.values().filter(|v| **v % 2 == 0 && **v > 65).count();
let odd_corners = visited.values().filter(|v| **v % 2 == 1 && **v > 65).count();

let even_full = visited.values().filter(|v| **v % 2 == 0).count();
let odd_full = visited.values().filter(|v| **v % 2 == 1).count();

// This is 202300 but im writing it out here to show the process
let n = ((26501365 - (env.dim.0 / 2)) / env.dim.0) as usize;
assert_eq!(n, 202300);

let p2 = ((n+1)*(n*1)) * odd_full + (n*n) * even_full - (n+1) * odd_corners + n * even_corners;


for x1, x2, y1, y2 in [(0, X, -Y*2, -Y), (0, X, Y*2, Y*3), (-X*2, -X, 0, Y), (X*2, X*3, 0, Y)]:
    for y in range(y1, y2):
        for x in range(x1, x2):
            if (y, x) in dists:
                d = dists[(y, x)]
                for times in range(target // S+10):
                    num = d + S * times
                    if num <= target:
                        s += num % 2 == mod

for xlims, ylims in [((-X*2, -X), (-Y*2, -Y)), ((X*2, X*3), (-Y*2, -Y)), ((X*2, X*3), (Y*2, Y*3)), ((-X*2, -X), (Y*2, Y*3))]:
    for y in range(*ylims):
        for x in range(*xlims):
            if (y, x) in dists:
                d = dists[(y, x)]
                for times in range(target // S+10):
                    num = d + S * times
                    if num <= target:
                        s += (num % 2 == mod) * (times+3)

                # num = (dists[(y, x)] - S * 2) + (target // S) * S
                # if num <= target:
                #     s += (num % 2 == (not mod)) * (target // S - 2)

                # num = (dists[(y, x)] - S * 3) + (target // S) * S
                # if num <= target:
                #     s += (num % 2 == mod) * (target // S - 3)

                # num = (dists[(y, x)]) + (target // S) * S
                # if num <= target:
                #     s += (num % 2 == (not mod)) * (target // S)
    print()

print(s+curr_sum)
exit()

for y in range(0, Y):
    for x in range(0, X):
        if (y, x) in dists:
            dist = dists[(y, x)]
            if dist % 2 == mod and dist <= target:
                s += 1
            for dy, dx in dirs + dirs_diag:
                dist = dists[(y+Y*2*dy, x+X*2*dx)] - S
                new = max(-1, (target - dist))
                if new >= 0:
                    # print(y, x, new, target, dist)
                    if new % 2 == mod:
                        div = S if dy == 0 or dx == 0 else S * 2
                        s += new // div + 1
            for dy, dx in dirs:
                dist = dists[(y+Y*2*dy, x+X*2*dx)] - S
                # print(dist)
                for side in [-1, 1]:
                    for i, rem in enumerate(range(target, -S*2, -S*2)):
                        new = max(-1, (rem - dist))
                        if new >= 0:
                            if new % 2 == mod:
                                s += (new) // S + 1

#
#          #---#
#          |###|
#          |###|
#          |###|
#          #---#

print(s)


# Too low:
# 618261433216623
# 618249208752749 wrong
# 618261433216623 same
