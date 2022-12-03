import sys
import string
s1, s2 = 0, 0
lines = sys.stdin.read().strip().split("\n")

for line in lines:
    half = len(line) // 2
    for c in set(line[:half]) & set(line[half:]):
        s1 += string.ascii_letters.index(c) + 1

for l1, l2, l3 in zip(lines[0::3], lines[1::3], lines[2::3]):
    for c in set(l1) & set(l2) & set(l3):
        s2 += string.ascii_letters.index(c) + 1

print(s1)
print(s2)
