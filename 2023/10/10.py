from sys import stdin
import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations


lines = stdin.read().strip().split('\n')

start = None

q = deque()

s = 0
for y, line in enumerate(lines):
    print(line)
    if 'S' in line:
        start = y, line.index('S')
        q.append((start, 0))

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

allowed = ["-7J", "|JL", "|F7", "-FL"]
allowed2 = ["-FLS", "|F7S", "|JLS", "-7JS"]

def is_valid(y, x):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0])

visited = set()
m = 0

inside = [['I'] * len(lines[0]) for line in lines]

blocked = set()

while len(q):
    curr, dist = q.popleft()
    y, x = curr
    m = max(m, dist)
    visited.add((y, x))
    blocked.add((y, x))
    inside[y][x] = '#'

    # for yinsi, insi in enumerate(inside):
    #     for xinsi, c in enumerate(insi):
    #         if c == '#':
    #             print(end=lines[yinsi][xinsi])
    #         else:
    #             print(end=c)
    #     print()
    # print()
    for (dy, dx), allow, allow2 in zip(dirs, allowed, allowed2):
        if is_valid(y+dy, x+dx) and lines[y+dy][x+dx] in allow and lines[y][x] in allow2:
            if (y+dy, x+dx) not in visited:
                q.append(((y+dy, x+dx), dist+1))
            blocked.add((y+dy/2, x+dx/2))
            blocked.add((y+dy, x+dx))

print(m)

for insi in inside:
    print(''.join(insi))
print()



q.clear()
visited.clear()


for y in range(len(lines)+1):
    q.append((y-0.5, -0.5))
    q.append((y, -0.5))
    q.append((y-0.5, len(lines[0]) - 0.5))
    q.append((y, len(lines[0]) - 0.5))

for x in range(len(lines[0])+1):
    q.append((-0.5, x-0.5))
    q.append((-0.5, x))
    q.append((len(lines) - 0.5, x - 0.5))
    q.append((len(lines) - 0.5, x))

dirtype = "hvvh"

def set_(y, x):
    if inside[y][x] == 'I':
        inside[y][x] = '.'
    #elif inside[y][x] == '#':
    #    inside[y][x] = 'B'

import math

while len(q):
    y, x = q.popleft()
    visited.add((y, x))

    if math.isclose(y, round(y)) and math.isclose(x, round(x)):
        set_(int(y), int(x))
    for (dy, dx), dirt in zip(dirs, dirtype):
        ya, xa = y+dy/2, x+dx/2
        if is_valid(ya, xa) and (ya, xa) not in visited:
            if (ya, xa) not in blocked:
                q.append((ya, xa))
                visited.add((ya, xa))
            if math.isclose(ya, round(ya)) and math.isclose(xa, round(xa)):
                set_(int(ya), int(xa))
            # if dirt == 'h':
            #     yup, ydown = int(ya-0.5), int(ya+0.5)
            #     xa = int(xa)
            #     if is_valid(yup, xa) and is_valid(ydown, xa):
            #         set(yup, xa)
            #         set(ydown, xa)
            #         con = lines[yup][xa] + lines[ydown][xa]
            #         if con[0] in 'L-J.' or con[1] in 'F-7.':
            #             visited.add((y+dy, x+dx))
            #             q.append((y+dy, x+dx))
            # if dirt == 'v':
            #     xleft, xright = int(xa-0.5), int(xa+0.5)
            #     ya = int(ya)
            #     if is_valid(ya, xleft) and is_valid(ya, xright):
            #         set(ya, xleft)
            #         set(ya, xright)
            #         con = lines[ya][xleft] + lines[ya][xright]
            #         if con[0] in '7|J.' or con[1] in 'F|L.':
            #             visited.add((y+dy, x+dx))
            #             q.append((y+dy, x+dx))


# while len(q):
#     y, x = q.popleft()
#     visited.add((y, x))
#     print(y, x)
#     for (dy, dx), dirt in zip(dirs, dirtype):
#         ya, xa = y+dy/2, x+dx/2
#         if is_valid(ya, xa) and (y+dy, x+dx) not in visited:
#             if dirt == 'h':
#                 yup, ydown = int(ya-0.5), int(ya+0.5)
#                 xa = int(xa)
#                 if is_valid(yup, xa) and is_valid(ydown, xa):
#                     set(yup, xa)
#                     set(ydown, xa)
#                     con = lines[yup][xa] + lines[ydown][xa]
#                     if con[0] in 'L-J.' or con[1] in 'F-7.':
#                         visited.add((y+dy, x+dx))
#                         q.append((y+dy, x+dx))
#             if dirt == 'v':
#                 xleft, xright = int(xa-0.5), int(xa+0.5)
#                 ya = int(ya)
#                 if is_valid(ya, xleft) and is_valid(ya, xright):
#                     set(ya, xleft)
#                     set(ya, xright)
#                     con = lines[ya][xleft] + lines[ya][xright]
#                     if con[0] in '7|J.' or con[1] in 'F|L.':
#                         visited.add((y+dy, x+dx))
#                         q.append((y+dy, x+dx))

for insi in inside:
    print(''.join(insi).replace("#", "_"))
print()

for y in range(len(lines) * 2):
    for x in range(len(lines[0]) * 2):
        c = ' '
        if (y / 2, x / 2) in blocked:
            c = '#'
        if (y / 2, x / 2) in visited:
            c = '.'
        print(end=c)
    print()
print()

outsides = 0
for line in inside:
    outsides += line.count('I')

print(outsides)
