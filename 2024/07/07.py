from collections import *
from itertools import *
from functools import *
import operator
import re

d4 = [1, 1j, -1, -1j]
d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
def adjacent(coord, dirs=d4):
    return [coord + d for d in dirs]


def concat(a, b):
    return int(str(a) + str(b))


s1 = 0
for line in open(0):
    first, rest = line.split(": ")
    n = [int(a) for a in rest.split()]
    first = int(first)
    repeat = len(n) - 1
    for mask in range(1 << repeat):
        s = n[0]
        for i in range(repeat):
            op = [operator.add, operator.mul][bool((1 << i) & mask)]
            s = op(s, n[i+1])
            if s > first:
                break
        if s == first:
            s1 += first
            # print('found', first, bin(mask))
            break
    else:
        for mask in range(3**repeat):
            s = n[0]
            for i in range(repeat):
                mask, index = divmod(mask, 3)
                op = [operator.add, operator.mul, concat][index]
                s = op(s, n[i+1])
                if s > first:
                    break
            if s == first:
                s1 += first
                print('found', first)
                break
print(s1) 
    # re.findall(r"\d+", line)
# not 17866121572136
# not 5724973022478
