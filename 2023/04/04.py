from sys import stdin

lines = stdin.read().strip().split("\n")
p = 0
repeat = [1] * len(lines)
for i, line in enumerate(lines):
    right, left = line.split(":")[1].split("|")
    shared = len(set(right.split()) & set(left.split()))
    if shared:
        p += 2**(shared - 1)
        for j in range(i+1, min(i+1+shared, len(lines))):
            repeat[j] += repeat[i]
print(p, sum(repeat), sep='\n')
