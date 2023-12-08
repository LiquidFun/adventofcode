from sys import stdin
import re
import math

rl, _, *lines = stdin.read().strip().split('\n')

parsed = [re.findall(r'[A-Z]{3}', line) for line in lines]
tree = {top: (left, right) for top, left, right in parsed}

def solve(curr, s=0):
    while not curr.endswith('Z'):
        curr = tree[curr][rl[s % len(rl)] == 'R']
        s+=1
    return s

print(solve("AAA"))
print(math.lcm(*[solve(top) for top in tree if top.endswith('A')]))


