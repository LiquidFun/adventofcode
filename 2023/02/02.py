import re
from sys import stdin
s1, s2 = 0, 0
for i, line in enumerate(stdin.readlines(), 1):
    r, g, b = [max(map(int, re.findall(fr"(\d+) {c}", line))) for c in "rgb"]
    s1 += (r <= 12 and g <= 13 and b <= 14) * i
    s2 += r * g * b

print(s1, s2, sep="\n")
