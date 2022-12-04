import sys

s1 = s2 = 0
for line in sys.stdin.readlines():
    a, b, c, d = map(int, line.strip().replace(",", "-").split("-"))
    range1, range2 = set(range(a, b+1)), set(range(c, d+1))

    s1 += len(range1 & range2) in (b-a+1, d-c+1)
    s2 += bool(range1 & range2)

print(s1)
print(s2)

