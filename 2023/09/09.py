from sys import stdin

lines = stdin.read().strip().split('\n')

first = last = 0
for line in lines:
    diff = [int(a) for a in line.split()]
    sign = 1
    while any(diff):
        last += diff[-1]
        first += diff[0] * sign
        sign *= -1
        diff = [b - a for a, b in zip(diff, diff[1:])]

print(first, last, sep='\n')
