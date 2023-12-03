from sys import stdin
from collections import defaultdict

lines = stdin.read().strip().split('\n')
gear_to_num = defaultdict(list)
s1 = 0

def is_valid(y, x):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0])

for y in range(len(lines)):
    for x_start in range(len(lines[y])):
        x_end = x_start
        if lines[y][x_start].isdigit() and (not is_valid(y, x_start-1) or not lines[y][x_start-1].isdigit()):
            while is_valid(y, x_end+1) and lines[y][x_end+1].isdigit():
                x_end += 1
            good = False
            for yd in range(y-1, y+2):
                for xd in range(x_start-1, x_end+2):
                    if is_valid(yd, xd) and lines[yd][xd] not in '.0123456789':
                        good = True
                        if lines[yd][xd] in '*':
                            gear_to_num[(yd, xd)].append(int(lines[y][x_start:x_end+1]))

            s1 += good * int(lines[y][x_start:x_end+1])

s2 = sum(n[0] * n[1] for n in gear_to_num.values() if len(n) == 2)
print(s1, s2, sep="\n")
