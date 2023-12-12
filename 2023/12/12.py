from sys import stdin
import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations

lines = stdin.read().strip().split('\n')

def decide(line, curr, needed, cache):
    tup = line, curr, needed
    if tup in cache:
        return cache[tup]
    if not line:
        return (needed or (0,)) == (curr,)

    s = 0
    if line[0] == '?':
        s += decide('.' + line[1:], curr, needed, cache)
        s += decide('#' + line[1:], curr, needed, cache)

    if line[0] == '#' and needed and curr < needed[0]:
        s += decide(line[1:], curr+1, needed, cache)

    if line[0] == '.':
        if needed and curr == needed[0]:
            s += decide(line[1:], 0, needed[1:], cache)
        if not needed or curr == 0:
            s += decide(line[1:], 0, needed, cache)

    cache[tup] = s
    return s


s1 = s2 = 0
for line in lines:
    chars, needed = line.split()
    needed = tuple(int(n) for n in needed.split(","))

    s1 += decide(chars, 0, needed, {})

    p2 = '?'.join([chars] * 5)
    s2 += decide(p2, 0, needed * 5, {})

print(s1, s2, sep='\n')
