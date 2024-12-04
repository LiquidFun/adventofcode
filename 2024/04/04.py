X = [l.strip() + "   " for l in open(0).readlines()]
X.extend([" " * len(X[0])] * 3)
s1 = s2 = 0
dirs = [
    [(0, 0), (1, 1), (2, 2), (3, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(3, 0), (2, 1), (1, 2), (0, 3)],
]

for y in range(len(X)-3):
    for x in range(len(X[y])-3):
        for dir in dirs:
            s1 += ''.join(X[y+dy][x+dx] for dy, dx in dir) in ("XMAS", "SAMX")

        a = (X[y][x] + X[y+2][x+2]) in ("MS", "SM")
        b = (X[y+2][x] + X[y][x+2]) in ("MS", "SM")
        s2 += X[y+1][x+1] == "A" and a and b

print(s1, s2, sep="\n")
