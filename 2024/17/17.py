from collections import *
from itertools import *
from functools import *
from operator import *
# import numpy as np
import networkx as nx
# import z3
import re
import sys
sys.setrecursionlimit(1000000)

s1 = s2 = 0
# coords = {x+1j*y: c for y, r in enumerate(open(0)) for x, c in enumerate(r.strip())}

# d4 = [1, 1j, -1, -1j]
# d8 = d4 + [1+1j, 1-1j, -1+1j, -1-1j]
# d4half = [i/2 for i in d4]
# d8half = [i/2 for i in d8]
# def adjacent(coord, dirs=d4):
#     return [coord + d for d in dirs]




# for line in open(0):
#     n = [int(a) for a in line.split()]
a, b, c, *nums = [int(a) for a in re.findall(r"\d+", open(0).read())]


def solve(A):
    init = A
    solution = []
    B = C = 0
    def combo(n):
        return {4:A, 5:B, 6:C}.get(n, n)
    inst = 0
    while inst < len(nums):
        op = nums[inst]
        num = nums[inst+1]
        # print(op, num, f"{A=} {B=} {C=}")
        match op:
            case 0:
                A = A // 2**combo(num)
            case 1:
                B ^= num
            case 2:
                B = combo(num) % 8
            case 3:
                if A != 0:
                    inst = num
                    continue
            case 4:
                B = B ^ C
            case 5:
                val = combo(num) % 8
                solution.append(val)
                if val != nums[len(solution)-1]:
                    return solution
                # print(combo(num) % 8, end=",")
            case 6:
                B = A // 2**combo(num)
            case 7:
                C = A // 2**combo(num)
        inst += 2
    if solution == nums:
        print(nums)
        print(solution)
        print(init)
        exit(0)
    return solution

lo = 2**(3*15)
lo = 37221200000000
   # 37221261688308
hi = 37221265882612-1

for i in range(lo, hi):
    # solve(i)
    lin = solve(i)
    # print(i, lin)

print(nums)
# print(solve(117440))
print(lo, hi)
# 8 64 512 4096
# 3 6  9   
# lo = 0
# hi = 2**100
import random
from math import *

mi, ma = 1e999, 0
while True:
    n= random.randint(lo, hi)
    s = solve(n)
    # print(f"{log2(n)} -> {len(s)}")
    # assert len(s) == len(nums), f"{log2(n)}"
    if s[-12:] == nums[-12:]:
        mi = min(mi, n)
        ma = max(ma, n)
        print(log2(n), n, s, mi, ma)

def to_num(curr):
    return ''.join(map(str, reversed(curr)))

while lo <= hi:
    mid = (lo + hi) // 2
    print(mid, solve(mid))
    curr = to_num(solve(mid))
    # loo = to_num(solve(lo))
    # hii = to_num(solve(lo))
    print(curr)
    num = to_num(nums)
    print(num)
    if len(curr) < len(num) or curr < num:
        lo = mid+1
    else:
        hi = mid
    

exit(0)

l = 0
for i in range(2**(3*15), 2**100):
    # solve(i)
    lin = solve(i)
    # if len(lin) != l:
    #     print(i, l)
    #     l = len(lin)
    # print(f"{i} -> ", lin)

# 2,0,4,0,7,2,3,4,0
    

# too high 37221265882612

# print(s1, s2, sep="\n")
