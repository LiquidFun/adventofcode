from sys import stdin
import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations

lines = stdin.read().strip().split('\n')
cache = {}

def decide(line, curr, needed):
    # print(line, curr, needed)
    # if needed and needed[0] == curr:
    #     needed = needed[1:]
    #     curr = 0
    tup = line, curr, needed
    if tup in cache:
        return cache[tup]
    if needed and needed[0] < curr:
        # print("===== False")
        cache[tup] = 0
        return 0
    if len(line) == 0:
        good = len(needed) == 1 and needed[0] == curr or not needed and curr == 0
        # print("=====", good)
        cache[tup] = good
        return good

    s = 0
    c = line[0]
    if needed and c == '?':
        if curr == needed[0]:
            s += decide(line[1:], 0, needed[1:])
        if curr < needed[0]:
            s += decide(line[1:], curr+1, needed)
    if c == '?':
        if 0 == curr:
            s += decide(line[1:], 0, needed)

    if c == '#' and needed:
        if curr < needed[0]:
            s += decide(line[1:], curr+1, needed)

    if c == '.':
        if needed and curr == needed[0]:
            s += decide(line[1:], 0, needed[1:])
        if not needed or curr == 0:
            s += decide(line[1:], 0, needed)
    # print("=====", s)
    cache[tup] = s
    return s


s = 0
for line in lines:
    chars, needed = line.split()
    needed = [int(n) for n in needed.split(",")]
    # curr_sum = decide(chars, 0, tuple(needed))
    p2 = '?'.join([chars] * 5)
    curr_sum = decide(p2, 0, tuple(needed * 5))
    cache.clear()
    print(chars * 5, needed * 5, curr_sum)
    s += curr_sum 
    print()
    print()
    print()
    # break

print(s)
