from sys import stdin
s1, s2 = 0, 0
for i, line in enumerate(stdin.readlines(), 1):
    _, subsets = line.split(":")
    r, g, b = 0, 0, 0
    for subset in subsets.split(';'):
        for showing in subset.split(","):
            num, color = showing.strip().split()
            globals()[color[0]] = max(globals()[color[0]], int(num))
    s1 += (r <= 12 and g <= 13 and b <= 14) * i
    s2 += r * g * b

print(s1, s2, sep="\n")
