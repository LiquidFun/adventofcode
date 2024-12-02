is_safe = lambda n: sorted(n) in (n, n[::-1]) and all(1 <= abs(a - b) <= 3 for a, b in zip(n, n[1:]))

s1 = s2 = 0
for line in open(0):
    n = [int(a) for a in line.split()]
    s1 += is_safe(n)
    s2 += any(is_safe(n[:i] + n[i+1:]) for i in range(len(n)))
print(s1, s2, sep="\n")

