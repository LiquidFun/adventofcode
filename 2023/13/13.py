from sys import stdin
import re
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations

fields = stdin.read().strip().split('\n\n')

def count_wrong_reflections(field, x):
    wrong = 0
    for y in range(len(field)):
        wrong += sum(a != b for a, b in zip(field[y][:x][::-1], field[y][x:]))
    return wrong

s1 = s2 = 0
for field in fields:
    field = field.split('\n')
    for x in range(1, len(field[0])):
        reflections = count_wrong_reflections(field, x)
        s1 += x if reflections == 0 else 0
        s2 += x if reflections == 1 else 0

    transposed = list(zip(*field))
    for y in range(1, len(transposed[0])):
        reflections = count_wrong_reflections(transposed, y)
        s1 += y*100 if reflections == 0 else 0
        s2 += y*100 if reflections == 1 else 0

print(s1, s2, sep="\n")
