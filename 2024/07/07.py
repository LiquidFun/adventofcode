from operator import *

def concat(a, b):
    return int(str(a) + str(b))

s1 = s2 = 0
for line in open(0):
    first, rest = line.split(": ")
    n = [int(a) for a in rest.split()]
    first = int(first)
    repeat = len(n) - 1
    for mask in range(3**repeat):
        s = n[0]
        for_part1 = True
        for i in range(repeat):
            mask, index = divmod(mask, 3)
            for_part1 &= index != 2
            op = [add, mul, concat][index]
            s = op(s, n[i+1])
            if s > first:
                break
        if s == first:
            s1 += first * for_part1
            s2 += first
            break

print(s1, s2, sep="\n") 
