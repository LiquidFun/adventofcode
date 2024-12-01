n = [int(a) for a in open(0).read().split()]

s1 = s2 = 0
for a, b in zip(sorted(n[::2]), sorted(n[1::2])):
    s1 += abs(a - b)
    s2 += a * n[1::2].count(a)
print(s1, s2, sep="\n")
