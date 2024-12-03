import re
s1, s2, enabled = 0, 0, True

for a, b, dont in re.findall(r"mul\((\d+),(\d+)\)|do(n't)?", open(0).read()):
    if a or b:
        s1 += int(a) * int(b)
        s2 += int(a) * int(b) * enabled
    else:
        enabled = dont == ''
print(s1, s2, sep="\n")
